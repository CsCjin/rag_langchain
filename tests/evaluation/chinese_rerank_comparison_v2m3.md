# 中文查询 Rerank 对比：bge-reranker-v2-m3

- 日期：2026-11-24
- 目标：验证更换多语言 reranker 后，中文查询的检索排序是否改善
- 数据集：`tests/evaluation/qa_set.jsonl` 中的 36 条中文问题
- 索引：现有 Chroma 索引，未重建
- 召回：纯向量检索 `candidate_k=30`
- 评测 rerank 输出：top 10（用于计算 @1/@3/@4/@5/@10）
- 对比对象：
  - 纯向量：`baseline_retrieval_v1.json`
  - `BAAI/bge-reranker-base`：`retrieval_report_rerank.json`
  - `BAAI/bge-reranker-v2-m3`：`retrieval_report_rerank_v2m3.json`
- 机器可读结果：`chinese_rerank_comparison_v2m3.json`

## 1. 中文查询总体结果

| k | Hit 基线 | Hit base-rerank | Hit v2-m3 | MRR 基线 | MRR base-rerank | MRR v2-m3 | nDCG 基线 | nDCG base-rerank | nDCG v2-m3 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.4167 | 0.5000 | **0.6389** | 0.4167 | 0.5000 | **0.6389** | 0.4167 | 0.5000 | **0.6389** |
| 3 | 0.6944 | 0.7500 | **0.8056** | 0.5509 | 0.6157 | **0.7222** | 0.5883 | 0.6505 | **0.7440** |
| 4 | 0.7222 | 0.7778 | **0.8333** | 0.5579 | 0.6227 | **0.7292** | 0.6003 | 0.6624 | **0.7560** |
| 5 | 0.7778 | 0.7778 | **0.8611** | 0.5690 | 0.6227 | **0.7347** | 0.6217 | 0.6624 | **0.7668** |
| 10 | 0.8889 | 0.8056 | **0.9167** | 0.5835 | 0.6273 | **0.7413** | 0.6574 | 0.6723 | **0.7839** |

相对 base-reranker 的提升：

- Hit@1：+13.89 个百分点
- Hit@5：+8.33 个百分点
- MRR@5：+11.20 个百分点
- nDCG@5：+10.44 个百分点
- Hit@10：+11.11 个百分点（同时高于纯向量基线）

相对纯向量基线，中文 Hit@5 从 0.7778 提升到 0.8611，MRR@5 从 0.5690 提升到 0.7347。

## 2. 全部 57 条的整体结果

| k | Hit 基线 | Hit base-rerank | Hit v2-m3 | MRR 基线 | MRR base-rerank | MRR v2-m3 | nDCG 基线 | nDCG base-rerank | nDCG v2-m3 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.4211 | 0.5263 | **0.6667** | 0.4211 | 0.5263 | **0.6667** | 0.4211 | 0.5263 | **0.6667** |
| 3 | 0.7018 | 0.8070 | **0.8421** | 0.5556 | 0.6608 | **0.7515** | 0.5936 | 0.6988 | **0.7751** |
| 5 | 0.8070 | 0.8246 | **0.9123** | 0.5792 | 0.6652 | **0.7673** | 0.6366 | 0.7064 | **0.8037** |
| 10 | 0.9123 | 0.8596 | **0.9474** | 0.5942 | 0.6711 | **0.7714** | 0.6716 | 0.7189 | **0.8146** |

英文 21 条：v2-m3 的 Hit@5 为 1.0000，MRR@5 为 0.8230。全部失败案例降到 5/57，且全部是中文问题。

## 3. 中文案例变化

相对 `bge-reranker-base`：

- 修复失败：q028、q030、q041
- 新增失败：无
- 排名改善：10 条
- 排名变差：0 条
- 不变：26 条

主要排名变化：

| id | base-rerank rank | v2-m3 rank | 类型 | 说明 |
|---|---:|---:|---|---|
| q005 | 4 | 1 | how_to | MCP 人工审批，目标页升到第 1 |
| q010 | 未命中 | 9 | conceptual | 有改善但仍未进 top-5 |
| q018 | 2 | 1 | factual | 进入第 1 |
| q019 | 2 | 1 | how_to | 进入第 1 |
| q028 | 6 | 5 | how_to | 从失败变为刚好命中 |
| q030 | 未命中 | 4 | how_to | RAG 评测 tutorial 回到 top-5 |
| q033 | 3 | 1 | how_to | 进入第 1 |
| q041 | 未命中 | 2 | conceptual | Agent Server 页面升到第 2 |
| q053 | 3 | 1 | metadata_filter | 进入第 1 |
| q057 | 未命中 | 8 | metadata_filter | 有改善但仍未进 top-5 |

## 4. 剩余中文失败

v2-m3 仍有 5 条中文失败：

| id | rank | 类型 | 基线 rank | base-rerank rank | 原因 |
|---|---:|---|---:|---:|---|
| q001 | 未命中 | conceptual | 未命中 | 未命中 | 概览页被 release/runtime 页面抢占 |
| q010 | 9 | conceptual | 2 | 未命中 | 子图/异步 subagents 页面竞争；目标答案 chunk 未进 top-30 |
| q026 | 未命中 | metadata_filter | 未命中 | 未命中 | 纯检索忽略 title 过滤；应使用 Self-query |
| q044 | 未命中 | conceptual | 未命中 | 未命中 | Deep Agents 对比概览页未被选中 |
| q057 | 8 | metadata_filter | 7 | 未命中 | 纯检索忽略 title 过滤；需要 Self-query |

结论：

1. v2-m3 对中文检索改善非常明显，排序质量、top-1 和 top-10 都优于 base
2. q028/q030/q041 已被修复，说明多语言 cross-encoder 对中文语义理解更合适
3. q010 从“未命中”提升到第 9，但仍受 chunk 级召回限制
4. q026/q057 是元数据过滤题，纯检索天然无法利用 title，应交给 Self-query
5. q001/q044 属于概念概览/对比问题，仍需要更好的候选召回或查询改写

## 5. 建议

1. 将 `BAAI/bge-reranker-v2-m3` 作为默认 reranker（已更新默认配置）
2. 保持 `candidate_k=30` 作为当前基线，下一步测试 `candidate_k=50`，重点看 q010/q044/q057
3. 对 q026/q057 启用 Self-query title/url 过滤
4. q001/q044 需要复核标注或增加查询改写/概览页召回
5. v2-m3 比 base 更大，需关注加载时间和 GPU 显存/推理延迟

## 6. 复现命令

```powershell
python tests/test_retriever.py --rerank --candidate-k 30 --report tests/evaluation/retrieval_report_rerank_v2m3.json
```
