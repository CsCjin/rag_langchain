# Answer Generation Evaluation

- 日期：2026-11-26
- 测试集：`D:\My_rag\tests\evaluation\qa_set.jsonl`
- 模式：gold_answer, gold_docs
- 生成模型：`deepseek-chat`
- 结果：`D:\My_rag\tests\evaluation\test_generation\generation_report.json`

## 1. 总体评分

| 模式 | 样本 | correctness | faithfulness | completeness | citation | refusal | language | conciseness |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `gold_answer` | 62 | 1.0000 | 1.0000 | 0.9758 | N/A | 1.0000 | 1.0000 | 0.9919 |
| `gold_docs` | 62 | 1.0000 | 1.0000 | 0.9919 | 1.0000 | 1.0000 | 0.9839 | 1.0000 |

## 2. 规则指标

| 模式 | 关键术语覆盖 | 规则语言一致 | 引用存在率 | 引用编号有效 | 拒答检出率 | 误拒答率 | 无答案误答率 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `gold_answer` | 0.6952 | 1.0000 | 0.0000 | 0.0000 | 0.1452 | 0.0702 | 0.0000 |
| `gold_docs` | 0.7820 | 0.9839 | 1.0000 | 1.0000 | 0.0968 | 0.0175 | 0.0000 |

## 3. 按语言 / 类型拆分

### 按语言

| 分组 | 模式 | n | correctness | faithfulness | completeness |
|---|---|---:|---:|---:|---:|
| `zh` | `gold_answer` | 41 | 1.0000 | 1.0000 | 0.9756 |
| `zh` | `gold_docs` | 41 | 1.0000 | 1.0000 | 0.9878 |
| `en` | `gold_answer` | 21 | 1.0000 | 1.0000 | 0.9762 |
| `en` | `gold_docs` | 21 | 1.0000 | 1.0000 | 1.0000 |

### 按类型

| 分组 | 模式 | n | correctness | faithfulness | completeness |
|---|---|---:|---:|---:|---:|
| `conceptual` | `gold_answer` | 11 | 1.0000 | 1.0000 | 1.0000 |
| `conceptual` | `gold_docs` | 11 | 1.0000 | 1.0000 | 1.0000 |
| `metadata_filter` | `gold_answer` | 15 | 1.0000 | 1.0000 | 0.9667 |
| `metadata_filter` | `gold_docs` | 15 | 1.0000 | 1.0000 | 1.0000 |
| `how_to` | `gold_answer` | 19 | 1.0000 | 1.0000 | 1.0000 |
| `how_to` | `gold_docs` | 19 | 1.0000 | 1.0000 | 1.0000 |
| `configuration` | `gold_answer` | 3 | 1.0000 | 1.0000 | 1.0000 |
| `configuration` | `gold_docs` | 3 | 1.0000 | 1.0000 | 1.0000 |
| `factual` | `gold_answer` | 7 | 1.0000 | 1.0000 | 0.8571 |
| `factual` | `gold_docs` | 7 | 1.0000 | 1.0000 | 0.9286 |
| `troubleshooting` | `gold_answer` | 2 | 1.0000 | 1.0000 | 1.0000 |
| `troubleshooting` | `gold_docs` | 2 | 1.0000 | 1.0000 | 1.0000 |
| `unanswerable` | `gold_answer` | 5 | 1.0000 | 1.0000 | 1.0000 |
| `unanswerable` | `gold_docs` | 5 | 1.0000 | 1.0000 | 1.0000 |

## 4. 失败案例

- `q052` mode=`gold_docs` type=`metadata_filter` lang=`en` reasons=['language_consistency=0', 'rule_language_mismatch'] judge_reason='回答内容与参考答案一致，引用 [S1] 支持结论；但问题语言是英文，回答使用中文，语言一致性不通过。'

## 5. 结论

1. 本报告区分 `gold_answer` 与 `gold_docs` 两种 oracle 上下文：前者测复述与约束遵循，后者测给定完整正确文档后的回答生成。
2. 引用准确性只在 `gold_docs` 模式计分；`gold_answer` 模式的 context 只有参考答案，因此 citation 记为 N/A。
3. 完整性以 `reference_answer` 为 gold checklist，并结合 `must_keep_terms` 做规则覆盖。
4. 语言一致性同时要求 judge 和规则检查通过；q052 是英文问题但中文回答，规则捕获了该问题，judge 未捕获。
5. q034 的 completeness=1，原因是只回答了 `trace_id=` 的主路径，缺少子 run 场景的可选说明。
6. `must_keep_terms` 是严格字面匹配；中文答案通常不包含英文术语，因此该指标偏低只能作为辅助信号。

## 6. 复现

```powershell
$env:PYTHONPATH="D:\My_rag\src"
$env:HF_HUB_OFFLINE="1"
$env:TRANSFORMERS_OFFLINE="1"
python tests/test_AnswerGeneration.py
```
