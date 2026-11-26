# Self-query 翻译版测试报告

- 日期：2026-11-24
- 测试对象：当前版本的 Self-query + 翻译 + rerank + doc_type 惩罚
- 测试集：`tests/evaluation/qa_set.jsonl`，57 条可回答问题
- 当前结果文件：`tests/evaluation/test_SelfQuery/translate_outcome.json`
- 惩罚项基线 JSON：`tests/evaluation/test_retrieval/retrieval_report_rerank_v2m3_penalty.json`
- 惩罚项实验报告：`tests/evaluation/test_retrieval/doctype_penalty_comparison.md`

## 1. 实验配置

| 项目 | 值 |
|---|---|
| Self-query | 已启用 |
| 翻译 | 已通过 schema prompt + examples 启用 |
| 向量召回 | `candidate_k=30` |
| 最终文档数 | top 10（评测口径） |
| Reranker | `BAAI/bge-reranker-v2-m3` |
| doc_type 惩罚 | changelog -0.05，release -0.03 |
| 基线 | 纯向量检索 + rerank + 惩罚，无 Self-query |
| 评测粒度 | 页面 URL 去重，Hit@k / Recall@k / MRR@k / nDCG@k |

## 2. 总体对比

| k | 基线 Hit@k | Self-query Hit@k | ΔHit | 基线 MRR@k | Self-query MRR@k | ΔMRR | 基线 nDCG@k | Self-query nDCG@k | ΔnDCG |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.6842 | 0.6316 | **-0.0526** | 0.6842 | 0.6316 | **-0.0526** | 0.6842 | 0.6316 | **-0.0526** |
| 3 | 0.8421 | 0.8421 | 0.0000 | 0.7602 | 0.7281 | -0.0321 | 0.7815 | 0.7575 | -0.0240 |
| 4 | 0.8947 | 0.8596 | -0.0351 | 0.7734 | 0.7325 | -0.0409 | 0.8042 | 0.7651 | -0.0391 |
| 5 | 0.9123 | 0.8596 | **-0.0527** | 0.7769 | 0.7325 | **-0.0444** | 0.8110 | 0.7651 | **-0.0459** |
| 10 | 0.9474 | 0.8947 | **-0.0527** | 0.7810 | 0.7367 | -0.0443 | 0.8218 | 0.7760 | -0.0458 |

结论：Self-query + 翻译在当前实现下**没有超过**纯检索 + rerank 基线，整体略有下降。

## 3. 中文子集

| 指标 | 基线 | Self-query | 变化 |
|---|---:|---:|---:|
| Hit@1 | 0.6389 | 0.5000 | **-0.1389** |
| Hit@3 | 0.8056 | 0.7500 | -0.0556 |
| Hit@5 | 0.8611 | 0.7778 | **-0.0833** |
| Hit@10 | 0.9167 | 0.8333 | -0.0834 |
| MRR@5 | 0.7361 | 0.6227 | **-0.1134** |
| nDCG@5 | 0.7680 | 0.6624 | **-0.1056** |

中文子集下降明显，说明翻译改善了 q026/q057，但也让部分原本能命中的问题失去了召回。

## 4. metadata_filter 子集

| 指标 | 基线 | Self-query | 变化 |
|---|---:|---:|---:|
| Hit@1 | 0.6667 | 0.9333 | **+0.2666** |
| Hit@3 | 0.7333 | 1.0000 | **+0.2667** |
| Hit@5 | 0.8667 | 1.0000 | **+0.1333** |
| Hit@10 | 0.9333 | 1.0000 | +0.0667 |
| MRR@5 | 0.7300 | 0.9667 | **+0.2367** |
| nDCG@5 | 0.7632 | 0.9754 | **+0.2122** |

Self-query 对带有明确 title/url 过滤条件的 15 条 metadata_filter 题提升非常明显，几乎全部在 top-1 命中。

## 5. Filter 质量

```text
expected_filter_cases = 15
filter_present = 15
exact_match = 15
field_match = 15
value_match = 15
operator_match = 15
exact_match_rate = 1.0000
invalid_or_failed = 0
unexpected_filter_cases = 7
```

15 条 metadata_filter 的 filter 全部完全匹配。但模型在 7 条普通问题上生成了原问题没有的额外 filter：

- q023、q025：`platform = javascript`（恰好正确，未造成失败）
- q042：`doc_type = troubleshooting`（恰好正确）
- q032：`platform = python AND doc_type = guide`（过滤过窄）
- q034：`platform = python AND doc_type = api_reference`（过滤后 0 条）
- q035：`platform = python AND doc_type = guide`（过滤过窄）
- q043：`platform = python AND doc_type = troubleshooting`（过滤后 0 条）

其中 q032/q034/q035/q043 直接导致原本正常的普通问题失败。

## 6. must_keep_terms 覆盖率

```text
must_keep_terms_avg = 0.5353
rewrite_required_avg = 0.5435
cases_below_1 = 55/57
```

覆盖率偏低的原因：

- 中文改写为英文时会省略部分精确术语，例如 q026 缺少 `LANGSMITH_ENDPOINT`，q010 缺少 `stateless`
- 该指标是严格字面覆盖，不等于语义完整性
- 需要结合上一轮设计的 LLM judge（faithfulness、retrieval_suitability、language_quality、conciseness）一起判断

## 7. 案例变化

修复：

- q026：未命中 → rank 1
- q057：rank 8 → rank 2

新增失败：

- q028：基线 rank 4 → 未命中
- q032：基线 rank 1 → 未命中
- q034：基线 rank 1 → 未命中
- q035：基线 rank 1 → 未命中
- q043：基线 rank 1 → 未命中

仍然失败：

- q001、q010、q044
- q010 从 rank 9 提升到 rank 7，但仍未进 top-5
- q044 从基线未命中提升到 rank 10，仍未进 top-5

q028 没有生成 filter，query 也翻译成英文，但目标 `evaluation-quickstart` 没有进入 top-10；这属于 query 改写/召回问题，不是 filter 误杀。

## 8. 结论

1. **Self-query 对 metadata_filter 题非常有效**：filter exact 15/15，Hit@5 1.0，应保留这条能力
2. **但不能让所有问题都走 Self-query**：普通问题会出现不必要的 platform/doc_type filter，导致 q032/q034/q035/q043 失败
3. **整体和中文指标低于纯检索 + rerank 基线**，当前 Self-query 不适合作为默认唯一检索路径
4. q028 显示即使没有 filter，query 改写也可能降低召回
5. q010/q044 仍需 chunk 召回、Python/JS 版本标注或更强查询改写

## 9. 建议

优先做查询路由，而不是继续无条件启用 Self-query：

- 有明确 title/url/metadata 约束的问题 → Self-query
- 普通 how-to/conceptual 问题 → 原始 query + rerank + 惩罚
- 或修改 Self-query 提示词，强制普通问题输出 `NO_FILTER`，禁止自动添加 `platform/doc_type` filter
- 对翻译后的 query 增加关键术语保留约束，先改善 must_keep_terms 覆盖率
- 下一轮测试建议对比：
  1. 纯 rerank + 惩罚（当前基线）
  2. Self-query 只对 metadata_filter 题启用
  3. Self-query 全量但禁用非显式 filter

## 10. 复现

```powershell
python tests/test_SelfQuery.py --report tests/evaluation/test_SelfQuery/translate_outcome.json
```

基线：

```powershell
python tests/test_retriever.py --rerank --candidate-k 30 --report tests/evaluation/test_retrieval/retrieval_report_rerank_v2m3_penalty.json
```
