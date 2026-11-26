# Router Optimization

- 日期：2026-11-26
- 分支：`retrieval-optimization`
- 上一版：`1c72000`（Self-query 翻译版）
- 当前版：规则路由 + 混合检索 + 兄弟 chunk 重构 + 生成评测 + 语言一致性提示词

## 1. 版本目标

上一版已经完成：

- 向量检索、Cross-Encoder 重排、doc_type 惩罚
- `doc_type` / `platform` 元数据
- Self-query 查询翻译
- 页面级 Hit@k / MRR / nDCG 评测

但上一版仍有两个核心问题：

1. **全量 Self-query 会误加 filter**：q032/q034/q035/q043 等普通问题被加上 `platform` / `doc_type` 过滤，直接导致原本可命中的页面失败。
2. **目标页召回不足**：q001/q010/q044 在 dense 向量阶段就没有进入候选集，reranker 无法补救。

当前版本的目标是：

```text
明确元数据约束 → Self-query
普通问题       → 普通检索
两者都使用     → 重排
召回不足       → BM25 + dense 混合
答案跨 chunk   → 兄弟 chunk 合并
```

## 2. 修改总览

| 模块 | 修改 | 主要文件 |
|---|---|---|
| 查询路由 | 新增硬规则路由，输出 `route`、`signals`、`allowed_fields` | `src/my_rag/core/router.py` |
| Self-query 约束 | 只向 Self-query 暴露路由允许的 metadata 字段 | `src/my_rag/core/retriever.py` |
| 混合检索 | BM25 0.3 + dense 0.7，加权融合 | `src/my_rag/core/hybrid.py` |
| Chunk 重构 | 按 `parent_id` 合并兄弟 chunk，再精排 | `src/my_rag/core/chunk_catalog.py` |
| 索引元数据 | 增加 `doc_id`、`parent_id`、`section_index`、`chunk_index`、`content_hash` | `src/my_rag/ingestion/splitter.py` |
| 索引构建 | 去重、重建 Chroma、缓存 BM25/catalog | `src/my_rag/pipeline.py`、`scripts/rebuild_index_v2.py` |
| 生成评测 | 7 维生成质量评测，gold_answer / gold_docs 两种 oracle context | `tests/test_AnswerGeneration.py` |
| 语言一致性 | 显式语言规则 + `answer_language` + 单次语言校正重试 | `src/my_rag/core/rag_chain.py` |
| 评测集 | 增加 `expected_router`、`citation_required`、`expected_refusal` | `tests/evaluation/qa_set.jsonl` |

## 3. 查询路由

### 3.1 规则

路由是纯硬规则，不调用 LLM：

| 信号 | 触发条件 | 允许字段 |
|---|---|---|
| URL | `https://docs.langchain.com/...` | `url` |
| 标题 | 中文 `《标题》`，或英文 `doc/page titled "标题"` | `title` |
| JavaScript | `JavaScript`、`JS`、`TypeScript` | `platform` |
| Python | 仅 `Python 版/版本/文档/docs/documentation`，不匹配 `Python SDK`、`Python 3.10` | `platform` |
| doc_type | changelog、release notes、troubleshooting、API reference、quickstart、明确的 tutorial、release policy | `doc_type` |
| 排除条件 | `exclude/不要/排除/仅限/只看` + 已知 metadata 目标 | 对应字段 |

约束：

- URL/title 命中时，只允许对应单字段，避免 Self-query 额外加 `platform/doc_type`。
- URL 和标题内的词会被 mask，避免 `.../javascript/...` 或 `Tracing quickstart` 误触发 platform/doc_type。
- 没有命中任何规则 → `default` 普通检索。

### 3.2 路由评测

`tests/evaluation/test_router/router_report.md`：

```text
total = 62
accuracy = 1.0000
self_query precision = 1.0000
self_query recall = 1.0000
self_query f1 = 1.0000

expected self_query, predicted self_query: 19
expected self_query, predicted default:    0
expected default, predicted self_query:    0
expected default, predicted default:       43
```

注意：这 62 条的 `expected_router` 是围绕当前规则标注的，1.0 只代表规则覆盖验证，不代表未知问法的泛化准确率。

## 4. Router v1：路由 + 重排

`tests/evaluation/test_SelfQuery/test_RouterQuery.json`：

| 指标 | penalty baseline | translate baseline | Router v1 |
|---|---:|---:|---:|
| Hit@1 | 0.6842 | 0.6316 | **0.7544** |
| Hit@5 | 0.9123 | 0.8596 | **0.9474** |
| Hit@10 | 0.9474 | 0.8947 | **0.9649** |
| MRR@5 | 0.7769 | 0.7325 | **0.8363** |
| nDCG@5 | 0.8110 | 0.7651 | **0.8645** |

按路由拆分（k=5）：

| 路由 | n | Hit@5 | MRR@5 |
|---|---:|---:|---:|
| `self_query` | 19 | 1.0000 | 0.9737 |
| `default` | 38 | 0.9211 | 0.7675 |

相对 penalty baseline：

- 修复：q026、q057
- 新增失败：无
- 仍然失败：q001、q010、q044

### 4.1 这三条结果直接决定了下一步

- **q001**：目标 overview 没有进入向量候选，属于 dense 召回失败。
- **q010**：top 1 是同一页面的 JavaScript 版本，Python 目标页未进 top 5；同时答案跨多个兄弟 chunk。
- **q044**：目标页没有被召回；`build-overview.md` 原始数据存在大量重复段落，答案被拆在多个 H2。

因此引入：

1. BM25 + dense 混合，补足精确术语和概念页召回；
2. 兄弟 chunk 合并，解决答案跨 chunk；
3. 索引去重和 parent metadata，解决重复页面和合并顺序。

## 5. Hybrid + 兄弟 chunk 重构

### 5.1 检索参数

```text
BM25 weight  = 0.3
dense weight = 0.7
candidate_k  = 50
coarse_k     = 20
final_k      = 5
sibling_window = 2
max_chars      = 3000
```

流程：

```text
query
  → dense top 50 + BM25 top 50
  → 加权融合
  → rerank 粗排 top 20
  → 按 parent_id 合并兄弟 chunk
  → 最终精排池 = 原始命中 chunk + 合并父块
  → rerank
  → 按 URL 去重，返回 top 5
```

保留原始命中 chunk 是为了避免 q019 这类聚焦型问题被合并父块稀释。

### 5.2 Router v2 结果

`tests/evaluation/test_router/router_v2_report.json`：

| 指标 | Router v1 | Router v2 | Δ |
|---|---:|---:|---:|
| Hit@1 | 0.7544 | 0.7544 | 0.0000 |
| Hit@3 | 0.9123 | **0.9298** | +0.0175 |
| Hit@5 | 0.9474 | **0.9649** | +0.0175 |
| MRR@5 | 0.8363 | **0.8450** | +0.0088 |
| nDCG@5 | 0.8645 | **0.8756** | +0.0111 |

按路由（k=5）：

| 路由 | n | v1 Hit@5 | v2 Hit@5 | v1 MRR@5 | v2 MRR@5 |
|---|---:|---:|---:|---:|---:|
| `self_query` | 19 | 1.0000 | 1.0000 | 0.9737 | 0.9737 |
| `default` | 38 | 0.9211 | **0.9474** | 0.7675 | **0.7807** |

案例变化：

- 修复：q044（未命中 → rank 4）
- 保持：q019 rank 1
- 无新增失败
- 仍然失败：q001、q010

q010 的 top 1 仍然是同一页面的 JavaScript 版本；如果按平台归一化，它是语义命中，但严格 URL 评测仍算失败。

## 6. 索引重建

`scripts/rebuild_index_v2.py` 已完成：

| 项目 | 结果 |
|---|---:|
| 去重后 chunk | 42,650 |
| 新向量库 chunk | 42,650 |
| 新向量库大小 | 360.36 MB |
| 旧向量库备份 | `data/vector_store_v1_backup`，1,052.84 MB |
| catalog/BM25 缓存 | `data/cache/chunk_catalog.pkl`，38.06 MB |
| 缓存加载耗时 | 0.84 秒 |

新增 metadata：

```text
doc_id
parent_id
section_index
chunk_index
content_hash
```

说明：

- 旧索引 43,245 chunk，新索引 42,650 chunk，减少 595 个重复 chunk。
- 旧索引保留为 `data/vector_store_v1_backup`，可回滚。
- Chroma 和 cache 不提交到 Git。

## 7. 生成节点评测

`tests/test_AnswerGeneration.py` 对 62 条样本做了两种 oracle context 评测：

- `gold_answer`：直接把参考答案作为 context；
- `gold_docs`：使用参考答案对应的完整文档页面作为 context。

评测维度：

```text
correctness
faithfulness
completeness
citation_accuracy
refusal_correct
language_consistency
conciseness
```

### 7.1 结果

`tests/evaluation/test_generation/generation_report.json`：

| 模式 | correctness | faithfulness | completeness | citation | refusal | language | conciseness |
|---|---:|---:|---:|---:|---:|---:|---:|
| `gold_answer` | 1.0000 | 1.0000 | 0.9758 | N/A | 1.0000 | 1.0000 | 0.9919 |
| `gold_docs` | 1.0000 | 1.0000 | 0.9919 | 1.0000 | 1.0000 | 0.9839 | 1.0000 |

### 7.2 关键案例

- q052：英文问题、中文回答，语言一致性失败。
- q034：`completeness=1`，缺少子 run 场景下 `trace_id` 可选但推荐的补充说明。
- q028/q035/q061：第一版 `gold_docs` 只取 top 4 父块，答案段落被截断，导致误拒答；改为完整页面 context 后全部恢复。

### 7.3 重要限制

生成评测使用的是 **oracle context**，不是真实检索链路：

- `gold_answer` 的正确性会偏高；
- `gold_docs` 给的是完整正确页面，仍然不是生产 top 3~5；
- 真实 RAG 的生成质量还需要用 router v2 的检索结果再测一轮。

## 8. 语言一致性提示词

q052 暴露了语言不一致问题。当前版本修改了 `src/my_rag/core/rag_chain.py`：

- 在 system prompt 中增加最高优先级语言规则；
- human prompt 增加确定性的 `answer_language`；
- 增加 `detect_answer_language()` 和 `language_matches()`；
- 如果回答语言不匹配，使用 `LANGUAGE_RETRY_PROMPT` 进行一次语言校正；
- 代码、API 名称、参数、命令、URL 不翻译。

修改后 q052 单例复测通过：英文问题 → 英文回答，`language_consistency=1`。

注意：`generation_report.json` 是提示词修改前的结果，q052 仍记录为失败；单例复测已经验证修复，完整生成报告尚未重新跑。

## 9. 测试结果与决策对应关系

| 测试结果 | 决策 |
|---|---|
| 全量 Self-query 在 q032/q034/q035/q043 误加 filter | 引入规则路由，只让明确 metadata 问题走 Self-query |
| Self-query 对 q026/q057 有效，metadata_filter Hit@5=1.0 | 保留 Self-query，但限制 allowed_fields |
| Router v1 修复 q026/q057，但 q001/q010/q044 仍失败 | 引入混合召回和兄弟 chunk 重构 |
| q001 目标页 dense 未召回 | BM25 + dense，补精确术语 |
| q010 答案跨 chunk，且 JS/Python 重复页 | 兄弟合并 + 平台归一化讨论 |
| q044 原始 Markdown 重复、答案跨 H2 | 索引去重 + parent/sibling metadata |
| Router v2 修复 q044，但 q019 回退 | 最终精排池保留原始 chunk + 合并父块 |
| q052 英文问题中文回答 | 强化语言提示词 + 确定性语言重试 |
| q028/q035/q061 在 gold_docs 中误拒答 | 生成评测改为完整页面 oracle context |

## 10. RAGChain 接入与端到端评测

`RAGChain.ask()` 已接入：

```text
route_query
  → Self-query allowed_fields / 原始 query
  → BM25 + dense hybrid
  → 兄弟 chunk 合并
  → reranker
  → LLM
  → 语言一致性保护
```

最终端到端报告：

- `tests/evaluation/final_test/final_pipeline_report.json`
- `tests/evaluation/final_test/final_pipeline_report.md`

结果：

| 指标 | 值 |
|---|---:|
| Retrieval Hit@5 | 0.9649 |
| Retrieval MRR@5 | 0.8450 |
| correctness | 0.9758 |
| faithfulness | 1.0000 |
| completeness | 0.9516 |
| citation_accuracy | 1.0000 |
| refusal_accuracy | 0.9839 |
| language_consistency | 1.0000 |
| conciseness | 1.0000 |

检索指标与 Router v2 一致；图扩展不改变 retrieval 排序，只扩展生成 context。  
结构图包含 Page / Section / Chunk / NEXT_CHUNK / NEXT_SECTION / SAME_TOPIC_AS，规模为 58,675 nodes、98,114 edges、14,376 sections。

图增强后，q003/q018/q026/q035/q040/q043 等 context 缺失案例恢复到 2/2；q041 仍失败；q001/q010 仍是 retrieval miss，但生成回答已明显改善。

最终端到端 correctness=0.9758、completeness=0.9516、citation=1.0、refusal=0.9839。

并发评测时还修复了一个 reranker 缓存问题：`get_cross_encoder()` 和 `get_cross_encoder(None)` 是两个不同的 `lru_cache` key，导致多线程重复加载模型；现在 `build_reranker` 统一使用 `get_cross_encoder()`，并在并发前预热。

## 11. 当前版本仍未解决的问题

1. **q001**：概念页 dense 召回不足，BM25 0.3 也没有把它带进候选；需要更强的多语言 embedding、query expansion 或标题/实体召回。
2. **q010**：Python 目标页没有进入 top 5，top 1 是 JavaScript 同页；需要平台归一化或更明确的平台意图。
3. **路由泛化**：62 条规则覆盖准确率 1.0，不代表未知问法；需要边界问法、真实用户问法。
4. **q041 仍失败**：run 生命周期页面未被召回，结构图无法从错误页面扩展出答案；需要实体图或更好的页面级召回。
5. **平台/标注粒度**：Python/JavaScript 双版本和单 URL 标注会放大失败率；q010 语义上已能回答，但严格 URL 评测仍失败。

## 12. 复现

```powershell
# 重建索引和 BM25 cache
python scripts/rebuild_index_v2.py

# Router 评测
python src/my_rag/core/router.py

# Router v1 / v2 检索评测
python tests/test_RouterQuery.py
python tests/test_RouterQuery_v2.py

# 生成评测（gold_answer + gold_docs）
python tests/test_AnswerGeneration.py --workers 4 --timeout 180 --restart

# 端到端完整流程评测
python tests/test_FinalPipeline.py --workers 2 --timeout 180 --restart
```

主要报告：

```text
tests/evaluation/test_router/router_report.md
tests/evaluation/test_router/router_v2_report.md
tests/evaluation/test_SelfQuery/test_RouterQuery.md
tests/evaluation/test_generation/generation_report.md
tests/evaluation/test_SelfQuery/router_failure_analysis.md
tests/evaluation/final_test/final_pipeline_report.md
```
