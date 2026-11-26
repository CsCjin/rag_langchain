# Final Pipeline Evaluation

- 日期：2026-11-26
- 测试集：`D:\My_rag\tests\evaluation\qa_set.jsonl`
- 流程：router → hybrid → sibling merge → rerank → LLM → language guard
- 返回文档数：top 5
- 生成模型：`deepseek-chat`
- 图扩展：`{'nodes': 58675, 'edges': 98114, 'pages': 1733, 'sections': 14376, 'chunks': 42650, 'same_topic_links': 215}`
- 结果：`D:\My_rag\tests\evaluation\final_test\final_pipeline_report.json`

## 0. 与无图基线对比

| 检索指标（k=5） | baseline | graph | Δ |
|---|---:|---:|---:|
| Hit@5 | 0.9649 | 0.9649 | +0.0000 |
| MRR@5 | 0.8450 | 0.8450 | +0.0000 |
| nDCG@5 | 0.8756 | 0.8756 | +0.0000 |

| 生成指标 | baseline | graph | Δ |
|---|---:|---:|---:|
| correctness | 0.7097 | 0.9758 | +0.2661 |
| faithfulness | 1.0000 | 1.0000 | +0.0000 |
| completeness | 0.6452 | 0.9516 | +0.3065 |
| citation_accuracy | 0.9211 | 1.0000 | +0.0789 |
| refusal_accuracy | 0.8871 | 0.9839 | +0.0968 |
| language_consistency | 1.0000 | 1.0000 | +0.0000 |
| conciseness | 0.9597 | 1.0000 | +0.0403 |

- 检索修复：无
- 检索新增失败：无
- correctness 提升：q001, q003, q005, q010, q011, q012, q013, q014, q015, q016, q018, q019, q021, q022, q023, q025, q027, q030, q031, q033, q035, q038, q040, q042, q043, q053, q057
- correctness 下降：无
- completeness 提升：q003, q004, q005, q007, q010, q011, q012, q013, q014, q016, q018, q019, q021, q022, q023, q024, q025, q027, q029, q030, q031, q033, q034, q035, q038, q039, q040, q042, q043, q045, q053, q057, q061
- completeness 下降：无

## 1. 检索指标（RAGChain 实际返回文档）

检索指标按 57 条可回答样本计算；生成指标按 62 条样本计算（含无答案样本）。

| k | Hit@k | Recall@k | MRR@k | nDCG@k |
|---:|---:|---:|---:|---:|
| 1 | 0.7544 | 0.7544 | 0.7544 | 0.7544 |
| 3 | 0.9298 | 0.9298 | 0.8363 | 0.8605 |
| 5 | 0.9649 | 0.9649 | 0.8450 | 0.8756 |

## 2. 路由与 Filter

```text
route_counts = {'default': 43, 'self_query': 19}
expected_route_counts = {'default': 43, 'self_query': 19}
route_accuracy = 1.0000
expected_filter_cases = 15
filter_present = 15
exact_match = 15
exact_match_rate = 1.0000
unexpected_filter_cases = 4
unexpected_filter_ids = ['q023', 'q025', 'q042', 'q043']
invalid_or_failed = 0
```

## 3. 生成质量（真实检索 context）

| 指标 | 值 |
|---|---:|
| correctness | 0.9758 |
| faithfulness | 1.0000 |
| completeness | 0.9516 |
| citation_accuracy | 1.0000 |
| refusal_accuracy | 0.9839 |
| language_consistency | 1.0000 |
| conciseness | 1.0000 |

## 4. 按路由拆分（k=5）

| 路由 | n | retrieval_n | Hit@5 | MRR@5 | correctness | faithfulness | completeness |
|---|---:|---:|---:|---:|---:|---:|---:|
| `default` | 43 | 38 | 0.9474 | 0.7807 | 0.9651 | 1.0000 | 0.9302 |
| `self_query` | 19 | 19 | 1.0000 | 0.9737 | 1.0000 | 1.0000 | 1.0000 |

## 5. 按语言 / 类型拆分（k=5）

### 按语言

| 分组 | n | retrieval_n | Hit@5 | correctness | faithfulness | completeness |
|---|---:|---:|---:|---:|---:|---:|
| `zh` | 41 | 36 | 0.9444 | 0.9634 | 1.0000 | 0.9390 |
| `en` | 21 | 21 | 1.0000 | 1.0000 | 1.0000 | 0.9762 |

### 按类型

| 分组 | n | retrieval_n | Hit@5 | correctness | faithfulness | completeness |
|---|---:|---:|---:|---:|---:|---:|
| `conceptual` | 11 | 11 | 0.8182 | 0.9091 | 1.0000 | 0.8636 |
| `metadata_filter` | 15 | 15 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| `how_to` | 19 | 19 | 1.0000 | 0.9737 | 1.0000 | 0.9211 |
| `configuration` | 3 | 3 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| `factual` | 7 | 7 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| `troubleshooting` | 2 | 2 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| `unanswerable` | 5 | 0 | N/A | 1.0000 | 1.0000 | 1.0000 |

## 6. 失败案例

- `q001` route=`default` rank=None reasons=['retrieval_miss'] judge_reason='回答准确解释了 create_agent 是高度可配置的 harness，并正确说明其返回编译后的 LangGraph graph，引用均来自上下文且支持结论。但遗漏了参考答案中关于 LangGraph 持久执行、human-in-the-loop 等能力以及高级场景使用 LangGraph 编排的关键点，完整性略有不足。'
- `q010` route=`default` rank=None reasons=['retrieval_miss'] judge_reason='回答准确描述了 Subagents 模式中主智能体将子智能体作为工具协调、所有路由经过主智能体，并正确解释了无状态设计导致重复请求时每次仍执行完整流程（4 次调用、两轮共 8 次），与参考答案和 S1/S8 一致；引用 S1、S2、S7、S8 均支持对应结论，语言为中文，简洁无冗余。'
- `q041` route=`default` rank=3 reasons=['correctness=0', 'completeness=0', 'refusal_correct=0'] judge_reason='问题可回答，但模型回答误判为无法回答，未提供 run 执行生命周期的任何关键步骤，属于误拒答；其陈述均可在上下文中找到支持，引用编号有效，语言与问题一致，但未覆盖参考答案的核心内容。'

## 7. 结论

1. 本报告是端到端结果：检索、路由、兄弟合并、生成和语言检查都走生产 `RAGChain`。
2. 实际检索 Hit@5 = 0.9649，MRR@5 = 0.8450。
3. 生成 correctness = 0.9758，faithfulness = 1.0000，completeness = 0.9516，citation = 1.0000，refusal = 0.9839，language = 1.0000。
4. 该结果使用真实检索 context，不能与 gold_docs oracle 结果直接等价比较。
5. 生成端的主要瓶颈是 context 覆盖，而不是幻觉：faithfulness=1.0000，但 completeness=0.6452，7 条可回答样本因检索 context 缺少答案而误拒答。下一轮应优先提升 chunk 召回和上下文覆盖，而不是继续调生成提示词。

## 8. 复现

```powershell
$env:PYTHONPATH="D:\My_rag\src"
$env:HF_HUB_OFFLINE="1"
$env:TRANSFORMERS_OFFLINE="1"
python tests/test_FinalPipeline.py --workers 2 --timeout 180 --restart
```
