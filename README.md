# My RAG：LangChain 文档智能问答

基于 LangChain 官方文档的 RAG 问答系统。项目当前包含文档加载、Markdown 标题切分、Chroma 向量库、Self-query 元数据检索、Cross-Encoder 重排、DeepSeek 问答和分层检索评测。

本次分支 `retrieval-optimization` 相对 GitHub `main` 的改动，主要是检索优化、元数据扩展和评测报告；Self-query 评测脚本已实现，查询路由和回答质量评测仍待后续完成。

## 1. 项目结构

```text
src/my_rag/
├── config.py                 # 路径和项目根目录
├── cli.py                    # 建库入口
├── pipeline.py               # 加载 -> 切分 -> 嵌入 -> Chroma
├── ingestion/
│   ├── loader.py             # 文档加载、frontmatter、doc_type/platform
│   └── splitter.py           # 标题切分 + 递归切分
├── model/
│   ├── embedding.py          # Yuan-embedding-2.0-en
│   ├── llm.py                # DeepSeek
│   └── reranker.py           # Cross-Encoder 重排 + doc_type 惩罚
├── core/
│   ├── vector_store.py       # Chroma 建库/加载
│   ├── retriever.py          # 普通检索、Self-query、重排
│   └── rag_chain.py          # Prompt + 上下文 + LLM
scripts/
├── build_index.py
└── chat.py
tests/
├── test_retriever.py         # 纯向量/rerank 检索评测
├── test_SelfQuery.py         # Self-query 改写、filter、检索评测
└── evaluation/               # 评测集和实验报告
```

## 2. 当前数据与索引

- Markdown 文档：1,733 篇
- 切分后 chunk：43,245 个
- chunk 大小：最大 512 字符，overlap 50
- 向量模型：`IEITYuan/Yuan-embedding-2.0-en`，1024 维
- 向量库：Chroma，collection `langchain_docs`
- 生成模型：DeepSeek `deepseek-chat`
- 重排模型：`BAAI/bge-reranker-v2-m3`
- 索引路径：`data/vector_store/`（不提交到 Git）

每个 chunk 除 `source` 外，还带有：

- `title`
- `url`
- `scraped_at`
- `word_count`
- `doc_type`
- `platform`
- `h1` / `h2` / `h3`（存在标题时才写入）

## 3. 本分支相对 main 的改动

| 改动 | 涉及文件 | 状态 |
|---|---|---|
| 增加 Cross-Encoder 重排 | `model/reranker.py`、`core/retriever.py`、`core/rag_chain.py` | 已采纳 |
| 默认重排模型改为多语言 `bge-reranker-v2-m3` | `model/reranker.py`、`.env.example` | 已采纳 |
| 增加 `doc_type` 元数据 | `ingestion/loader.py` | 已采纳 |
| 增加 `platform` 元数据 | `ingestion/loader.py` | 已采纳 |
| 增加 changelog/release 分数惩罚 | `model/reranker.py` | 已采纳 |
| 评测脚本支持 rerank、candidate_k 和惩罚开关 | `tests/test_retriever.py` | 已采纳 |
| 增加检索实验报告和失败分析 | `tests/evaluation/` | 已记录 |
| 增加 `langchain-classic`、`sentence-transformers` 依赖 | `pyproject.toml`、`uv.lock` | 已采纳 |

### 3.1 重排逻辑

流程：

```text
query
→ 向量检索 candidate_k=30
→ CrossEncoder 对 30 个 (query, document) 打分
→ 根据分数和 doc_type 惩罚排序
→ 取 top_n
```

生产链路：

- `candidate_k=30`
- `top_n=4`（最终交给 LLM 的文档数）
- 默认启用重排
- 可通过 `build_rag_chain(use_rerank=False)` 关闭

评测链路：

- 使用 top-10 重排结果计算 `@1/@3/@4/@5/@10`
- 因此评测 `@1–@5` 与生产 top_n=4/5 的重排顺序一致

### 3.2 doc_type 派生规则

`doc_type` 在 `loader.py` 中基于 URL 和 title 派生，优先级：

1. frontmatter 已有 `doc_type` 时直接使用
2. URL path
3. title
4. 默认 `guide`

规则：

| doc_type | 规则 |
|---|---|
| `changelog` | URL basename 或 title 包含 `changelog` |
| `release` | URL 位于 `/releases/`，且不是 changelog |
| `policy` | URL 包含 `release-policy` 或 `release-stages` |
| `api_reference` | URL 以 `/langsmith/smith-api/`、`/langsmith/agent-server-api/` 或 `/api-reference/` 开头 |
| `troubleshooting` | URL/title 包含 troubleshoot、diagnostics、common-issues、faq |
| `quickstart` | URL/title 包含 quickstart |
| `tutorial` | URL/title 包含 tutorial |
| `concept` | URL/title 包含 concepts、overview、architecture、philosophy、introduction、fundamentals |
| `guide` | 其余普通操作文档 |

当前语料分布：

```text
guide          898
api_reference  720
concept         68
quickstart      15
troubleshooting 14
changelog        6
tutorial         5
release          4
policy           3
```

采用原因：这些文档的标题和 h1/h2 很多是通用结构词（`Overview`、`Setup`、`Next steps`），不适合作为稳定过滤条件；URL 和 doc_type 更可靠。changelog/release 文档虽只有 10 篇，但产生了 3,329 个 chunk，占全库 7.7%，容易在长文档和关键词密度上挤占检索结果。

### 3.3 platform 派生规则

`platform` 用于区分 Python、JavaScript 和与语言无关的文档：

| platform | 规则 |
|---|---|
| `python` | URL path 中出现独立 `python` 段，或以 `python-` 开头 / `-python` 结尾；标题包含 `(Python only)`、`Python extensions` |
| `javascript` | URL path 中出现独立 `javascript` 段，或以 `javascript-` 开头 / `-javascript` 结尾；标题包含 `(JavaScript only)`、`(JS only)` |
| `agnostic` | 同时覆盖 Python 和 JS/TS 的页面、LangSmith 通用页、API reference 等 |

当前分布：

```text
文档：python 229 / javascript 233 / agnostic 1271
chunk：python 10695 / javascript 9569 / agnostic 22981
```

边界验证：

- `oss/python/langchain/quickstart` → `python`
- `oss/javascript/langchain/quickstart` → `javascript`
- `langsmith/setup-javascript` → `javascript`
- `langsmith/trace-with-langchain` → `agnostic`

`platform` 目前只作为新增 metadata 和 Self-query 可过滤字段，尚未做默认过滤，也未单独评测其检索收益。

### 3.4 doc_type 惩罚

`DocTypePenalizedReranker` 在 cross-encoder 原始分数上执行加法惩罚：

```python
penalties = {"changelog": 0.05, "release": 0.03}
final_score = rerank_score - penalty
```

默认启用，可用 `--no-doc-type-penalty` 关闭。当前没有查询意图分类，因此不会判断问题是否真正与 release/changelog 相关。

## 4. 评测方法

评测集：`tests/evaluation/qa_set.jsonl`

评测口径参考 `技术文档.txt` 的“检索评测”部分，并结合当前评测集的实际字段执行。

- 总 62 条
- 57 条可回答，5 条不可回答
- 语言：中文 41 条、英文 21 条；可回答部分为中文 36 条、英文 21 条
- 类型：how_to 19、conceptual 11、factual 7、configuration 3、metadata_filter 15、troubleshooting 2、unanswerable 5
- 15 条 metadata_filter：7 条 url 过滤、8 条 title 过滤
- `must_keep_terms`：改写 query 时必须保留的核心术语/实体/约束
- `rewrite_required`：是否预期需要 query 改写/翻译；当前 47 条为 true，15 条为 false（10 条简单英文问题 + 5 条不可回答问题）

当前 `tests/test_retriever.py` 不读取 `must_keep_terms` 和 `rewrite_required`，它们用于后续 Self-query 改写质量评测。

检索评测只使用 57 条可回答问题，按页面 URL 去重，计算：

- **Hit@k**：top-k 至少命中一个相关页面的问题比例
- **Recall@k**：命中相关 URL 数 / 标注相关 URL 总数，再平均
- **MRR@k**：第一个相关页面的排名倒数平均值
- **nDCG@k**：按排名折损的归一化相关性分数

当前评测是页面级、二值相关性；每条问题只有一个 `relevant_urls`，因此 `Recall@k` 与 `Hit@k` 数值相同。评测不包含回答质量、faithfulness、Self-query 和路由。

## 5. 实验结果

### 5.1 Reranker 对比

| k | 基线 Hit | base-rerank Hit | v2-m3 Hit | 基线 MRR | base-rerank MRR | v2-m3 MRR | 基线 nDCG | base-rerank nDCG | v2-m3 nDCG |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.4211 | 0.5263 | **0.6667** | 0.4211 | 0.5263 | **0.6667** | 0.4211 | 0.5263 | **0.6667** |
| 3 | 0.7018 | 0.8070 | **0.8421** | 0.5556 | 0.6608 | **0.7515** | 0.5936 | 0.6988 | **0.7751** |
| 5 | 0.8070 | 0.8246 | **0.9123** | 0.5792 | 0.6652 | **0.7673** | 0.6366 | 0.7064 | **0.8037** |
| 10 | 0.9123 | 0.8596 | **0.9474** | 0.5942 | 0.6711 | **0.7714** | 0.6716 | 0.7189 | **0.8146** |

@5 失败数：

```text
基线 11 / 57
base-rerank 10 / 57
v2-m3 5 / 57
```

中文 36 条：

| 指标 | 基线 | base-rerank | v2-m3 |
|---|---:|---:|---:|
| Hit@1 | 0.4167 | 0.5000 | **0.6389** |
| Hit@5 | 0.7778 | 0.7778 | **0.8611** |
| MRR@5 | 0.5690 | 0.6227 | **0.7347** |
| nDCG@5 | 0.6217 | 0.6624 | **0.7668** |

结论：

- `bge-reranker-base` 明显提升 top-1/MRR，但 Hit@10 下降，且出现 5 条新失败
- `bge-reranker-v2-m3` 同时改善 top-1、top-10 和中文指标，失败数从 10 降到 5
- 采用 `v2-m3` 作为默认 reranker；base 不采用

base-rerank 修复的基线失败：q004、q005、q016、q020、q038、q061；新增失败：q010、q028、q030、q041、q056。

v2-m3 相对 base-rerank 修复：q028、q030、q041；剩余失败：q001、q010、q026、q044、q057。

### 5.2 candidate_k 30 vs 50

| 配置 | Hit@1 | Hit@5 | Hit@10 | MRR@5 | nDCG@5 | @5 失败 |
|---|---:|---:|---:|---:|---:|---:|
| base + 30 | 0.5263 | 0.8246 | 0.8596 | 0.6652 | 0.7064 | 10 |
| base + 50 | 0.5263 | 0.8421 | 0.9298 | 0.6702 | 0.7144 | 9 |
| v2-m3 + 30 | **0.6667** | **0.9123** | 0.9474 | 0.7673 | **0.8037** | **5** |
| v2-m3 + 50 | **0.6667** | 0.8947 | 0.9474 | 0.7681 | 0.8005 | 6 |

中文结果：

| 配置 | Hit@1 | Hit@5 | MRR@5 | nDCG@5 |
|---|---:|---:|---:|---:|
| v2-m3 + 30 | **0.6389** | **0.8611** | **0.7347** | **0.7668** |
| v2-m3 + 50 | 0.6111 | **0.8611** | 0.7278 | 0.7621 |

结论：`candidate_k=50` 对 v2-m3 没有收益，反而使 Hit@5、中文 Hit@1、MRR、nDCG 略降，q010 还从第 9 掉出 top-10。**不采纳 50，保留 30**。base 在 50 下略有改善，但仍远低于 v2-m3。

### 5.3 doc_type 惩罚对比

无惩罚 vs 惩罚（v2-m3 + candidate 30）：

| 指标 | 无惩罚 | 有惩罚 |
|---|---:|---:|
| Hit@1 | 0.6667 | **0.6842** |
| Hit@5 | 0.9123 | 0.9123 |
| MRR@5 | 0.7673 | **0.7769** |
| nDCG@5 | 0.8037 | **0.8110** |
| @5 失败数 | 5 | 5 |
| top-5 changelog 次数 | 7 | **3** |
| top-5 release 次数 | 5 | **4** |
| 含 changelog/release 问题数 | 8 | **4** |

案例：q028 从 rank 5 升到 4，changelog 被挤出 top-5；q022 从 2 升到 1。q001 的 top-5 仍有 3 个 release 页面，未被完全解决。

结论：惩罚项**部分解决挤占**，changelog 改善明显，release 改善有限；Hit@5 不变，但 top-1/MRR/nDCG 小幅提升。采用为默认策略，但保留后续查询意图分类/关闭惩罚的开关。

### 5.4 Self-query 评测

新增 `tests/test_SelfQuery.py`，评测内容：

- `structured_query.query` 的 `must_keep_terms` 覆盖率
- `expected_filter` 与生成 filter 的 exact/field/value/operator 匹配
- Self-query 检索的 Hit@k、Recall@k、MRR@k、nDCG@k
- 可按 `--ids` 指定样例，支持 `--no-rerank` 和 `--no-doc-type-penalty`

smoke test（q026/q057）：

```text
filter exact match: 2/2
q026 rank=1, q057 rank=2
must_keep coverage 平均: 0.5
```

覆盖率偏低的主要原因是 Self-query 保留了中文检索表达，而 `must_keep_terms` 主要记录英文规范术语；这说明后续需要评估查询改写/翻译，而不是只看 filter 命中。全量 57 条尚未运行，完整报告默认写入 `tests/evaluation/self_query_report.json`。

## 6. 剩余失败案例

当前 v2-m3 + 惩罚项仍失败 5 条，其中 4 条为中文：

- **q001**：概念/概览问题，release/runtime 页面挤占，目标 overview 未命中
- **q010**：中文跨语言 + Python/JS 双版本 + chunk 召回不足；英文重写后可到 rank 4
- **q026**：title 元数据过滤题，目标页未进入 top-30，需要 Self-query
- **q044**：中文跨语言 + 概览页排序靠后，Managed Deep Agents 页面可能也是有效答案
- **q057**：title 元数据过滤题，目标页 rank 8，需要 Self-query

详细分析见：

- `tests/evaluation/rerank_failure_analysis.md`
- `tests/evaluation/doctype_penalty_comparison.md`
- `tests/evaluation/candidate_k_comparison_30_vs_50.md`
- `tests/evaluation/chinese_rerank_comparison_v2m3.md`

## 7. 决策记录

| 改动 | 结果 | 决策 |
|---|---|---|
| 引入 rerank | Hit@1 +10.53，MRR/nDCG 提升 | 采纳 |
| 使用 base reranker | top-1 提升，但 Hit@10 下降、新失败增加 | 不作为默认 |
| 改用 v2-m3 | 中文和整体显著提升，失败 10→5 | 采纳为默认 |
| candidate_k=50 | 无收益，中文略降，失败 5→6 | 不采纳 |
| doc_type 惩罚 | changelog 挤占 7→3，MRR/nDCG 小幅提升 | 采纳，后续加意图开关 |
| doc_type/platform 元数据 | 不改召回，但支持稳定过滤 | 采纳 |
| Self-query 评测 | 脚本已实现；q026/q057 smoke test 的 filter 均 exact match，rank 分别为 1/2 | 待全量运行和分析 |
| 查询路由/意图分类 | 尚未实现 | 待做 |
| 查询翻译/重写 | 实验显示 q010/q044 有效 | 待集成 |
| chunk_role 导航片段过滤 | 尚未实现 | 待做 |
| BM25 混合检索 | 尚未实现 | 待做 |

## 8. 复现

```powershell
# 建立索引（会写入 doc_type/platform）
uv run my-rag

# 基线纯向量检索
python tests/test_retriever.py --report tests/evaluation/retrieval_report.json

# v2-m3 + rerank + 惩罚
python tests/test_retriever.py --rerank --candidate-k 30 --report tests/evaluation/retrieval_report_rerank_v2m3_penalty.json

# 关闭惩罚，复现无惩罚版本
python tests/test_retriever.py --rerank --no-doc-type-penalty --candidate-k 30 --report tests/evaluation/retrieval_report_rerank_v2m3.json

# Self-query 全量评测
python tests/test_SelfQuery.py

# Self-query 指定样例
python tests/test_SelfQuery.py --ids q026,q057
```

主要报告：

```text
tests/evaluation/baseline_retrieval_v1.json
tests/evaluation/retrieval_report_rerank.json
tests/evaluation/retrieval_report_rerank_v2m3.json
tests/evaluation/retrieval_report_rerank_v2m3_penalty.json
tests/evaluation/rerank_comparison_v1.md
tests/evaluation/chinese_rerank_comparison_v2m3.md
tests/evaluation/doctype_penalty_comparison.md
tests/evaluation/candidate_k_comparison_30_vs_50.md
```

## 9. 限制与下一步

当前评测仍是页面级检索评测：

- 没有 Self-query query/filter 准确率
- 没有路由准确率
- 没有回答正确性、faithfulness、引用准确性
- 没有 release/changelog 意图题，无法验证惩罚是否会误伤版本类问题
- 每条问题只有一个相关 URL，Python/JS 双版本容易产生标注偏差
- 57 条样本较小，指标差异需谨慎看待

下一步优先级：

1. 运行 Self-query 全量评测：filter 准确率、must_keep_term 覆盖率、过滤后检索指标
2. 增加 release/changelog 意图题和查询路由
3. 增加查询翻译/重写，改善中文跨语言检索
4. 增加 `chunk_role` 和导航片段过滤
5. 增加回答质量与端到端评测
