# Router + Rerank Retrieval Report

- 日期：2026-11-25
- 测试集：`D:\My_rag\tests\evaluation\qa_set.jsonl`
- 路由：`src/my_rag/core/router.py`（硬规则，无 LLM）
- 向量召回：`candidate_k=30`
- 最终文档数：top 10（评测口径）
- Reranker：`BAAI/bge-reranker-v2-m3`
- doc_type 惩罚：`{'changelog': 0.05, 'release': 0.03}`
- Self-query 允许字段：路由决定；URL/title 命中时只允许对应单字段，否则按 platform/doc_type 组合
- 结果文件：`D:\My_rag\tests\evaluation\test_SelfQuery\test_RouterQuery.json`

## 1. 路由结果

| 路由 | 样本数 |
|---|---:|
| `self_query` | 19 |
| `default` | 38 |

与 `expected_router` 对比准确率：**1.0000**

> 注：`expected_router` 是围绕当前高置信规则标注的，因此 1.0 只代表规则覆盖验证，不代表对未知问法的泛化准确率。

Self-query 路由样本：

- `q002` signals=['url', 'doc_type:quickstart'], allowed_fields=['url']
- `q023` signals=['platform:javascript'], allowed_fields=['platform']
- `q025` signals=['platform:javascript'], allowed_fields=['platform']
- `q026` signals=['title'], allowed_fields=['title']
- `q037` signals=['title'], allowed_fields=['title']
- `q042` signals=['doc_type:troubleshooting'], allowed_fields=['doc_type']
- `q043` signals=['doc_type:troubleshooting'], allowed_fields=['doc_type']
- `q051` signals=['url'], allowed_fields=['url']
- `q052` signals=['url'], allowed_fields=['url']
- `q053` signals=['url'], allowed_fields=['url']
- `q054` signals=['url'], allowed_fields=['url']
- `q055` signals=['url'], allowed_fields=['url']
- `q056` signals=['url'], allowed_fields=['url']
- `q057` signals=['title'], allowed_fields=['title']
- `q058` signals=['title'], allowed_fields=['title']
- `q059` signals=['title'], allowed_fields=['title']
- `q060` signals=['title'], allowed_fields=['title']
- `q061` signals=['title'], allowed_fields=['title']
- `q062` signals=['title'], allowed_fields=['title']

## 2. 总体检索指标

### Hit@k

| k | penalty baseline | translate baseline | router | Δ router - translate | Δ router - penalty |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.6842 | 0.6316 | 0.7544 | +0.1228 | +0.0702 |
| 3 | 0.8421 | 0.8421 | 0.9123 | +0.0702 | +0.0702 |
| 5 | 0.9123 | 0.8596 | 0.9474 | +0.0877 | +0.0351 |
| 10 | 0.9474 | 0.8947 | 0.9649 | +0.0702 | +0.0175 |

### MRR@k

| k | penalty baseline | translate baseline | router | Δ router - translate | Δ router - penalty |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.6842 | 0.6316 | 0.7544 | +0.1228 | +0.0702 |
| 3 | 0.7602 | 0.7281 | 0.8275 | +0.0994 | +0.0673 |
| 5 | 0.7769 | 0.7325 | 0.8363 | +0.1038 | +0.0594 |
| 10 | 0.7810 | 0.7367 | 0.8382 | +0.1015 | +0.0572 |

### nDCG@k

| k | penalty baseline | translate baseline | router | Δ router - translate | Δ router - penalty |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.6842 | 0.6316 | 0.7544 | +0.1228 | +0.0702 |
| 3 | 0.7815 | 0.7575 | 0.8494 | +0.0919 | +0.0679 |
| 5 | 0.8110 | 0.7651 | 0.8645 | +0.0995 | +0.0535 |
| 10 | 0.8218 | 0.7760 | 0.8698 | +0.0938 | +0.0480 |

## 3. 按路由拆分（k=5）

| 路由 | n | penalty Hit@5 | translate Hit@5 | router Hit@5 | Δ vs translate | Δ vs penalty |
|---|---:|---:|---:|---:|---:|---:|
| `self_query` | 19 | 0.8947 | 0.9474 | 1.0000 | +0.0526 | +0.1053 |
| `default` | 38 | 0.9211 | 0.8158 | 0.9211 | +0.1053 | +0.0000 |

Self-query 路由组（19 条）中，15 条是带明确 title/url 的 metadata_filter 题，另外 4 条是 platform/doc_type 规则命中的普通问题（q023/q025/q042/q043）。

### 按语言拆分（k=5）

| 分组 | n | penalty Hit@5 | translate Hit@5 | router Hit@5 | Δ vs translate | Δ vs penalty |
|---|---:|---:|---:|---:|---:|---:|
| `zh` | 36 | 0.8611 | 0.7778 | 0.9167 | +0.1389 | +0.0556 |
| `en` | 21 | 1.0000 | 1.0000 | 1.0000 | +0.0000 | +0.0000 |

### 按类型拆分（k=5）

| 分组 | n | penalty Hit@5 | translate Hit@5 | router Hit@5 | Δ vs translate | Δ vs penalty |
|---|---:|---:|---:|---:|---:|---:|
| `conceptual` | 11 | 0.7273 | 0.7273 | 0.7273 | +0.0000 | +0.0000 |
| `metadata_filter` | 15 | 0.8667 | 1.0000 | 1.0000 | +0.0000 | +0.1333 |
| `how_to` | 19 | 1.0000 | 0.8947 | 1.0000 | +0.1053 | +0.0000 |
| `configuration` | 3 | 1.0000 | 1.0000 | 1.0000 | +0.0000 | +0.0000 |
| `factual` | 7 | 1.0000 | 0.7143 | 1.0000 | +0.2857 | +0.0000 |
| `troubleshooting` | 2 | 1.0000 | 0.5000 | 1.0000 | +0.5000 | +0.0000 |

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
allowed_field_violations = 0
invalid_or_failed = 0
```

说明：`unexpected_filter_cases` 统计原本 `expected_filter=null` 但 Self-query 仍生成 filter 的样本；`allowed_field_violations` 统计 filter 使用了路由未允许字段的样本。

## 5. must_keep_terms 覆盖率

```text
must_keep_terms_avg = 0.8285296574770259
rewrite_required_avg = 0.8090678824721379
cases_below_1 = 19
```

## 6. 案例变化（Hit@5）

### 6.1 对比 translate_outcome（全量 Self-query）

- 修复：q028, q032, q034, q035, q043
- 新增失败：无
- 仍然失败：q001, q010, q044

### 6.2 对比 penalty baseline（普通检索 + rerank）

- 修复：q026, q057
- 新增失败：无
- 仍然失败：q001, q010, q044

### 6.3 排名变化明细

| id | route | router rank | translate rank | penalty rank |
|---|---|---:|---:|---:|
| `q005` | `default` | 1 | 2 | 1 |
| `q010` | `default` | 9 | 7 | 9 |
| `q011` | `default` | 1 | 2 | 1 |
| `q014` | `default` | 2 | 1 | 2 |
| `q016` | `default` | 2 | 3 | 2 |
| `q018` | `default` | 1 | 2 | 1 |
| `q026` | `self_query` | 1 | 1 | miss |
| `q028` | `default` | 4 | miss | 4 |
| `q032` | `default` | 1 | miss | 1 |
| `q034` | `default` | 1 | miss | 1 |
| `q035` | `default` | 1 | miss | 1 |
| `q038` | `default` | 1 | 2 | 1 |
| `q041` | `default` | 3 | 3 | 2 |
| `q043` | `self_query` | 1 | miss | 1 |
| `q044` | `default` | miss | 10 | miss |
| `q051` | `self_query` | 1 | 1 | 2 |
| `q052` | `self_query` | 1 | 1 | 4 |
| `q056` | `self_query` | 1 | 1 | 5 |
| `q057` | `self_query` | 2 | 2 | 8 |

## 7. 失败与回退

- `q001` type=`conceptual` route=`default` rank=miss signals=[] filter=None
- `q010` type=`conceptual` route=`default` rank=9 signals=[] filter=None
- `q044` type=`conceptual` route=`default` rank=miss signals=[] filter=None

回退到 default 的样本数：0

异常样本数：0

## 8. 结论

1. 路由 + 受限 Self-query + rerank 在总体指标上同时超过两个基线：Hit@1 0.7544、Hit@5 0.9474、Hit@10 0.9649，MRR@5 0.8363。
2. Self-query 路由组（19 条）Hit@5 达到 1.0000，MRR@5 为 0.9737；default 路由组（38 条）Hit@5 为 0.9211，与 penalty 基线持平，说明路由避免了全量 Self-query 在普通问题上的误过滤。
3. 15 条 expected_filter 样本的 filter 全部精确匹配，且没有出现路由允许字段之外的 filter；4 条额外 filter（q023/q025/q042/q043）都命中 rank 1，未造成伤害。
4. 对比全量 Self-query，路由修复了 q028/q032/q034/q035/q043，没有新增失败；对比 penalty 基线，路由修复了 q026/q057。
5. 剩余失败 q001/q010/q044 都是 conceptual 问题，属于 chunk 召回/语义排序问题，不是元数据过滤问题。
6. `expected_router` 准确率 1.0 是规则覆盖验证，下一步应补充边界问法和真实用户问法，并接入 `RAGChain.ask()`。

## 9. 复现

```powershell
$env:PYTHONPATH="D:\My_rag\src"
$env:HF_HUB_OFFLINE="1"
$env:TRANSFORMERS_OFFLINE="1"
python tests/test_RouterQuery.py
```

> 如果 Hugging Face 可访问，可以去掉两个离线环境变量；这里设置它们是为了直接使用本地缓存的 embedding 和 reranker 模型。
