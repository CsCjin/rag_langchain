# Router v2 Report：Hybrid + Sibling Chunk Reconstruction

- 日期：2026-11-26
- 测试集：`D:\My_rag\tests\evaluation\qa_set.jsonl`
- 路由来源：`D:\My_rag\tests\evaluation\test_SelfQuery\test_RouterQuery.json`（复用上一轮 router 结果，不重新路由）
- 检索：BM25 + dense 混合，dense=0.7，BM25=0.3
- 向量召回：candidate_k=50
- 粗排：coarse_k=20
- 最终返回：top 5（按 URL 去重）
- Reranker：`BAAI/bge-reranker-v2-m3`
- doc_type 惩罚：`{'changelog': 0.05, 'release': 0.03}`
- 兄弟合并：`True`，window=2，max_chars=3000
- 去重后 catalog：42650 chunks
- 最终精排池：原始命中 chunk + 合并父块，按 URL 去重
- 结果：`D:\My_rag\tests\evaluation\test_router\router_v2_report.json`

## 1. 总体指标（对比上一轮 Router v1）

| k | v1 Hit@k | v2 Hit@k | Δ Hit | v1 MRR@k | v2 MRR@k | Δ MRR | v1 nDCG@k | v2 nDCG@k | Δ nDCG |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.7544 | 0.7544 | +0.0000 | 0.7544 | 0.7544 | +0.0000 | 0.7544 | 0.7544 | +0.0000 |
| 3 | 0.9123 | 0.9298 | +0.0175 | 0.8275 | 0.8363 | +0.0088 | 0.8494 | 0.8605 | +0.0111 |
| 5 | 0.9474 | 0.9649 | +0.0175 | 0.8363 | 0.8450 | +0.0088 | 0.8645 | 0.8756 | +0.0111 |

## 2. 按路由拆分（k=5）

| 路由 | n | v1 Hit@5 | v2 Hit@5 | Δ Hit | v1 MRR@5 | v2 MRR@5 | Δ MRR |
|---|---:|---:|---:|---:|---:|---:|---:|
| `self_query` | 19 | 1.0000 | 1.0000 | +0.0000 | 0.9737 | 0.9737 | +0.0000 |
| `default` | 38 | 0.9211 | 0.9474 | +0.0263 | 0.7675 | 0.7807 | +0.0132 |

## 3. 按语言 / 类型拆分（k=5）

### 按语言

| 分组 | n | v1 Hit@5 | v2 Hit@5 | Δ Hit |
|---|---:|---:|---:|---:|
| `zh` | 36 | 0.9167 | 0.9444 | +0.0278 |
| `en` | 21 | 1.0000 | 1.0000 | +0.0000 |

### 按类型

| 分组 | n | v1 Hit@5 | v2 Hit@5 | Δ Hit |
|---|---:|---:|---:|---:|
| `conceptual` | 11 | 0.7273 | 0.8182 | +0.0909 |
| `metadata_filter` | 15 | 1.0000 | 1.0000 | +0.0000 |
| `how_to` | 19 | 1.0000 | 1.0000 | +0.0000 |
| `configuration` | 3 | 1.0000 | 1.0000 | +0.0000 |
| `factual` | 7 | 1.0000 | 1.0000 | +0.0000 |
| `troubleshooting` | 2 | 1.0000 | 1.0000 | +0.0000 |

## 4. Filter 质量

```text
expected_filter_cases = 15
filter_present = 15
exact_match = 15
field_match = 15
value_match = 15
operator_match = 15
exact_match_rate = 1.0
unexpected_filter_cases = 4
unexpected_filter_ids = ['q023', 'q025', 'q042', 'q043']
invalid_or_failed = 0
```

## 5. must_keep_terms 覆盖率

```text
must_keep_terms_avg = 0.8250208855472014
rewrite_required_avg = 0.8048125633232016
cases_below_1 = 19
```

## 6. 案例变化（Hit@5）

- 修复：q044
- 新增失败：无
- 仍然失败：q001, q010

## 7. 失败与回退

- `q001` type=`conceptual` route=`default` rank=miss search_query='LangChain 里的 create_agent 是什么？它和 LangGraph 是什么关系？' filter=None
- `q010` type=`conceptual` route=`default` rank=miss search_query='LangChain 多智能体系统中的 Subagents 模式是如何工作的？为什么它在重复请求时模型调用次数不会减少？' filter=None

异常样本：0

## 8. 结论

1. v2 的 Hit@5 为 0.9649（v1 0.9474，Δ +0.0175），MRR@5 为 0.8450（Δ +0.0088），nDCG@5 为 0.8756（Δ +0.0111）；Hit@1 与 v1 持平。
2. default 路由组 Hit@5 从 0.9211 提升到 0.9474，MRR@5 从 0.7675 提升到 0.7807；self_query 路由组保持 Hit@5=1.0000。
3. q044 从 v1 未命中提升到 rank 4，q019 保持 rank 1，没有新增失败。
4. q001/q010 仍然失败：q001 的目标 overview 页没有被召回；q010 的 top 1 是同一页面的 JavaScript 版本，Python 目标页没有进入 top 5。
5. Filter 质量保持稳定：15/15 精确匹配；4 条额外 filter 均命中 rank 1；无异常。
6. 最终精排池同时保留原始命中 chunk 和合并后的父块，避免 q019 这类聚焦型问题被父块稀释，同时保留 q044 这类比较型问题的跨 chunk 答案。

## 9. 复现

```powershell
$env:PYTHONPATH="D:\My_rag\src"
$env:HF_HUB_OFFLINE="1"
$env:TRANSFORMERS_OFFLINE="1"
python tests/test_RouterQuery_v2.py
```
