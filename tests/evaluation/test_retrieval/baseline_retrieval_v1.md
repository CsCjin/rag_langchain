# Retrieval Baseline v1

- 记录时间：2026-11-20
- 对象：纯向量检索（不包含 Self-query、不调用生成 LLM）
- 评测脚本：`tests/test_retriever.py`
- 数据集：`tests/evaluation/qa_set.jsonl`
- 机器可读快照：`tests/evaluation/test_retrieval/baseline_retrieval_v1.json`
- 本次运行报告：`tests/evaluation/test_retrieval/retrieval_report.json`

## 1. 配置

| 项目 | 值 |
|---|---|
| 文档数 | 1733 |
| chunk 数 | 43245 |
| chunk_size / overlap | 512 / 50 |
| separators | `\n`, `""` |
| 嵌入模型 | `IEITYuan/Yuan-embedding-2.0-en` |
| 向量维度 | 1024 |
| 向量库 | Chroma，collection=`langchain_docs` |
| 检索方式 | 原始问题直接向量检索 |
| 结果粒度 | 页面 URL 去重后的 top-10 |
| 评测样本 | 62 条，评测 57 条，排除 5 条不可回答 |
| 其中元数据过滤题 | 15 条 |
| k 值 | 1, 3, 5, 10 |

## 2. 总体指标

| k | Hit@k | Recall@k | MRR@k | nDCG@k |
|---:|---:|---:|---:|---:|
| 1 | 0.4211 | 0.4211 | 0.4211 | 0.4211 |
| 3 | 0.7018 | 0.7018 | 0.5556 | 0.5936 |
| 5 | 0.8070 | 0.8070 | 0.5792 | 0.6366 |
| 10 | 0.9123 | 0.9123 | 0.5942 | 0.6716 |

每条问题只有 1 个相关 URL，因此 Recall@k 与 Hit@k 数值相同。

## 3. 分组指标 @5

| 分组 | n | Hit@1 | Hit@5 | MRR@5 | nDCG@5 |
|---|---:|---:|---:|---:|---:|
| conceptual | 11 | 0.1818 | 0.7273 | 0.4318 | 0.5078 |
| configuration | 3 | 0.3333 | 0.6667 | 0.4000 | 0.4623 |
| factual | 7 | 0.5714 | 0.8571 | 0.6905 | 0.7330 |
| how_to | 19 | 0.5263 | 0.8947 | 0.6947 | 0.7459 |
| metadata_filter | 15 | 0.3333 | 0.7333 | 0.4689 | 0.5340 |
| troubleshooting | 2 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| 英文 | 21 | 0.4286 | 0.8571 | 0.5968 | 0.6620 |
| 中文 | 36 | 0.4167 | 0.7778 | 0.5690 | 0.6217 |

过滤题 / 非过滤题对比：

| 子集 | n | Hit@1 | Hit@5 | MRR@5 |
|---|---:|---:|---:|---:|
| all | 57 | 0.4211 | 0.8070 | 0.5792 |
| non_filter | 42 | 0.4524 | 0.8333 | 0.6187 |
| metadata_filter | 15 | 0.3333 | 0.7333 | 0.4689 |

## 4. 排名结构

- top-1 命中：24/57
- 命中案例平均排名：2.46
- 排名分布：第 1 名 24 条，第 2 名 14 条，第 3 名 2 条，第 4 名 3 条，第 5 名 3 条，第 6–10 名 6 条，未命中 5 条
- 失败 @5：11/57，其中 5 条完全未进 top-10，6 条排名 6–10

## 5. 失败案例

### q001

- 类型/语言：conceptual / zh
- 排名：未命中
- 问题：LangChain 里的 create_agent 是什么？它和 LangGraph 是什么关系？
- 正确 URL：`https://docs.langchain.com/oss/python/langchain/overview`
- 实际 top3：
  - `https://docs.langchain.com/oss/javascript/langchain/runtime`
  - `https://docs.langchain.com/oss/python/langchain/runtime`
  - `https://docs.langchain.com/oss/javascript/releases/langchain-v1`
- 疑似原因：概念概览页被 runtime/release 页抢占；Python/JS 双版本干扰

### q004

- 类型/语言：conceptual / en
- 排名：6
- 问题：What is MCPAdapter in LangChain and how does it turn MCP server tools into tools usable by a LangChain agent?
- 正确 URL：`https://docs.langchain.com/oss/python/langchain/mcp`
- 实际 top3：
  - `https://docs.langchain.com/oss/javascript/langchain/mcp/tools`
  - `https://docs.langchain.com/oss/python/langchain/mcp/tools`
  - `https://docs.langchain.com/oss/python/langchain/tools`
- 疑似原因：同主题子页面（mcp/tools）抢占；Python/JS 双版本干扰

### q005

- 类型/语言：how_to / zh
- 排名：7
- 问题：如何让 LangChain 智能体在调用 MCP 工具时，仅对服务器标记为破坏性的工具弹出人工审批？
- 正确 URL：`https://docs.langchain.com/oss/python/langchain/mcp/tools`
- 实际 top3：
  - `https://docs.langchain.com/langsmith/langsmith-mcp-server`
  - `https://docs.langchain.com/langsmith/server-mcp`
  - `https://docs.langchain.com/oss/javascript/integrations/chat/openai`
- 疑似原因：LangChain MCP 与 LangSmith MCP 产品混淆

### q016

- 类型/语言：configuration / zh
- 排名：9
- 问题：如何把 GitHub 仓库中的 LangChain agent 部署到 LangSmith Cloud，并获取 Agent Server 的 API URL？
- 正确 URL：`https://docs.langchain.com/oss/python/langchain/deploy`
- 实际 top3：
  - `https://docs.langchain.com/langsmith/cicd-pipeline-example`
  - `https://docs.langchain.com/langsmith/deploy-to-cloud`
  - `https://docs.langchain.com/oss/javascript/langchain/studio`
- 疑似原因：同类部署页面抢占

### q020

- 类型/语言：factual / en
- 排名：未命中
- 问题：What is the `create_agent` function in LangChain and what does the harness include?
- 正确 URL：`https://docs.langchain.com/oss/javascript/langchain/overview`
- 实际 top3：
  - `https://docs.langchain.com/oss/python/releases/langchain-v1`
  - `https://docs.langchain.com/oss/javascript/deepagents/customization`
  - `https://docs.langchain.com/oss/javascript/releases/langchain-v1`
- 疑似原因：Python/JS 双版本混淆；release 页面干扰

### q026

- 类型/语言：metadata_filter / zh
- 排名：未命中
- 问题：在《Tracing quickstart - Docs by LangChain》这篇文档里，如果我的 LangSmith 账号位于 EU 区域，需要设置哪个环境变量、设成什么值，否则 API key 会无法通过认证？
- 正确 URL：`https://docs.langchain.com/langsmith/observability-quickstart`
- 实际 top3：
  - `https://docs.langchain.com/langsmith/llm-gateway-authentication`
  - `https://docs.langchain.com/langsmith/trace-with-temporal`
  - `https://docs.langchain.com/langsmith/trace-with-langgraph`
- 疑似原因：纯检索忽略 title 元数据过滤

### q038

- 类型/语言：how_to / zh
- 排名：8
- 问题：如何用 langgraph deploy 命令把应用部署到 LangSmith Cloud，并在部署后用 Python SDK 测试 API？
- 正确 URL：`https://docs.langchain.com/langsmith/deployment-quickstart`
- 实际 top3：
  - `https://docs.langchain.com/langsmith/deploy-google-adk`
  - `https://docs.langchain.com/langsmith/deploy-other-frameworks`
  - `https://docs.langchain.com/langsmith/deploy-to-cloud-overview`
- 疑似原因：同类部署页面抢占

### q044

- 类型/语言：conceptual / zh
- 排名：未命中
- 问题：LangChain 的 Deep Agents 和 Managed Deep Agents 有什么区别？
- 正确 URL：`https://docs.langchain.com/build-overview`
- 实际 top3：
  - `https://docs.langchain.com/langsmith/javascript/managed-deep-agents-tools`
  - `https://docs.langchain.com/langsmith/python/managed-deep-agents-tools`
  - `https://docs.langchain.com/oss/python/learn`
- 疑似原因：概念对比题；概览页未排前；相邻产品页抢占

### q052

- 类型/语言：metadata_filter / en
- 排名：6
- 问题：According to the LangChain docs at https://docs.langchain.com/oss/python/langchain/messages, what fields does a ToolMessage require, and what is the purpose of its artifact field?
- 正确 URL：`https://docs.langchain.com/oss/python/langchain/messages`
- 实际 top3：
  - `https://docs.langchain.com/oss/javascript/integrations/chat/openai`
  - `https://docs.langchain.com/oss/javascript/integrations/chat/anthropic`
  - `https://docs.langchain.com/oss/python/langchain/mcp/tools`
- 疑似原因：纯检索忽略 URL 元数据过滤；精确术语混淆

### q057

- 类型/语言：metadata_filter / zh
- 排名：7
- 问题：在《Middleware overview - Docs by LangChain》这篇文档里，中间件（middleware）是如何接入 agent 的？它又通过什么方式在 agent 循环中生效？
- 正确 URL：`https://docs.langchain.com/oss/python/langchain/middleware/overview`
- 实际 top3：
  - `https://docs.langchain.com/oss/javascript/contributing/implement-langchain`
  - `https://docs.langchain.com/oss/python/releases/langchain-v1`
  - `https://docs.langchain.com/oss/python/contributing/implement-langchain`
- 疑似原因：纯检索忽略 title 元数据过滤；release/contributing 页面干扰；Python/JS 双版本

### q061

- 类型/语言：metadata_filter / zh
- 排名：未命中
- 问题：在《Trace an agent - Docs by LangChain》这篇文档中，如果我想在终端查看某个特定 trace 的完整运行层级和输入输出，应该执行什么命令？
- 正确 URL：`https://docs.langchain.com/langsmith/observability-llm-tutorial`
- 实际 top3：
  - `https://docs.langchain.com/oss/javascript/deepagents/rag`
  - `https://docs.langchain.com/oss/python/deepagents/rag`
  - `https://docs.langchain.com/oss/python/deepagents/overview`
- 疑似原因：纯检索忽略 title 元数据过滤

## 6. 已知问题

1. top-1 精度低：42.11%，且 14 条命中排在第 2 名；主要损失在排序而非召回
2. 概念型问题最弱：Hit@1 18.18%，overview/runtime/release 页面容易互抢
3. 中文查询弱于英文：Hit@5 77.78% vs 85.71%，英文嵌入模型导致跨语言损失
4. 纯检索无法利用 title/url 元数据：4 条失败案例属于该类
5. Python/JS 双版本文档互相干扰：q001、q004、q020、q057
6. 同类页面/邻近产品页抢占：部署、MCP、Managed Deep Agents
7. 6 条失败排名在 6–10，属于近邻失败，rerank 有较大提升空间
8. 通用导航片段：739 个（1.71%），86.6% 为链接堆叠；不建议直接删除 Prerequisites/Setup 等结构片段（1813 个，67.1% 含代码）
9. 评测限制：页面级二值相关性、只有 1 个相关 URL、troubleshooting 仅 2 条，不代表 chunk 级排序质量

## 7. 复现与对比

```powershell
python tests/test_retriever.py
```

修改检索、索引或数据后，重新运行同一脚本，并对比：

- `tests/evaluation/test_retrieval/retrieval_report.json`
- `tests/evaluation/test_retrieval/baseline_retrieval_v1.json`
- 本文件中的指标和失败案例

建议后续对比项：Self-query、rerank、`section`/`language` 元数据、中文查询改写、k 值变化。
