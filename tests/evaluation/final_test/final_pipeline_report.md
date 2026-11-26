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
| correctness | 0.7097 | 0.9597 | +0.2500 |
| faithfulness | 1.0000 | 1.0000 | +0.0000 |
| completeness | 0.6452 | 0.9355 | +0.2903 |
| citation_accuracy | 0.9211 | 0.9912 | +0.0702 |
| refusal_accuracy | 0.8871 | 0.9677 | +0.0806 |
| language_consistency | 1.0000 | 1.0000 | +0.0000 |
| conciseness | 0.9597 | 0.9839 | +0.0242 |

- 检索修复：无
- 检索新增失败：无
- correctness 提升：q001, q003, q005, q010, q011, q012, q013, q014, q015, q016, q018, q019, q021, q022, q023, q025, q027, q030, q031, q033, q035, q038, q040, q042, q043, q053, q057
- correctness 下降：q026
- completeness 提升：q003, q004, q005, q007, q010, q011, q012, q013, q015, q016, q018, q019, q021, q022, q023, q024, q025, q027, q029, q030, q031, q033, q034, q035, q038, q039, q040, q042, q043, q045, q053, q057
- completeness 下降：q026

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
| correctness | 0.9597 |
| faithfulness | 1.0000 |
| completeness | 0.9355 |
| citation_accuracy | 0.9912 |
| refusal_accuracy | 0.9677 |
| language_consistency | 1.0000 |
| conciseness | 0.9839 |

## 4. 按路由拆分（k=5）

| 路由 | n | retrieval_n | Hit@5 | MRR@5 | correctness | faithfulness | completeness |
|---|---:|---:|---:|---:|---:|---:|---:|
| `default` | 43 | 38 | 0.9474 | 0.7807 | 0.9651 | 1.0000 | 0.9419 |
| `self_query` | 19 | 19 | 1.0000 | 0.9737 | 0.9474 | 1.0000 | 0.9211 |

## 5. 按语言 / 类型拆分（k=5）

### 按语言

| 分组 | n | retrieval_n | Hit@5 | correctness | faithfulness | completeness |
|---|---:|---:|---:|---:|---:|---:|
| `zh` | 41 | 36 | 0.9444 | 0.9390 | 1.0000 | 0.9024 |
| `en` | 21 | 21 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

### 按类型

| 分组 | n | retrieval_n | Hit@5 | correctness | faithfulness | completeness |
|---|---:|---:|---:|---:|---:|---:|
| `conceptual` | 11 | 11 | 0.8182 | 0.9091 | 1.0000 | 0.8636 |
| `metadata_filter` | 15 | 15 | 1.0000 | 0.9333 | 1.0000 | 0.9000 |
| `how_to` | 19 | 19 | 1.0000 | 0.9737 | 1.0000 | 0.9474 |
| `configuration` | 3 | 3 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| `factual` | 7 | 7 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| `troubleshooting` | 2 | 2 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| `unanswerable` | 5 | 0 | N/A | 1.0000 | 1.0000 | 1.0000 |

## 6. 失败案例

- `q001` route=`default` rank=None reasons=['retrieval_miss'] judge_reason='回答准确解释了 create_agent 是高度可配置的 harness，并正确引用 S3 说明 Agent = Model + Harness；也正确引用 S1/S2/S6 说明 create_agent 返回/底层生成 LangGraph graph。但缺少参考答案中关于 LangChain agents 构建在 LangGraph 之上从而获得持久执行、human-in-the-loop、持久化能力，以及高级场景使用 LangGraph 底层编排框架的关键信息，故 completeness 为 1。所有事实性陈述均有上下文支持，引用编号正确且支持结论。'
- `q010` route=`default` rank=None reasons=['retrieval_miss'] judge_reason='回答准确描述了 Subagents 模式中主智能体将子智能体作为工具协调、所有路由经过主智能体，并正确解释了无状态设计导致重复请求时仍执行完整流程（4 次调用、共 8 次），同时提到上下文隔离的代价及与有状态模式的对比。所有事实性陈述均有 S1、S4、S8 支持，引用编号正确且对应结论，语言与问题一致，内容简洁无冗余。'
- `q026` route=`self_query` rank=1 reasons=['correctness=0', 'completeness=0', 'refusal_correct=0'] judge_reason='问题可回答，参考答案明确指出需设置 LANGSMITH_ENDPOINT="https://eu.api.smith.langchain.com"。模型误判为无法回答，属于错误拒答，遗漏全部关键信息，correctness 与 refusal_correct 均为 0。'
- `q041` route=`default` rank=3 reasons=['correctness=0', 'completeness=0', 'refusal_correct=0'] judge_reason='模型回答明确拒答，但问题可回答且参考答案给出了完整的 run 生命周期；上下文虽未直接描述完整生命周期，但模型未尝试基于已有信息作答，属于误拒答。回答中引用的事实性陈述均可在上下文中找到支持，引用编号正确，语言与问题一致，内容简洁。'

## 7. 结论

1. 本报告是端到端结果：检索、路由、兄弟合并、生成和语言检查都走生产 `RAGChain`。
2. 实际检索 Hit@5 = 0.9649，MRR@5 = 0.8450。
3. 生成 correctness = 0.9597，faithfulness = 1.0000，completeness = 0.9355，citation = 0.9912，refusal = 0.9677，language = 1.0000。
4. 该结果使用真实检索 context，不能与 gold_docs oracle 结果直接等价比较。
5. 生成端的主要瓶颈是 context 覆盖，而不是幻觉：faithfulness=1.0000，但 completeness=0.6452，7 条可回答样本因检索 context 缺少答案而误拒答。下一轮应优先提升 chunk 召回和上下文覆盖，而不是继续调生成提示词。

## 8. 复现

```powershell
$env:PYTHONPATH="D:\My_rag\src"
$env:HF_HUB_OFFLINE="1"
$env:TRANSFORMERS_OFFLINE="1"
python tests/test_FinalPipeline.py --workers 2 --timeout 180 --restart
```
