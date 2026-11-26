# Rerank 新增失败案例分析

- 日期：2026-11-24
- 对比对象：`baseline_retrieval_v1.json` vs `retrieval_report_rerank.json`
- 新增失败案例：q010、q028、q030、q041、q056
- 说明：这里的“失败”定义为 `rank > 5` 或 `rank is None`

## 总览

| ID | 类型 | 语言 | 基线 rank | rerank rank | 预期页面 | 主要失败原因 |
|---|---|---|---:|---|---|---|
| q010 | conceptual | zh | 2 | 未命中 | python/langchain/multi-agent | 子页面/近邻页面抢占；中文 query + 英文 reranker |
| q028 | how_to | zh | 2 | 6 | langsmith/evaluation-quickstart | 多个评估/数据集页面内容高度重叠；changelog 噪声 |
| q030 | how_to | zh | 2 | 未命中 | langsmith/evaluate-rag-tutorial | “测试数据集”被 pytest/vitest 页面抢占；目标 chunk 召回不足 |
| q041 | conceptual | zh | 2 | 未命中 | langsmith/agent-server | 目标页的关键 chunk 未进入候选；`lifecycle` 词面命中错误页面 |
| q056 | metadata_filter | en | 5 | 未命中 | langsmith/manage-datasets-in-application | 纯检索忽略 URL 约束；UI 页面被 programmatic 页面压制 |

共性：5 条中有 4 条是中文 query；5 条在基线中都至少有 1 个目标页面 chunk 进入候选池，rerank 阶段发生了明显的降权或错误排序。

## q010

**问题**：LangChain 多智能体系统中的 Subagents 模式是如何工作的？为什么它在重复请求时模型调用次数不会减少？

**预期**：`https://docs.langchain.com/oss/python/langchain/multi-agent`

**基线 rank 2 +5**：

1. `oss/javascript/langchain/multi-agent`
2. **`oss/python/langchain/multi-agent`**
3. `oss/python/langgraph/use-subgraphs`
4. `oss/javascript/langgraph/use-subgraphs`
5. `oss/python/langchain/multi-agent/subagents`

**rerank top5**：

1. `oss/javascript/deepagents/async-subagents`（Async subagents）
2. `oss/javascript/langgraph/use-subgraphs`（Subgraphs）
3. `oss/python/langgraph/use-subgraphs`（Subgraphs）
4. `oss/javascript/langchain/multi-agent/handoffs-customer-support`
5. `oss/python/langgraph/use-subgraphs`（Subgraphs）

**目标页面在候选池中的 chunk**：

- 候选位置 2，标题 Multi-agent，章节 `Performance comparison / Summary`
- 内容是 Subagents/Handoffs/Router 的对比表，包含“Subagents 4 次调用”等信息；目标页真正解释该模式的 chunk 未必进入了 top 30

**失败原因**：

1. reranker 强烈偏好标题/内容中直接出现 `subagents` 的页面，`async-subagents`、`subgraphs` 被排到前面
2. 中文 query 对英文 cross-encoder 不友好，模型没有充分理解“重复请求时模型调用次数不会减少”这一因果关系
3. 目标页只有“性能对比/Summary”chunk 进入候选，缺少更直接的“Subagents pattern”chunk；属于 chunk 级召回不足
4. 另一个子图页面也包含 “Subagent message count: 4” 的内容，说明当前标注可能不是唯一可回答页面，存在多答案标注问题

## q028

**问题**：如何在 LangSmith 的 Playground 中创建一个用于评估的数据集并运行正确性评估？

**预期**：`https://docs.langchain.com/langsmith/evaluation-quickstart`

**基线 rank 2 +5**：

1. `langsmith/changelog`
2. **`langsmith/evaluation-quickstart`**
3. `langsmith/run-evaluation-from-playground`
4. `langsmith/code-evaluator-ui`
5. `langsmith/create-a-prompt`

**rerank top5**：

1. `langsmith/changelog`
2. `langsmith/code-evaluator-ui`
3. `langsmith/bind-evaluator-to-dataset`
4. `langsmith/manage-datasets-in-application`
5. `langsmith/llm-as-judge`

**目标页面在候选池中的 chunk**：

- 候选位置 2：`Next steps`
- 候选位置 3：`5. Define an evaluator`
- 候选位置 11：`3. Create a dataset`
- 目标页确实有创建数据集和定义 evaluator 的内容，但最匹配的 chunk 并非排名最高

**失败原因**：

1. 查询中的 `Playground`、`dataset`、`evaluator`、`correctness` 在多个 LangSmith 页面重复出现，属于近邻页面密集竞争
2. reranker 选择了“标题直接包含 evaluator/dataset”的页面，而不是包含完整操作流程的 quickstart
3. changelog 页面包含 Playground Evaluate、evaluator、dataset 等关键词，被误排到第一；长文档/变更日志更容易积累词面匹配
4. `run-evaluation-from-playground` 是更直接的产品页面，但 rerank 后排到第 10，说明当前 reranker 对产品流程语义理解不足
5. 标注可能存在多答案：`run-evaluation-from-playground` 和 `manage-datasets-in-application` 也部分回答该问题

## q030

**问题**：如何用 LangSmith 创建一个包含示例问答的测试数据集来评估 RAG 应用？

**预期**：`https://docs.langchain.com/langsmith/evaluate-rag-tutorial`

**基线 rank 2 +5**：

1. `oss/javascript/deepagents/rag`
2. **`langsmith/evaluate-rag-tutorial`**
3. `langsmith/evaluate-on-intermediate-steps`
4. `oss/javascript/langgraph/agentic-rag`
5. `oss/python/langgraph/agentic-rag`

**rerank top5**：

1. `langsmith/pytest`
2. `langsmith/changelog`
3. `langsmith/evaluate-chatbot-tutorial`
4. `langsmith/evaluation-quickstart`
5. `langsmith/vitest-jest`

**目标页面在候选池中的 chunk**：

- 候选位置 2：页面介绍（RAG 定义）
- 候选位置 13：`Run the evaluation`
- “创建测试数据集”的具体操作 chunk 没有进入 top 30，目标页只有介绍段和评估段

**失败原因**：

1. “测试数据集”被 reranker 理解为软件测试，`pytest`、`vitest-jest` 排到前面，属于词义歧义
2. 目标 RAG tutorial 的 dataset 创建 chunk 没有进入候选，reranker 只能看到介绍页，无法正确排序
3. changelog 再次因为关键词覆盖被排到第二
4. `evaluate-chatbot-tutorial` 与 RAG tutorial 结构相似，近邻页面竞争
5. 中文 query 对英文 reranker 的语义匹配有损失

## q041

**问题**：LangSmith Agent Server 的运行（run）执行生命周期是怎样的？

**预期**：`https://docs.langchain.com/langsmith/agent-server`

**基线 rank 2 +5**：

1. `langsmith/deployment`
2. **`langsmith/agent-server`**
3. `langsmith/runs`
4. `langsmith/coding-agent-metadata-contract`
5. `oss/javascript/langgraph/application-structure`

**rerank top5**：

1. `langsmith/data-storage-and-privacy`
2. `oss/javascript/deepagents/async-subagents`（Understand the lifecycle）
3. `oss/python/deepagents/async-subagents`（Understand the lifecycle）
4. `oss/javascript/langgraph/application-structure`
5. `oss/python/langgraph/application-structure`

**目标页面在候选池中的 chunk**：

- 候选位置 2：Agent Server 介绍（runtime、assistants 等）
- 候选位置 13：`LangSmith Deployment is now LangSmith Agent Server`
- 真正讲 run 生命周期/队列/worker 的 chunk 没有进入候选

**失败原因**：

1. reranker 对 `lifecycle` 的词面匹配过强，`async-subagents` 的 `Understand the lifecycle` 直接抢到前面
2. 目标页进入候选的是通用介绍 chunk，不是生命周期 chunk；chunk 召回不足导致 rerank 无法补救
3. 中文 query 对英文 cross-encoder 的语义理解不足
4. `agent-server` 页面较长，关键内容被切成多个 chunk，当前 30 个候选没有覆盖到关键段落
5. `data-storage-and-privacy` 提到 durable execution 和 checkpoints，虽然不是生命周期主页面，但词面更接近

## q056

**问题**：According to the page at https://docs.langchain.com/langsmith/manage-datasets-in-application, how do I add metadata to an example in a dataset?

**预期**：`https://docs.langchain.com/langsmith/manage-datasets-in-application`

**基线 rank 5 +5**：

1. `langsmith/manage-datasets-programmatically`
2. `langsmith/evaluate-llm-application`
3. `langsmith/data-purging-compliance`
4. `langsmith/evaluation-quickstart`
5. **`langsmith/manage-datasets-in-application`**

**rerank top5**：

1. `langsmith/manage-datasets-programmatically`
2. `langsmith/changelog`
3. `langsmith/evaluate-with-attachments`
4. `langsmith/evaluate-llm-application`（Add metadata to an experiment）
5. `langsmith/manage-datasets`

**目标页面在候选池中的 chunk**：

- 候选位置 6：Add synthetic examples created by an LLM
- 候选位置 10：Filter examples
- 候选位置 11：Create a dataset schema
- 候选位置 12：页面介绍
- 候选位置 24：synthetic examples（另一段）
- “如何给 example 添加 metadata”的操作 chunk 没有进入 top 30

**失败原因**：

1. 这是 metadata_filter 题，query 里明确给了 URL，但纯向量检索完全忽略 URL，rerank 也无法利用该约束
2. `manage-datasets-programmatically` 的代码示例直接包含 `metadata`，对 cross-encoder 更有吸引力
3. 目标 UI 页面的候选 chunk 主要是 schema、过滤、synthetic examples，缺少最直接的 metadata 操作段
4. `evaluate-llm-application` 的 `Add metadata to an experiment` 与 query 词面高度相似，但不是 example metadata
5. 该案例应交给 Self-query 的 `url` 过滤，而不是纯检索 + rerank

## 共性原因

1. **中文 query + 英文 reranker**：5 条新失败中 4 条是中文；`bge-reranker-base` 的跨语言能力不足，中文语义没有充分对齐英文文档
2. **近邻页面竞争**：subagents/async-subagents/use-subgraphs、evaluation quickstart/tutorial/chatbot、datasets UI/programmatic，标题和内容高度相似
3. **chunk 级召回不足**：q010、q030、q041、q056 的目标页面虽然进入候选池，但真正包含答案的 chunk 没有进入 top 30；rerank 无法对未出现的 chunk 排序
4. **关键词陷阱**：`lifecycle` 命中 async-subagents，`测试数据集` 命中 pytest/vitest，`metadata` 命中 programmatic 代码页
5. **changelog/长页面噪声**：q028、q030、q056 的 changelog 或长页面因关键词密度高被排到前面
6. **元数据约束未利用**：q056 明确指定 URL，但纯检索无法执行 URL filter

## 建议

1. 先测试 `BAAI/bge-reranker-v2-m3`，重点看 4 条中文失败案例
2. 将 `candidate_k` 从 30 提到 50，确认 q010/q030/q041/q056 的关键 chunk 是否进入候选
3. 对 chunk 级召回做诊断：把目标页面的关键 chunk 按标题和内容单独检索，确认是切分问题还是 top-k 问题
4. 增加 `doc_type`/`section` 元数据，对 changelog、release、API reference 降权
5. 对 q056 这类问题使用 Self-query 的 URL/title 过滤；纯检索基线不应承担这类评价
6. 复核 q010、q028 的多答案标注：`use-subgraphs`、`run-evaluation-from-playground` 等页面也可能部分回答问题，单一 `relevant_urls` 可能过于严格
