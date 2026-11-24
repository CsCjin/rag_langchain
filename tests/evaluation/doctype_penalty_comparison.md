# Doc Type 惩罚项实验报告

- 日期：2026-11-24
- 目标：验证对 `changelog` / `release` 做 rerank 惩罚，是否能减少它们对 top-5 的挤占
- 模型：`BAAI/bge-reranker-v2-m3`
- 召回：`candidate_k=30`
- 评测：rerank top 10，计算 @1/@3/@5/@10
- 惩罚方式：在 cross-encoder 原始分数上做加法惩罚
  - `changelog`: -0.05
  - `release`: -0.03
- 对比：
  - 无惩罚：`retrieval_report_rerank_v2m3.json`
  - 有惩罚：`retrieval_report_rerank_v2m3_penalty.json`
- 机器可读结果：`doctype_penalty_comparison.json`

## 1. 总体指标

| k | Hit 无惩罚 | Hit 有惩罚 | MRR 无惩罚 | MRR 有惩罚 | nDCG 无惩罚 | nDCG 有惩罚 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.6667 | **0.6842** | 0.6667 | **0.6842** | 0.6667 | **0.6842** |
| 3 | 0.8421 | 0.8421 | 0.7515 | **0.7602** | 0.7751 | **0.7815** |
| 5 | 0.9123 | 0.9123 | 0.7673 | **0.7769** | 0.8037 | **0.8110** |
| 10 | 0.9474 | 0.9474 | 0.7714 | **0.7810** | 0.8146 | **0.8218** |

结论：

- Hit@k 基本不变，Hit@1 +1.75 个百分点
- MRR@5 +0.96 个百分点，nDCG@5 +0.73 个百分点
- @5 失败数仍为 5，但排序质量略有改善

中文 36 条：

| k | Hit 无惩罚 | Hit 有惩罚 | MRR 无惩罚 | MRR 有惩罚 |
|---:|---:|---:|---:|---:|
| 1 | 0.6389 | 0.6389 | 0.6389 | 0.6389 |
| 5 | 0.8611 | 0.8611 | 0.7347 | **0.7361** |
| 10 | 0.9167 | 0.9167 | 0.7413 | **0.7427** |

中文几乎没有变化，主要收益来自英文问题。

## 2. top-5 中的 changelog/release 挤占

| 指标 | 无惩罚 | 有惩罚 |
|---|---:|---:|
| top-5 中 changelog 次数 | 7 | **3** |
| top-5 中 release 次数 | 5 | **4** |
| 含 changelog/release 的问题数 | 8 | **4** |

问题列表：

- 无惩罚：q001、q005、q020、q022、q028、q031、q033、q037
- 有惩罚：q001、q020、q022、q037

明显改善：

- q028：目标页面从 rank 5 提升到 **rank 4**，changelog 被挤出 top-5
- q022：rank 2 → **rank 1**

没有完全解决：

- q001：top-5 仍有 3 个 release 页面，目标 overview 仍未命中
- q020/q022/q037 仍有 changelog/release 页面
- q010、q026、q044、q057 的失败与 changelog/release 无关，惩罚项没有作用

## 3. 案例变化

无惩罚 → 有惩罚，只有两条排名变化：

| id | 类型 | 语言 | 无惩罚 rank | 有惩罚 rank |
|---|---|---|---:|---:|
| q022 | how_to | en | 2 | **1** |
| q028 | how_to | zh | 5 | **4** |

失败案例仍为：

- q001：概览页被 runtime/release 页面压制
- q010：跨语言查询 + Python/JS 页面重复，目标页面 rank 9
- q026：title 元数据过滤未利用
- q044：概念对比页未命中
- q057：title 元数据过滤未利用，rank 8

## 4. 结论

惩罚项**部分解决了挤占问题**：

- changelog 的 top-5 出现次数从 7 降到 3，含 changelog/release 的问题数从 8 降到 4
- q028 和 q022 排名改善
- 但 release 只从 5 降到 4，q001 仍被 release 页面占据
- 对 q010/q026/q044/q057 无帮助

当前评测集没有 release/changelog 意图题，因此无法判断惩罚是否会误伤“最近更新了什么”“版本变化”等问题。也就是说：

- 现在可以保留惩罚作为默认策略
- 但不应继续加大惩罚，直到补上 release 意图评测
- 后续应增加查询意图分类，在 release 查询时关闭惩罚或提升 changelog/release
- q001 需要更强的手段：扩大候选、查询改写，或对 release 页面做硬过滤
- q010/q057 需要 Self-query 或 chunk 级优化，不应靠 doc_type 惩罚解决

## 5. 复现

```powershell
# 带惩罚
python tests/test_retriever.py --rerank --candidate-k 30 --report tests/evaluation/retrieval_report_rerank_v2m3_penalty.json

# 关闭惩罚
python tests/test_retriever.py --rerank --no-doc-type-penalty --candidate-k 30 --report tests/evaluation/retrieval_report_rerank_v2m3_nopenalty.json
```
