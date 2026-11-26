# My RAG：LangChain 文档智能问答

基于 LangChain 官方文档的 RAG 问答系统。项目从最基础的「Markdown 加载 → 标题切分 → Chroma 向量检索 → DeepSeek 回答」开始，经过重排、元数据、Self-query、查询路由、BM25 混合检索、兄弟 chunk 重构、生成评测和文档结构图扩展，逐步演进为当前的端到端流程。

本文既是 README，也是当前版本的项目报告，重点说明：

- 从初始架构到当前版本做了哪些修改；
- 每项修改基于哪次评测结果；
- 当前指标、失败案例和限制；
- 如何复现。

---

## 1. 项目概览

- 文档：1,733 篇 LangChain / LangSmith Markdown 文档
- 当前索引：42,650 个去重 chunk
- 向量库：Chroma，collection `langchain_docs`
- 向量模型：`IEITYuan/Yuan-embedding-2.0-en`
- 重排模型：`BAAI/bge-reranker-v2-m3`
- 生成模型：DeepSeek `deepseek-chat`
- 评测集：62 条，其中 57 条可回答、5 条不可回答
- 当前端到端结果：
  - Retrieval Hit@5：**0.9649**
  - Retrieval MRR@5：**0.8450**
  - Generation correctness：**0.9758**
  - Generation completeness：**0.9516**
  - Faithfulness：**1.0000**
  - Citation accuracy：**1.0000**

> 当前 `RAGChain.ask()` 已接入 router、hybrid、兄弟 chunk 合并、文档结构图上下文扩展和语言一致性保护。

---

## 2. 当前架构

```text
┌─────────────────────────────────────────────────────────────┐
│ 离线索引                                                     │
│                                                             │
│  Markdown 文档                                              │
│    → loader.py：frontmatter + doc_type / platform           │
│    → splitter.py：标题切分 + 递归切分 + parent/section 元数据│
│    → 去重                                                   │
│    → Chroma 向量库                                          │
│    → chunk_catalog / BM25 cache                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 在线问答                                                     │
│                                                             │
│  用户问题                                                   │
│    → router.py：规则路由                                     │
│        ├─ self_query：Self-query 翻译 + allowed_fields      │
│        └─ default：原始 query                               │
│    → hybrid.py：BM25 0.3 + dense 0.7                        │
│    → 粗排 rerank                                            │
│    → 兄弟 chunk 合并（parent_id）                            │
│    → 最终 rerank，按 URL 去重（评测 top5；生产默认 k=4）    │
│    → document_graph.py：结构图 context 扩展                 │
│    → context rerank top 8                                   │
│    → rag_chain.py：Prompt + LLM + 语言一致性保护            │
└─────────────────────────────────────────────────────────────┘
```

### 2.1 当前代码结构

```text
src/my_rag/
├── config.py                 # 项目路径与配置
├── cli.py                    # 命令行入口
├── pipeline.py               # 加载 → 去重 → 嵌入 → Chroma → BM25 cache
├── ingestion/
│   ├── loader.py             # DirectoryLoader、frontmatter、doc_type/platform
│   └── splitter.py           # 标题切分、递归切分、doc_id/parent_id 等
├── model/
│   ├── embedding.py          # Yuan-embedding-2.0-en
│   ├── llm.py                # DeepSeek
│   └── reranker.py           # bge-reranker-v2-m3 + doc_type 惩罚
├── core/
│   ├── vector_store.py       # Chroma 建库/加载
│   ├── retriever.py          # 普通检索、Self-query、allowed_fields
│   ├── router.py             # 硬规则查询路由
│   ├── chunk_catalog.py      # 去重 catalog、BM25、兄弟合并、缓存
│   ├── hybrid.py             # BM25 + dense 融合与两阶段重排
│   ├── document_graph.py     # Page/Section/Chunk 结构图与 context 扩展
│   └── rag_chain.py          # 当前端到端 RAGChain
scripts/
├── build_index.py
├── rebuild_index_v2.py       # 重建带 parent metadata 的索引与 cache
└── chat.py
tests/
├── test_retriever.py         # 纯向量 / rerank 检索评测
├── test_SelfQuery.py         # Self-query 改写、filter、检索评测
├── test_RouterQuery.py       # Router v1 检索评测
├── test_RouterQuery_v2.py    # Hybrid + chunk 重构评测
├── test_AnswerGeneration.py  # 生成质量 7 维评测
├── test_FinalPipeline.py     # RAGChain 端到端流程评测
└── evaluation/
    ├── qa_set.jsonl
    ├── title_catalog.json
    ├── test_retrieval/
    ├── test_SelfQuery/
    ├── test_router/
    ├── test_generation/
    └── final_test/
```

---

## 3. 当前数据与索引

### 3.1 文档与 chunk

- Markdown 文档：1,733 篇
- 切分后 chunk：43,245 个
- 去重后 chunk：**42,650 个**
- chunk 最大 512 字符，overlap 50
- 索引路径：`data/vector_store/`（不提交 Git）
- BM25/catalog 缓存：`data/cache/chunk_catalog.pkl`
- 旧索引备份：`data/vector_store_v1_backup/`

当前索引由 `scripts/rebuild_index_v2.py` 重建：

| 项目 | 结果 |
|---|---:|
| 新索引 chunk | 42,650 |
| 新索引大小 | 360.36 MB |
| 旧索引 chunk | 43,245 |
| 旧索引大小 | 1,052.84 MB |
| catalog/BM25 缓存 | 38.06 MB |
| 缓存加载耗时 | 0.84 秒 |

减少的 595 个 chunk 主要来自重复段落，例如 `build-overview.md` 中重复出现的 Managed Deep Agents / Deep Agents 段落。

### 3.2 元数据

frontmatter 原始字段：

```text
title
url
scraped_at
word_count
```

由 frontmatter 或正文衍生出的字段：

| 字段 | 来源 |
|---|---|
| `doc_type` | `url` + `title`，规则见 `loader.py` |
| `platform` | `url` + `title`，Python / JavaScript / agnostic |
| `source` | TextLoader 文件路径 |
| `doc_id` | `url`，没有 URL 时使用 `source` |
| `h1/h2/h3` | Markdown 标题层级 |
| `parent_id` | `doc_id` + 父级标题路径 |
| `section_index` | 标题 section 顺序 |
| `chunk_index` | 文档内 chunk 全局顺序 |
| `content_hash` | chunk 文本 SHA-1 |

当前 `doc_type` 分布：

```text
guide           898
api_reference   720
concept          68
quickstart       15
troubleshooting  14
changelog         6
tutorial          5
release           4
policy            3
```

当前 `platform` 分布：

```text
agnostic    1271
javascript   233
python       229
```

---

## 4. 评测集与指标

评测集：`tests/evaluation/qa_set.jsonl`

- 总 62 条
- 57 条可回答，5 条不可回答
- 语言：中文 41 条，英文 21 条
- 类型：how_to 19、conceptual 11、factual 7、configuration 3、metadata_filter 15、troubleshooting 2、unanswerable 5
- 15 条 metadata_filter：7 条按 URL 过滤，8 条按 title 过滤

关键字段：

```text
id
question
reference_answer
relevant_urls
type
language
answerable
expected_filter
expected_router
must_keep_terms
rewrite_required
source_title
review_status
citation_required
expected_refusal
```

检索指标（57 条可回答样本，页面 URL 去重）：

- **Hit@k**：top-k 至少命中一个相关页面的问题比例
- **Recall@k**：命中相关 URL 数 / 标注相关 URL 总数
- **MRR@k**：第一个相关页面排名的倒数平均值
- **nDCG@k**：按排名折损并归一化的相关性分数

生成指标（62 条，含无答案样本）：

- correctness
- faithfulness
- completeness
- citation_accuracy
- refusal_correct
- language_consistency
- conciseness

---

## 5. 从初始架构到当前版本

### 5.1 初始版本：基础 RAG

初始流程：

```text
Markdown
→ DirectoryLoader + TextLoader
→ MarkdownHeaderTextSplitter
→ RecursiveCharacterTextSplitter（512 / overlap 50）
→ Yuan-embedding-2.0-en
→ Chroma
→ 向量 similarity_search
→ DeepSeek 回答
```

初始基线（57 条可回答样本）：

| 指标 | 值 |
|---|---:|
| Hit@1 | 0.4211 |
| Hit@5 | 0.8070 |
| Hit@10 | 0.9123 |
| MRR@5 | 0.5792 |
| nDCG@5 | 0.6366 |
| @5 失败数 | 11 / 57 |

失败集中体现为：

1. top-1 精度不足，大量相关页面排在 6~10；
2. 中文 query 与英文文档跨语言匹配弱；
3. changelog/release 页面很长、关键词密度高，挤占普通文档；
4. Python/JavaScript 双版本文档互相挤占；
5. 元数据过滤题（title/url）无法靠普通向量检索解决；
6. 真正包含答案的 chunk 有时没有进入 top-30。

### 5.2 重排：base reranker → bge-reranker-v2-m3

先加入 Cross-Encoder 重排：

```text
向量召回 candidate_k=30
→ CrossEncoder 对 30 个候选打分
→ 按分数排序
→ 取 top_n
```

对比：

| k | 初始基线 Hit | base-rerank Hit | v2-m3 Hit |
|---:|---:|---:|---:|
| 1 | 0.4211 | 0.5263 | **0.6667** |
| 5 | 0.8070 | 0.8246 | **0.9123** |
| 10 | 0.9123 | 0.8596 | **0.9474** |

中文 36 条：

| 指标 | 初始基线 | base-rerank | v2-m3 |
|---|---:|---:|---:|
| Hit@5 | 0.7778 | 0.7778 | **0.8611** |
| MRR@5 | 0.5690 | 0.6227 | **0.7347** |
| nDCG@5 | 0.6217 | 0.6624 | **0.7668** |

结论：

- base-rerank 提升 top-1，但 Hit@10 下降，并新增失败；
- v2-m3 同时改善 top-1、top-10 和中文指标；
- **采用 `BAAI/bge-reranker-v2-m3`**，base 不作为默认。

### 5.3 candidate_k：30 vs 50

| 配置 | Hit@1 | Hit@5 | Hit@10 | MRR@5 | nDCG@5 | @5 失败 |
|---|---:|---:|---:|---:|---:|---:|
| v2-m3 + 30 | 0.6667 | **0.9123** | 0.9474 | 0.7673 | **0.8037** | **5** |
| v2-m3 + 50 | 0.6667 | 0.8947 | 0.9474 | 0.7681 | 0.8005 | 6 |

candidate_k=50 没有收益，中文指标还略降，因此普通向量检索阶段保留 30。

> 后续 Hybrid 阶段重新使用 candidate_k=50，是因为 BM25 与 dense 需要融合候选，属于不同实验配置。

### 5.4 doc_type 元数据与惩罚

为区分 changelog/release 等长文档，增加 `doc_type` 元数据，并在 reranker 中加入惩罚：

```python
penalties = {"changelog": 0.05, "release": 0.03}
final_score = rerank_score - penalty
```

结果：

| 指标 | 无惩罚 | 有惩罚 |
|---|---:|---:|
| Hit@1 | 0.6667 | **0.6842** |
| Hit@5 | 0.9123 | 0.9123 |
| MRR@5 | 0.7673 | **0.7769** |
| nDCG@5 | 0.8037 | **0.8110** |
| top-5 changelog 次数 | 7 | **3** |

惩罚主要改善 changelog 挤占，release 改善有限；Hit@5 不变，top-1/MRR/nDCG 小幅提升，因此采用为默认策略。

### 5.5 Self-query 与查询翻译

Self-query 目标：

```text
query
→ LLM 拆成 search_query + metadata_filter
→ filter 限定 url / title / platform / doc_type
→ 向量检索
→ rerank
```

评测结果：

- 15 条 metadata_filter 的 filter 全部精确匹配；
- metadata_filter 子集 Hit@5 = **1.0000**；
- q026/q057 被修复；
- 但全量 Self-query 整体 Hit@5 **0.8596**，低于 penalty baseline **0.9123**；
- q032/q034/q035/q043 等普通问题被错误加上 `platform/doc_type` filter，导致失败。

结论：Self-query 对明确 metadata 约束有效，但不能全量启用，需要查询路由。

### 5.6 查询路由

新增硬规则路由 `src/my_rag/core/router.py`：

| 信号 | 触发条件 | allowed_fields |
|---|---|---|
| URL | `https://docs.langchain.com/...` | `url` |
| 标题 | `《标题》` / `doc titled "标题"` | `title` |
| JavaScript | JavaScript / JS / TypeScript | `platform` |
| Python | 仅 `Python 版/版本/文档` 等上下文 | `platform` |
| doc_type | changelog / release notes / troubleshooting / API reference / quickstart / tutorial / policy | `doc_type` |
| 排除条件 | exclude / 不要 / 排除 / 仅限 / 只看 + metadata 目标 | 对应字段 |

路由结果：

```text
62 条 accuracy = 1.0000
self_query precision/recall/F1 = 1.0000
19 条 self_query
43 条 default
```

> 1.0 是规则覆盖验证，不代表未知问法的泛化准确率。

Router v1 检索结果：

| 指标 | penalty baseline | translate baseline | Router v1 |
|---|---:|---:|---:|
| Hit@1 | 0.6842 | 0.6316 | **0.7544** |
| Hit@5 | 0.9123 | 0.8596 | **0.9474** |
| Hit@10 | 0.9474 | 0.8947 | **0.9649** |
| MRR@5 | 0.7769 | 0.7325 | **0.8363** |
| nDCG@5 | 0.8110 | 0.7651 | **0.8645** |

按路由：

| 路由 | n | Hit@5 | MRR@5 |
|---|---:|---:|---:|
| self_query | 19 | 1.0000 | 0.9737 |
| default | 38 | 0.9211 | 0.7675 |

修复 q026/q057，剩余失败 q001/q010/q044。

### 5.7 Hybrid + 兄弟 chunk 重构 + 索引重建

针对 q001/q010/q044 的失败分析：

- q001：概念页 dense 没有召回；
- q010：答案跨 chunk，且 Python/JS 双版本互相挤占；
- q044：原始 Markdown 重复段落，答案跨 H2。

引入：

```text
BM25 weight = 0.3
dense weight = 0.7
candidate_k = 50
coarse_k = 20
final_k = 5
```

流程：

```text
dense top50 + BM25 top50
→ 加权融合
→ 粗排 top20
→ 按 parent_id 合并兄弟 chunk
→ 最终精排池 = 原始命中 chunk + 合并父块
→ rerank
→ 按 URL 去重，返回 top5
```

Router v2 结果：

| 指标 | Router v1 | Router v2 | Δ |
|---|---:|---:|---:|
| Hit@1 | 0.7544 | 0.7544 | 0.0000 |
| Hit@3 | 0.9123 | **0.9298** | +0.0175 |
| Hit@5 | 0.9474 | **0.9649** | +0.0175 |
| MRR@5 | 0.8363 | **0.8450** | +0.0088 |
| nDCG@5 | 0.8645 | **0.8756** | +0.0111 |

按路由：

| 路由 | n | v1 Hit@5 | v2 Hit@5 | v1 MRR@5 | v2 MRR@5 |
|---|---:|---:|---:|---:|---:|
| self_query | 19 | 1.0000 | 1.0000 | 0.9737 | 0.9737 |
| default | 38 | 0.9211 | **0.9474** | 0.7675 | **0.7807** |

案例变化：

- 修复 q044；
- q019 保持 rank 1（最终池保留原始 chunk，避免兄弟合并稀释）；
- 无新增失败；
- q001/q010 仍然失败。

### 5.8 生成节点评测与语言一致性

新增 `tests/test_AnswerGeneration.py`，覆盖 7 个维度：

```text
correctness
faithfulness
completeness
citation_accuracy
refusal_correct
language_consistency
conciseness
```

两种 oracle context：

- `gold_answer`：参考答案作为 context；
- `gold_docs`：参考答案对应完整文档作为 context。

结果：

| 模式 | correctness | faithfulness | completeness | citation | refusal | language | conciseness |
|---|---:|---:|---:|---:|---:|---:|---:|
| gold_answer | 1.0000 | 1.0000 | 0.9758 | N/A | 1.0000 | 1.0000 | 0.9919 |
| gold_docs | 1.0000 | 1.0000 | 0.9919 | 1.0000 | 1.0000 | 0.9839 | 1.0000 |

发现：

- q052 英文问题被回答成中文；
- q034 缺少子 run 的 `trace_id` 可选说明；
- q028/q035/q061 第一版 gold_docs 只取 top 4 父块，答案段落被截断，导致误拒答；改为完整页面 context 后恢复。

语言一致性修复：

- system prompt 增加最高优先级语言规则；
- human prompt 注入确定性的 `answer_language`；
- 增加 `detect_answer_language()` / `language_matches()`；
- 不匹配时使用 `LANGUAGE_RETRY_PROMPT` 校正一次；
- 代码/API/参数/命令/URL 不翻译。

### 5.9 文档结构图与最终端到端流程

为减少「页面已命中，但 top5 context 缺少答案细节」的问题，新增结构图：

```text
Page → Section → Chunk
Chunk → NEXT_CHUNK
Section → NEXT_SECTION
Page → SAME_TOPIC_AS（Python/JavaScript 双版本）
```

图规模：

```text
nodes = 58,675
edges = 98,114
pages = 1,733
sections = 14,376
chunks = 42,650
same_topic_links = 215
```

图只做 **context 扩展**，不改变检索排序：

```text
hybrid top5
→ 图扩展同页 section / Python-JS 对应 section
→ context rerank top8
→ LLM
```

最终 62 条端到端结果：

| 指标 | 无图基线 | 图增强 | Δ |
|---|---:|---:|---:|
| Retrieval Hit@5 | 0.9649 | 0.9649 | +0.0000 |
| Retrieval MRR@5 | 0.8450 | 0.8450 | +0.0000 |
| correctness | 0.7097 | **0.9758** | +0.2661 |
| faithfulness | 1.0000 | 1.0000 | +0.0000 |
| completeness | 0.6452 | **0.9516** | +0.3065 |
| citation_accuracy | 0.9211 | **1.0000** | +0.0789 |
| refusal_accuracy | 0.8871 | **0.9839** | +0.0968 |
| language_consistency | 1.0000 | 1.0000 | +0.0000 |
| conciseness | 0.9597 | **1.0000** | +0.0403 |

图增强后 correctness/completeness 无下降案例；q003/q018/q026/q035/q040/q043 等从 0/0 恢复；q041 仍失败。

---

## 6. 最终结果汇总

### 6.1 检索（57 条可回答样本）

| k | Hit@k | Recall@k | MRR@k | nDCG@k |
|---:|---:|---:|---:|---:|
| 1 | 0.7544 | 0.7544 | 0.7544 | 0.7544 |
| 3 | 0.9298 | 0.9298 | 0.8363 | 0.8605 |
| 5 | **0.9649** | **0.9649** | **0.8450** | **0.8756** |

### 6.2 路由与 Filter

```text
route_accuracy = 1.0000
default = 43
self_query = 19
expected_filter_cases = 15
exact_match = 15
unexpected_filter_cases = 4（q023/q025/q042/q043）
invalid_or_failed = 0
```

### 6.3 生成（62 条，含无答案样本）

| 指标 | 值 |
|---|---:|
| correctness | 0.9758 |
| faithfulness | 1.0000 |
| completeness | 0.9516 |
| citation_accuracy | 1.0000 |
| refusal_accuracy | 0.9839 |
| language_consistency | 1.0000 |
| conciseness | 1.0000 |

分组：

| 路由 | n | Hit@5 | correctness | completeness |
|---|---:|---:|---:|---:|
| default | 43 | 0.9474 | 0.9651 | 0.9302 |
| self_query | 19 | 1.0000 | 1.0000 | 1.0000 |

---

## 7. 失败分析

当前端到端失败：

- **q001**：目标 overview 没有进入检索 top5；生成回答部分正确，completeness=1。
- **q010**：Python 目标页没有进入 top5，top 1 是 JavaScript 同页；生成回答已经正确，严格 URL 评测仍失败。
- **q041**：run 生命周期页面没有被召回，图扩展无法从错误页面生成答案，correctness=0、completeness=0。

部分通过：

- **q028**：rank 4，部分步骤缺失，correctness=1、completeness=1。
- **q033**：页面命中，但步骤不完整，completeness=1。

主要结论：

1. **faithfulness=1.0**：模型没有编造，失败主要是 context 不完整；
2. **图扩展显著改善「页面命中但 context 缺细节」**；
3. **q001/q010 是页面级召回问题**，需要更强的多语言 embedding、query expansion 或实体图；
4. **q041 是页面级召回失败**，结构图无法从错误页面扩展出 run 生命周期；
5. Python/JavaScript 双版本和单 URL 标注会放大失败率。

---

## 8. 决策记录

| 观察 | 决策 |
|---|---|
| 初始基线 top-1 0.4211，失败 11/57 | 引入 Cross-Encoder rerank |
| base-rerank 新增失败、Hit@10 下降 | 改用 `bge-reranker-v2-m3` |
| candidate_k=50 无收益 | 普通向量检索保留 candidate_k=30 |
| changelog/release 挤占 top5 | 增加 doc_type 惩罚（changelog 0.05，release 0.03） |
| Self-query metadata_filter Hit@5=1.0 | 保留 Self-query 能力 |
| 全量 Self-query q032/q034/q035/q043 误过滤 | 增加规则查询路由 + allowed_fields |
| Router v1 修复 q026/q057，仍失败 q001/q010/q044 | 引入 BM25 + dense、兄弟 chunk 合并 |
| q044 原始 Markdown 重复、答案跨 H2 | 索引去重 + parent/sibling metadata |
| q019 被合并父块稀释 | 最终精排池保留原始 chunk + 合并父块 |
| q052 英文问题中文回答 | 强化语言 prompt + 确定性语言重试 |
| 页面命中但 context 缺细节 | 增加 Page/Section/Chunk 结构图 context 扩展 |
| 图增强 q041 仍失败 | 下一步做实体图/页面级召回优化 |

---

## 9. 当前限制与下一步

当前已完成：

- 页面级检索评测（Hit@k / MRR / nDCG）
- Self-query 全量评测和 filter 质量评测
- 规则路由评测和 Router v1 / v2 检索评测
- 生成质量 7 维评测（oracle context）
- RAGChain 端到端完整流程评测
- 索引重建、去重、BM25/catalog 缓存和结构图扩展

仍需注意：

- 路由准确率 1.0 是 62 条规则覆盖验证，不代表未知问法泛化；
- q001 仍是 dense 召回失败；
- q010 的 top 1 是 JavaScript 同页，严格 URL 评测仍失败；
- q041 是 run 生命周期页面未召回；
- 57 条可回答样本较小，指标差异需谨慎看待；
- 结构图是原型（NetworkX），生产可迁移到 Neo4j / Kùzu。

下一步优先级：

1. 改善 q001/q010 的页面级召回：多语言 embedding、query expansion、实体图；
2. 解决 q041 的页面级召回；
3. 平台归一化和语义等价评测，减少 q010 类误判；
4. 扩展路由边界问法和真实用户问法；
5. 将结构图持久化为图数据库，并评估图遍历延迟。

---

## 10. 复现

```powershell
# 1. 建立索引和 BM25/catalog cache
uv run my-rag
# 或
python scripts/build_index.py
# 或重建带 parent metadata 的索引
python scripts/rebuild_index_v2.py

# 2. 基础检索 / rerank 评测
python tests/test_retriever.py --report tests/evaluation/test_retrieval/retrieval_report.json
python tests/test_retriever.py --rerank --candidate-k 30 --report tests/evaluation/test_retrieval/retrieval_report_rerank_v2m3_penalty.json

# 3. Self-query 评测
python tests/test_SelfQuery.py

# 4. Router 评测
python src/my_rag/core/router.py
python tests/test_RouterQuery.py
python tests/test_RouterQuery_v2.py

# 5. 生成质量评测
python tests/test_AnswerGeneration.py --workers 4 --timeout 180 --restart

# 6. 端到端完整流程评测
python tests/test_FinalPipeline.py --workers 2 --timeout 180 --restart
```

环境说明：

- Python 3.12
- `uv` 管理依赖
- 需要 NVIDIA GPU（embedding/reranker 默认使用 CUDA）
- DeepSeek API Key 放在 `.env`
- Hugging Face 不可达时可设置 `HF_HUB_OFFLINE=1` / `TRANSFORMERS_OFFLINE=1`
- 索引和缓存不提交 Git

---

## 11. 报告与产物索引

主要报告：

```text
tests/evaluation/test_retrieval/
  baseline_retrieval_v1.json / .md
  retrieval_report_rerank_v2m3_penalty.json
  rerank_comparison_v1.md
  chinese_rerank_comparison_v2m3.md
  doctype_penalty_comparison.md
  candidate_k_comparison_30_vs_50.md

tests/evaluation/test_SelfQuery/
  translate_outcome.json
  translate_report.md
  test_RouterQuery.json / .md
  router_failure_analysis.md

tests/evaluation/test_router/
  router_report.json / .md
  router_v2_report.json / .md

tests/evaluation/test_generation/
  generation_report.json / .md

tests/evaluation/final_test/
  final_pipeline_report.json / .md
  final_pipeline_report_baseline_no_graph.json / .md

router-optimization.md
```

参考文档：

- `技术文档.txt`：早期实验笔记与问题记录
- `代码架构.txt`：当前代码结构
- `tests/evaluation/title_catalog.json`：全部 title 元数据目录

---

## 12. 依赖与模型

- `langchain-core` / `langchain-classic` / `langchain-chroma`
- `chromadb`
- `sentence-transformers`
- `torch`（CUDA）
- `langchain-deepseek`
- `networkx`
- `scikit-learn`（BM25 矩阵）
- `IEITYuan/Yuan-embedding-2.0-en`
- `BAAI/bge-reranker-v2-m3`
- `deepseek-chat`
