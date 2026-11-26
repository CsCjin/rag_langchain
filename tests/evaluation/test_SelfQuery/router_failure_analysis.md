# Router 检索失败案例分析：q001 / q010 / q044

- 日期：2026-11-26
- 分析对象：`tests/evaluation/test_SelfQuery/test_RouterQuery.json` 中 Hit@5 未命中的三条样本
- 检索配置：原始 query → 向量召回 `candidate_k=30` → `BAAI/bge-reranker-v2-m3` 重排 → 页面 URL 去重
- 诊断方法：
  1. 复现原始 query 的向量 top 100 和重排 top 30；
  2. 对目标页面所有 chunk 直接做 rerank，判断“重排是否能识别答案”；
  3. 用翻译后的 query 再跑一遍，比较召回变化；
  4. 检查目标页面的 chunk 数量、重复内容和答案分布。

> 下表中的分数均为 rerank 原始分减去 doc_type 惩罚后的调整分。

## 1. 总览

| 案例 | 目标页面最佳向量排名 | 是否进入 candidate_k=30 | 扩到 top 60 后的重排排名 | 目标页最佳答案 chunk 直接重排分 | 主要问题 |
|---|---:|---|---:|---:|---|
| q001 | 32 | 否 | 52 | 0.9925 | dense 召回漏掉概念页答案 chunk |
| q010 | 2 | 是 | 10 | 0.9282 | 答案 chunk 粒度 + JavaScript 重复页 |
| q044 | 41 | 否 | 9 | 0.9954 | 页面重复 + 答案被拆成多个 H2 + 标注粒度过严 |

三条失败并不是同一类问题：

- **q001 是明确的召回失败**：目标页的答案 chunk 重排分很高，但向量检索没有把它召回来。
- **q010 主要是 chunk 粒度和平台重复问题**：目标页被召回了，但真正回答“为什么重复请求不减少调用”的 chunk 没进候选窗口；同时 JavaScript 版本排在第一位。
- **q044 主要是 chunk 切分、页面重复和评测标注问题**：目标 hub 页的答案被拆成两个 H2，且原始 Markdown 本身有重复段落；top 5 中已经有能回答问题的专门页面。

## 2. q001：create_agent 与 LangGraph 的关系

### 2.1 实际召回结果

| 排名 | URL | 调整分 |
|---:|---|---:|
| 1 | `https://docs.langchain.com/oss/python/langchain/runtime` | 0.9958 |
| 2 | `https://docs.langchain.com/oss/javascript/langchain/runtime` | 0.9887 |
| 3 | `https://docs.langchain.com/oss/python/releases/langchain-v1` | 0.9677 |
| 4 | `https://docs.langchain.com/oss/javascript/releases/langchain-v1` | 0.9643 |
| 5 | `https://docs.langchain.com/oss/python/releases/langgraph-v1` | 0.9635 |

目标页面：`https://docs.langchain.com/oss/python/langchain/overview`

- 目标页最佳向量排名：**32**，刚好在 `candidate_k=30` 之外。
- 把候选窗口扩到 60 后，目标页只有“LangChain vs. LangGraph vs. Deep Agents”这个 chunk 进入重排，最终排名 **52**，分数只有 **0.2108**。
- 但直接对目标页全部 22 个 chunk 做重排，结果完全不同：
  - “Agent = Model + Harness. LangChain provides `create_agent`...”：**0.9925**
  - “Built on top of LangGraph”：**0.8603**

也就是说，**真正回答问题的 chunk 重排分足够高，但向量检索根本没有召回它**。如果第一个 chunk 进入候选，目标页会排到第 2 名左右。

### 2.2 翻译 query 的结果

翻译后的 query：

> What is create_agent in LangChain and how does it relate to LangGraph?

目标页在翻译 query 的向量 top 100 中**完全没有出现**。翻译没有改善 q001，反而更差。

### 2.3 结论

q001 是典型的 **dense 向量召回失败**：

- 不是 reranker 不识别答案，而是答案 chunk 没进候选集；
- `candidate_k=30` 只是表面原因，因为最佳答案 chunk 连 top 60 都没进；
- 中文 query + 英文概念页之间存在语义匹配缺口；
- 典型修复手段是 hybrid retrieval（BM25 + dense）、实体/关键词增强、multi-query，而不是继续加大 candidate_k。

## 3. q010：Subagents 模式与重复请求的模型调用

### 3.1 实际召回结果

| 排名 | URL | 调整分 |
|---:|---|---:|
| 1 | `https://docs.langchain.com/oss/javascript/langchain/multi-agent` | 0.9379 |
| 2 | `https://docs.langchain.com/oss/python/langgraph/use-subgraphs` | 0.9295 |
| 3 | `https://docs.langchain.com/oss/javascript/langgraph/use-subgraphs` | 0.9183 |
| 4 | `https://docs.langchain.com/oss/python/langchain/multi-agent/router-knowledge-base` | 0.7705 |
| 5 | `https://docs.langchain.com/oss/javascript/langchain/multi-agent/router-knowledge-base` | 0.7474 |
| ... | ... | ... |
| 10 | `https://docs.langchain.com/oss/python/langchain/multi-agent`（目标） | 0.5640 |

目标页面：`https://docs.langchain.com/oss/python/langchain/multi-agent`

- 目标页最佳 chunk 向量排名 **2**，进入候选窗口，但重排后只排 **10**。
- 真正回答“为什么重复请求不减少调用”的 “Performance comparison > Repeat request” chunk：
  - 向量排名 **48**，在 `candidate_k=30` 之外；
  - 把候选窗口扩到 60 后进入重排，但只排 **23**，分数 **0.5537**。
- 直接对目标页全部 38 个 chunk 做重排：
  - 包含 “Subagents are stateless by design” 的 Repeat request chunk：**0.9282 / 0.9051**
  - “Patterns” chunk：**0.7911**
  - “Summary” chunk：**0.7458**

所以 q010 的问题是双重的：

1. **答案 chunk 没有被向量召回**：向量 top 30 里只有 Summary，没有真正的 Repeat request 解释。
2. **进入候选的 Summary chunk 语义不够直接**：它只有表格数字，没有解释“stateless/重复完整流程”，所以重排分只有 0.564。

### 3.2 JavaScript 重复页的影响

排名第 1 的 `.../oss/javascript/langchain/multi-agent` 是目标 Python 页面的 JavaScript 版本，内容结构基本相同。如果按平台归一化（Python/JavaScript 视为同一页面），q010 的实际排名就是 **1**。

当前评测要求精确 URL，因此它被算作失败；但从用户角度看，JavaScript 页面同样能回答这个平台无关的问题。

### 3.3 翻译 query 的结果

翻译后的 query：

> How does the Subagents pattern work in LangChain multi-agent systems, and why does it not reduce the number of model calls for repeated requests?

- 目标页最佳重排排名从 10 提升到 **7**，分数 **0.7994**。
- 仍然没有进入 top 5。
- 真正的 Repeat request 答案 chunk 仍然没有被召回。

### 3.4 结论

q010 不是单纯的召回失败，而是：

- **chunk 粒度问题**：答案被拆在 “Patterns” 和 “Repeat request” 两个 chunk；
- **reranker 偏好问题**：Summary/Patterns 的泛化表述压过了具体解释；
- **平台重复问题**：JavaScript 版本排在第一位；
- **query 需要分解**：问题同时问“怎么工作”和“为什么重复请求不减少调用”，单个 chunk 很难同时覆盖。

## 4. q044：Deep Agents 与 Managed Deep Agents 的区别

### 4.1 实际召回结果

| 排名 | URL | 调整分 |
|---:|---|---:|
| 1 | `https://docs.langchain.com/oss/python/langchain/quickstart` | 0.9976 |
| 2 | `https://docs.langchain.com/oss/python/learn` | 0.9966 |
| 3 | `https://docs.langchain.com/oss/javascript/learn` | 0.9964 |
| 4 | `https://docs.langchain.com/langsmith/javascript/managed-deep-agents-overview` | 0.9949 |
| 5 | `https://docs.langchain.com/langsmith/python/managed-deep-agents-overview` | 0.9948 |

目标页面：`https://docs.langchain.com/build-overview`

- 目标页最佳 chunk 向量排名 **41**，在 `candidate_k=30` 之外。
- 把候选窗口扩到 60 后，目标页重排排名 **9**，分数 **0.9937**。
- 直接对目标页全部 23 个 chunk 做重排：
  - “Choose your starting point”：**0.9954**
  - “Managed Deep Agents”：**0.9937**
  - “Deep Agents”：**0.9350**

最佳答案 chunk 也没有被向量召回。如果 “Choose your starting point” 进入候选，目标页会排到第 2 名左右。

### 4.2 页面本身的问题

`build-overview` 只有 527 词，却被切成了 **23 个 chunk**。原始 Markdown 中这些段落重复了两遍：

- Managed Deep Agents
- Deep Agents
- LangChain
- LangGraph
- Prefer no-code?
- Integrations / Learn / Reference / Contribute

因此索引中存在大量完全重复的 chunk，浪费候选名额，也会干扰页面级聚合。

同时，问题的答案被拆在两个 H2：

- “Managed Deep Agents”：托管部署、LangSmith 运行 harness/runtime、最快方式；
- “Deep Agents”：相同 harness、最大灵活性、自托管或自定义 Agent Server。

单个 chunk 只覆盖一半，重排器很难给完整答案高分。

### 4.3 评测标注问题

排名第 4、5 的 `managed-deep-agents-overview` 页面都有 “Relationship to Deep Agents” 小节，实际上能回答这个问题。当前评测只认 `build-overview` 一个 URL，因此把这些页面算作未命中。

所以 q044 同时包含：

- 目标 hub 页的召回问题；
- chunk 切分过碎 + 原始页面重复；
- 评测标注只认单一 URL 的问题。

### 4.4 翻译 query 的结果

翻译后的 query：

> What is the difference between Deep Agents and Managed Deep Agents?

- 目标页最佳重排排名 **10～12**，分数 **0.9098**。
- 仍然没有进入 top 5。
- 最佳答案 chunk “Choose your starting point” 仍然没有被召回。

## 5. 三条案例的共同结论

1. **主要瓶颈在向量召回，不在 reranker。**
   三条案例的目标页最佳答案 chunk 直接重排分分别是 0.9925、0.9282、0.9954，说明 reranker 能识别答案；问题是它们没有进入向量候选集。

2. **单纯增大 candidate_k 不够。**
   - q001 目标页在 top 60 中只排 52；
   - q010 包含 stateless 解释的 chunk 在 top 60 中仍未出现，top 60 里只有 Repeat request 的表格引导 chunk（排 23）；
   - q044 目标页在 top 60 中排 9。
   继续加到 50/60 只能覆盖部分边界案例，不能解决 q001/q010/q044 的答案 chunk 召回问题。

3. **chunk 切分和页面重复是第二大头。**
   - q010 的答案跨 “Patterns” 和 “Repeat request”；
   - q044 的答案跨 “Managed Deep Agents” 和 “Deep Agents”，且页面重复；
   - q001 的 overview 页面也被切成 22 个 chunk，答案分别落在 “Agent = Model + Harness” 和 “Built on top of LangGraph”。

4. **评测口径放大了失败。**
   - q010 的 top 1 是同一页面的 JavaScript 版本；
   - q044 的 top 4/5 是专门讲 Managed Deep Agents 的页面，包含 “Relationship to Deep Agents”。
   如果做平台归一化或语义等价判定，q010 可以算 Hit@1，q044 可以算 Hit@4/5；只有 q001 是严格意义上的真失败。

5. **翻译不是稳定收益。**
   - q001 翻译后目标页跌出 top 100；
   - q010 从 rank 10 提升到 7，但仍未进 top 5；
   - q044 仍然在 10 名左右。
   翻译应作为“额外一路召回”与原始 query 融合，而不是替换原始 query。

## 6. 建议的改进优先级

1. **Hybrid retrieval**
   - BM25/关键词检索 + dense 向量检索，再做融合；
   - 对 `create_agent`、`Subagents`、`stateless`、`Managed Deep Agents` 这类精确术语效果会很明显。

2. **Chunking 重构**
   - 兄弟 chunk 合并：比较类问题把相邻 H2 合并成父级 chunk；
   - parent-child retrieval：先召回子 chunk，再扩展到父 section；
   - 入库前按内容 hash 去重，避免 `build-overview` 这种重复段落。

3. **Query 侧增强**
   - 多 query / query decomposition：q010 拆成“Subagents 如何工作”和“重复请求为什么仍调用模型”；
   - 原始 query 与翻译 query 双路召回后融合；
   - 抽取实体和关键词，作为 BM25 的补充。

4. **评测口径**
   - Python/JavaScript 页面做平台归一化；
   - 允许语义等价页面，或增加 answer-point recall；
   - 否则会把 q010/q044 这类“检索结果其实可用”的案例误判为失败。

5. **Reranker**
   - 页面级聚合（同一 URL 取 top chunk 分数）可以作为补充；
   - 但对 q001/q010/q044，页面级聚合仍然受限于“答案 chunk 没被召回”，所以不是第一优先级。

6. **Embedding 模型**
   - 中文 query + 英文文档场景下，考虑多语言 embedding 或双语索引；
   - 当前模型对 q001 的概念页召回明显不足。
