# Final Pipeline Evaluation

- 日期：2026-11-26
- 测试集：`D:\My_rag\tests\evaluation\qa_set.jsonl`
- 流程：router → hybrid → sibling merge → rerank → LLM → language guard
- 返回文档数：top 5
- 生成模型：`deepseek-chat`
- 结果：`D:\My_rag\tests\evaluation\final_test\final_pipeline_report.json`

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
| correctness | 0.7097 |
| faithfulness | 1.0000 |
| completeness | 0.6452 |
| citation_accuracy | 0.9211 |
| refusal_accuracy | 0.8871 |
| language_consistency | 1.0000 |
| conciseness | 0.9597 |

## 4. 按路由拆分（k=5）

| 路由 | n | retrieval_n | Hit@5 | MRR@5 | correctness | faithfulness | completeness |
|---|---:|---:|---:|---:|---:|---:|---:|
| `default` | 43 | 38 | 0.9474 | 0.7807 | 0.6628 | 1.0000 | 0.5814 |
| `self_query` | 19 | 19 | 1.0000 | 0.9737 | 0.8158 | 1.0000 | 0.7895 |

## 5. 按语言 / 类型拆分（k=5）

### 按语言

| 分组 | n | retrieval_n | Hit@5 | correctness | faithfulness | completeness |
|---|---:|---:|---:|---:|---:|---:|
| `zh` | 41 | 36 | 0.9444 | 0.6585 | 1.0000 | 0.5976 |
| `en` | 21 | 21 | 1.0000 | 0.8095 | 1.0000 | 0.7381 |

### 按类型

| 分组 | n | retrieval_n | Hit@5 | correctness | faithfulness | completeness |
|---|---:|---:|---:|---:|---:|---:|
| `conceptual` | 11 | 11 | 0.8182 | 0.7727 | 1.0000 | 0.6364 |
| `metadata_filter` | 15 | 15 | 1.0000 | 0.9333 | 1.0000 | 0.9000 |
| `how_to` | 19 | 19 | 1.0000 | 0.4474 | 1.0000 | 0.4474 |
| `configuration` | 3 | 3 | 1.0000 | 0.5000 | 1.0000 | 0.5000 |
| `factual` | 7 | 7 | 1.0000 | 0.8571 | 1.0000 | 0.5714 |
| `troubleshooting` | 2 | 2 | 1.0000 | 0.2500 | 1.0000 | 0.2500 |
| `unanswerable` | 5 | 0 | N/A | 1.0000 | 1.0000 | 1.0000 |

## 6. 失败案例

- `q001` route=`default` rank=None reasons=['retrieval_miss'] judge_reason='回答正确指出 create_agent 是高度可配置的 harness 且底层生成 LangGraph graph，引用准确；但未覆盖参考答案中关于 harness 具体涵盖内容（提示词、工具、中间件）以及 LangGraph 持久执行、human-in-the-loop、持久化等能力的关键信息，完整性不足。'
- `q003` route=`default` rank=1 reasons=['correctness=0', 'completeness=0', 'refusal_correct=0'] judge_reason='The answer correctly notes that the provided context lacks the exact Document construction syntax, but the question is answerable per the reference answer. It fails to provide the key API (langchain_core.documents.Document), the constructor usage with page_content and metadata, and the optional id attribute. Thus correctness and completeness are 0, and refusal_correct is 0 because it effectively declines to answer an answerable question. Faithfulness is high because its claims are supported by the context, and citations are mostly accurate but incomplete.'
- `q010` route=`default` rank=None reasons=['refusal_correct=0', 'retrieval_miss'] judge_reason='回答正确描述了Subagents模式的工作方式（主智能体作为supervisor将子智能体作为工具调用、无状态、上下文隔离），引用[S3][S2][S4]准确支持相应结论。但回答对第二部分误判为不可回答，而参考答案明确说明无状态设计导致重复请求仍重复完整流程（如4次调用变8次），这属于可回答内容，因此refusal_correct为0、completeness不足。语言一致、简洁，无编造。'
- `q018` route=`default` rank=1 reasons=['correctness=0', 'completeness=0', 'refusal_correct=0'] judge_reason='模型回答声称上下文无法找到 fetch_documentation 的域名限制机制，但参考答案明确给出了 ALLOWED_DOMAINS 列表和检查逻辑，属于误拒答且遗漏全部关键信息。回答本身忠实于所引上下文，但未回答问题，正确性和完整性均为 0。'
- `q033` route=`default` rank=1 reasons=['correctness=0', 'completeness=0'] judge_reason='回答正确指出可在 Annotation Queues 区域创建单次运行队列，且所有陈述均有上下文支持，引用准确。但回答声称上下文未提供详细创建步骤，而参考答案包含完整步骤；实际上上下文虽未逐条列出，但回答未覆盖参考答案的关键操作流程，导致完整性严重不足。回答未误拒答，语言一致，表述简洁。'
- `q035` route=`default` rank=1 reasons=['correctness=0', 'completeness=0', 'refusal_correct=0'] judge_reason='模型回答拒答了本可回答的问题，未提供参考答案中的关键步骤和 API 调用；虽然其陈述在上下文中可找到支持且引用准确，但未回答问题，因此 correctness、completeness 和 refusal_correct 均为 0。'
- `q040` route=`default` rank=1 reasons=['correctness=0', 'completeness=0', 'refusal_correct=0'] judge_reason='回答正确指出上下文缺少 JWT 校验具体实现，但参考答案实际给出了可回答的关键步骤（Supabase 配置、httpx 调用 /auth/v1/user、返回 identity/email/is_authenticated、保留 @auth.on），模型回答未覆盖这些核心内容，且将可回答问题误判为无法完整回答，属于关键信息遗漏和误拒答。引用均能在上下文中找到支持，无编造。'
- `q041` route=`default` rank=3 reasons=['correctness=0', 'completeness=0', 'refusal_correct=0'] judge_reason='模型回答明确拒答，但问题可回答且参考答案提供了完整的 run 生命周期流程；上下文虽未直接给出完整生命周期，但模型未尝试基于已有信息作答，属于误拒答。回答中引用的上下文信息均准确，但完全遗漏了参考答案的关键步骤和限制条件。'
- `q043` route=`self_query` rank=1 reasons=['correctness=0', 'completeness=0', 'refusal_correct=0'] judge_reason='回答仅复述了上下文中关于 trace 嵌套问题的现象描述，未给出参考答案中的根因（Python < 3.11 contextvars 支持不足）和具体解决方案（升级 Python 或手动传递上下文），且误判为无法回答，属于误拒答。引用 [S1] 虽存在但仅部分支持现象描述，未支持关键结论。'

## 7. 结论

1. 本报告是端到端结果：检索、路由、兄弟合并、生成和语言检查都走生产 `RAGChain`。
2. 实际检索 Hit@5 = 0.9649，MRR@5 = 0.8450。
3. 生成 correctness = 0.7097，faithfulness = 1.0000，completeness = 0.6452，citation = 0.9211，refusal = 0.8871，language = 1.0000。
4. 该结果使用真实检索 context，不能与 gold_docs oracle 结果直接等价比较。
5. 生成端的主要瓶颈是 context 覆盖，而不是幻觉：faithfulness=1.0000，但 completeness=0.6452，7 条可回答样本因检索 context 缺少答案而误拒答。下一轮应优先提升 chunk 召回和上下文覆盖，而不是继续调生成提示词。

## 8. 复现

```powershell
$env:PYTHONPATH="D:\My_rag\src"
$env:HF_HUB_OFFLINE="1"
$env:TRANSFORMERS_OFFLINE="1"
python tests/test_FinalPipeline.py --workers 2 --timeout 180 --restart
```
