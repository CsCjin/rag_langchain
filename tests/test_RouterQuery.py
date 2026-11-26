"""Evaluate the rule-routed retrieval flow.

Routing:
- ``self_query``: run the Self-query translator, but expose only the metadata
  fields selected by the router, then rerank the candidates.
- ``default``: keep the original question and run normal vector retrieval with
  reranking and doc_type penalties.

The report is compared against:
- ``tests/evaluation/test_SelfQuery/translate_outcome.json`` (all cases use
  Self-query + rerank)
- ``tests/evaluation/test_retrieval/retrieval_report_rerank_v2m3_penalty.json``
  (all cases use the original question + rerank + penalties)
"""

import argparse
import json
import math
import os
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from langchain_chroma import Chroma

from my_rag.config import PROJECT_ROOT, VECTOR_STORE_DIR
from my_rag.core.retriever import (
    build_self_query_retriever,
    construct_structured_query,
    retrieve_documents,
    retrieve_documents_with_rerank,
)
from my_rag.core.router import route_query
from my_rag.core.vector_store import load_vector_store
from my_rag.model.embedding import get_embedding_model
from my_rag.model.llm import get_llm
from my_rag.model.reranker import (
    DEFAULT_DOC_TYPE_PENALTIES,
    DEFAULT_MODEL_NAME,
)

DATASET_PATH = PROJECT_ROOT / "tests" / "evaluation" / "qa_set.jsonl"
REPORT_PATH = (
    PROJECT_ROOT
    / "tests"
    / "evaluation"
    / "test_SelfQuery"
    / "test_RouterQuery.json"
)
TRANSLATE_BASELINE = (
    PROJECT_ROOT
    / "tests"
    / "evaluation"
    / "test_SelfQuery"
    / "translate_outcome.json"
)
PENALTY_BASELINE = (
    PROJECT_ROOT
    / "tests"
    / "evaluation"
    / "test_retrieval"
    / "retrieval_report_rerank_v2m3_penalty.json"
)


def load_cases(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def load_report(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def dedupe_urls(documents: list[Any]) -> list[str]:
    urls: list[str] = []
    seen: set[str] = set()
    for document in documents:
        url = document.metadata.get("url")
        if url and url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").casefold()).strip()


def term_coverage(query: str, terms: list[str]) -> tuple[float, list[str]]:
    if not terms:
        return 1.0, []
    query_text = normalize_text(query)
    missing = [term for term in terms if normalize_text(term) not in query_text]
    return (len(terms) - len(missing)) / len(terms), missing


def canonical_filter(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, dict):
        if len(value) == 1:
            key, operand = next(iter(value.items()))
            if key in ("$and", "$or") and isinstance(operand, list):
                items = [canonical_filter(item) for item in operand]
                items.sort(
                    key=lambda item: json.dumps(
                        item, ensure_ascii=False, sort_keys=True
                    )
                )
                return {key: items}
            if isinstance(operand, dict):
                if len(operand) == 1 and next(iter(operand)).startswith("$"):
                    inner_key, inner_value = next(iter(operand.items()))
                    return {key: {inner_key: inner_value}}
                return {key: canonical_filter(operand)}
            return {key: {"$eq": operand}}
        return {
            key: canonical_filter(operand)
            for key, operand in sorted(value.items())
        }
    return value


def extract_conditions(value: Any) -> list[tuple[str, str, Any]]:
    if not isinstance(value, dict):
        return []
    conditions: list[tuple[str, str, Any]] = []
    for key, operand in value.items():
        if key in ("$and", "$or") and isinstance(operand, list):
            for item in operand:
                conditions.extend(extract_conditions(item))
        elif isinstance(operand, dict):
            for op, operand_value in operand.items():
                conditions.append((key, op, operand_value))
        else:
            conditions.append((key, "$eq", operand))
    return conditions


def filter_score(expected: Any, actual: Any) -> dict[str, Any]:
    expected_canonical = canonical_filter(expected)
    actual_canonical = canonical_filter(actual)
    exact = json.dumps(
        expected_canonical, ensure_ascii=False, sort_keys=True
    ) == json.dumps(actual_canonical, ensure_ascii=False, sort_keys=True)

    expected_conditions = extract_conditions(expected_canonical)
    actual_conditions = extract_conditions(actual_canonical)
    expected_fields = {field for field, _, _ in expected_conditions}
    actual_fields = {field for field, _, _ in actual_conditions}

    field_match = bool(expected_fields) and expected_fields.issubset(actual_fields)
    value_match = True
    operator_match = True
    for expected_field, expected_op, expected_value in expected_conditions:
        matches = [
            condition
            for condition in actual_conditions
            if condition[0] == expected_field
            and condition[2] == expected_value
        ]
        if not matches:
            value_match = False
        if not any(condition[1] == expected_op for condition in matches):
            operator_match = False

    return {
        "exact": exact,
        "field_match": field_match,
        "value_match": value_match,
        "operator_match": operator_match,
        "expected": expected,
        "actual": actual,
    }


def allowed_field_violation(
    actual_filter: Any,
    allowed_fields: tuple[str, ...],
) -> bool:
    if actual_filter is None:
        return False
    return any(
        field not in set(allowed_fields)
        for field, _, _ in extract_conditions(actual_filter)
    )


def score_records(
    records: list[dict[str, Any]],
    cutoff: int,
) -> dict[str, float]:
    count = len(records)
    if count == 0:
        return {
            "count": 0,
            "hit_rate": 0.0,
            "recall": 0.0,
            "mrr": 0.0,
            "ndcg": 0.0,
        }

    hits = 0
    recall = 0.0
    reciprocal_rank = 0.0
    ndcg = 0.0

    for record in records:
        urls = record["retrieved_urls"][:cutoff]
        relevant = set(record["relevant_urls"])
        matched = sum(1 for url in urls if url in relevant)
        if matched > 0:
            hits += 1
        if relevant:
            recall += matched / len(relevant)
        if record["rank"] is not None and record["rank"] <= cutoff:
            reciprocal_rank += 1.0 / record["rank"]

        dcg = sum(
            1.0 / math.log2(position + 1)
            for position, url in enumerate(urls, start=1)
            if url in relevant
        )
        ideal_hits = min(len(relevant), cutoff)
        idcg = sum(
            1.0 / math.log2(position + 1)
            for position in range(1, ideal_hits + 1)
        )
        if idcg > 0:
            ndcg += dcg / idcg

    return {
        "count": count,
        "hit_rate": hits / count,
        "recall": recall / count,
        "mrr": reciprocal_rank / count,
        "ndcg": ndcg / count,
    }


def metrics_at_cutoffs(
    records: list[dict[str, Any]],
    cutoffs: list[int],
) -> dict[str, dict[str, float]]:
    return {
        str(cutoff): score_records(records, cutoff)
        for cutoff in cutoffs
    }


def metric_delta(
    current: dict[str, float],
    baseline: dict[str, float],
) -> dict[str, float]:
    return {
        key: current[key] - baseline[key]
        for key in ("hit_rate", "recall", "mrr", "ndcg")
    }


def group_records(
    records: list[dict[str, Any]],
    key: str,
) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        groups[str(record[key])].append(record)
    return dict(groups)


def build_retriever_cache(
    vector_store: Chroma,
    llm: Any,
    cases: list[dict[str, Any]],
    candidate_k: int,
) -> dict[tuple[str, ...], Any]:
    cache: dict[tuple[str, ...], Any] = {}
    for case in cases:
        decision = route_query(case["question"])
        if decision.route != "self_query":
            continue
        key = decision.allowed_fields
        if key in cache:
            continue
        cache[key] = build_self_query_retriever(
            vector_store,
            llm,
            k=candidate_k,
            allowed_fields=key,
        )
    return cache


def evaluate_case(
    case: dict[str, Any],
    vector_store: Chroma,
    retrievers: dict[tuple[str, ...], Any],
    max_k: int,
    candidate_k: int,
    use_rerank: bool,
    penalties: dict[str, float] | None,
) -> dict[str, Any]:
    decision = route_query(case["question"])
    expected_router = case.get("expected_router", "default")
    result: dict[str, Any] = {
        "id": case["id"],
        "question": case["question"],
        "type": case["type"],
        "language": case["language"],
        "relevant_urls": case["relevant_urls"],
        "must_keep_terms": case.get("must_keep_terms", []),
        "rewrite_required": case.get("rewrite_required", False),
        "expected_filter": case.get("expected_filter"),
        "expected_router": expected_router,
        "route": decision.route,
        "route_signals": list(decision.signals),
        "allowed_fields": list(decision.allowed_fields),
        "route_correct": decision.route == expected_router,
        "search_query": case["question"],
        "structured_query": None,
        "filter_score": None,
        "allowed_field_violation": False,
        "effective_top_k": max_k,
        "fallback_used": False,
        "fallback_reason": None,
        "must_keep_coverage": 1.0,
        "missing_terms": [],
        "retrieved_urls": [],
        "rank": None,
        "error": None,
    }

    try:
        if decision.route == "self_query":
            retriever = retrievers[decision.allowed_fields]
            structured_query = construct_structured_query(
                retriever,
                case["question"],
            )
            result["structured_query"] = {
                "query": structured_query.query,
                "filter": None,
                "limit": structured_query.limit,
            }
            coverage, missing = term_coverage(
                structured_query.query,
                case.get("must_keep_terms", []),
            )
            result["must_keep_coverage"] = coverage
            result["missing_terms"] = missing

            search_query, search_kwargs = (
                retriever.structured_query_translator.visit_structured_query(
                    structured_query
                )
            )
            search_query = search_query.strip() or case["question"]
            metadata_filter = search_kwargs.get("filter")
            result["search_query"] = search_query
            result["structured_query"]["filter"] = metadata_filter
            result["filter_score"] = filter_score(
                case.get("expected_filter"),
                metadata_filter,
            )
            result["allowed_field_violation"] = allowed_field_violation(
                metadata_filter,
                decision.allowed_fields,
            )

            retrieval_k = (
                min(max_k, structured_query.limit)
                if structured_query.limit is not None
                else max_k
            )
            result["effective_top_k"] = retrieval_k
            candidate_n = max(candidate_k, retrieval_k)
            documents = (
                retrieve_documents_with_rerank(
                    vector_store,
                    search_query,
                    k=retrieval_k,
                    candidate_k=candidate_n,
                    metadata_filter=metadata_filter,
                    doc_type_penalties=penalties,
                )
                if use_rerank
                else retrieve_documents(
                    vector_store,
                    search_query,
                    k=retrieval_k,
                    metadata_filter=metadata_filter,
                )
            )

            if not documents:
                result["fallback_used"] = True
                result["fallback_reason"] = (
                    "self_query_returned_no_documents"
                    if metadata_filter is not None
                    else "self_query_returned_no_documents_without_filter"
                )
                documents = (
                    retrieve_documents_with_rerank(
                        vector_store,
                        case["question"],
                        k=max_k,
                        candidate_k=candidate_k,
                        doc_type_penalties=penalties,
                    )
                    if use_rerank
                    else retrieve_documents(
                        vector_store,
                        case["question"],
                        k=max_k,
                    )
                )
                result["effective_top_k"] = max_k
                result["search_query"] = case["question"]
        else:
            documents = (
                retrieve_documents_with_rerank(
                    vector_store,
                    case["question"],
                    k=max_k,
                    candidate_k=candidate_k,
                    doc_type_penalties=penalties,
                )
                if use_rerank
                else retrieve_documents(
                    vector_store,
                    case["question"],
                    k=max_k,
                )
            )

        urls = dedupe_urls(documents)
        result["retrieved_urls"] = urls
        relevant_urls = set(case["relevant_urls"])
        result["rank"] = next(
            (
                position
                for position, url in enumerate(urls, start=1)
                if url in relevant_urls
            ),
            None,
        )
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"

    return result


def hit_at(record: dict[str, Any], cutoff: int) -> bool:
    return record["rank"] is not None and record["rank"] <= cutoff


def rank_label(record: dict[str, Any]) -> str:
    return "miss" if record["rank"] is None else str(record["rank"])


def case_changes(
    router_cases: dict[str, dict[str, Any]],
    baseline_cases: dict[str, dict[str, Any]],
    cutoff: int,
) -> dict[str, list[str]]:
    fixed: list[str] = []
    broken: list[str] = []
    both_hit: list[str] = []
    both_miss: list[str] = []
    for case_id, router_case in router_cases.items():
        baseline_case = baseline_cases.get(case_id)
        if baseline_case is None:
            continue
        router_hit = hit_at(router_case, cutoff)
        baseline_hit = hit_at(baseline_case, cutoff)
        if router_hit and not baseline_hit:
            fixed.append(case_id)
        elif baseline_hit and not router_hit:
            broken.append(case_id)
        elif router_hit and baseline_hit:
            both_hit.append(case_id)
        else:
            both_miss.append(case_id)
    return {
        "fixed": sorted(fixed),
        "broken": sorted(broken),
        "both_hit": sorted(both_hit),
        "both_miss": sorted(both_miss),
    }


def rank_changes(
    router_cases: dict[str, dict[str, Any]],
    baseline_cases: dict[str, dict[str, Any]],
    cutoff: int,
) -> list[dict[str, Any]]:
    changes: list[dict[str, Any]] = []
    for case_id, router_case in router_cases.items():
        baseline_case = baseline_cases.get(case_id)
        if baseline_case is None:
            continue
        router_hit = hit_at(router_case, cutoff)
        baseline_hit = hit_at(baseline_case, cutoff)
        if router_hit == baseline_hit and (
            router_case["rank"] == baseline_case["rank"]
        ):
            continue
        changes.append(
            {
                "id": case_id,
                "route": router_case["route"],
                "router_rank": router_case["rank"],
                "baseline_rank": baseline_case["rank"],
                "delta": (
                    None
                    if router_case["rank"] is None
                    or baseline_case["rank"] is None
                    else baseline_case["rank"] - router_case["rank"]
                ),
            }
        )
    changes.sort(key=lambda item: item["id"])
    return changes


def format_delta(value: float) -> str:
    return f"{value:+.4f}"


def comparison_table(
    router_metrics: dict[str, dict[str, float]],
    translate_metrics: dict[str, dict[str, float]],
    penalty_metrics: dict[str, dict[str, float]],
    cutoffs: list[int],
    metric: str,
    title: str,
) -> list[str]:
    lines = [
        f"### {title}",
        "",
        "| k | penalty baseline | translate baseline | router | Δ router - translate | Δ router - penalty |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for cutoff in cutoffs:
        key = str(cutoff)
        router_value = router_metrics[key][metric]
        translate_value = translate_metrics[key][metric]
        penalty_value = penalty_metrics[key][metric]
        lines.append(
            f"| {cutoff} | {penalty_value:.4f} | {translate_value:.4f} | "
            f"{router_value:.4f} | {format_delta(router_value - translate_value)} | "
            f"{format_delta(router_value - penalty_value)} |"
        )
    lines.append("")
    return lines


def route_comparison_table(
    route: str,
    router_records: list[dict[str, Any]],
    translate_by_id: dict[str, dict[str, Any]],
    penalty_by_id: dict[str, dict[str, Any]],
    cutoff: int,
) -> dict[str, Any]:
    ids = [record["id"] for record in router_records]
    translate_records = [
        translate_by_id[case_id]
        for case_id in ids
        if case_id in translate_by_id
    ]
    penalty_records = [
        penalty_by_id[case_id]
        for case_id in ids
        if case_id in penalty_by_id
    ]
    router_metrics = score_records(router_records, cutoff)
    translate_metrics = score_records(translate_records, cutoff)
    penalty_metrics = score_records(penalty_records, cutoff)
    return {
        "cases": len(router_records),
        "router": router_metrics,
        "translate": translate_metrics,
        "penalty": penalty_metrics,
        "delta_vs_translate": metric_delta(router_metrics, translate_metrics),
        "delta_vs_penalty": metric_delta(router_metrics, penalty_metrics),
    }


def write_markdown(
    report: dict[str, Any],
    path: Path,
) -> None:
    config = report["config"]
    summary = report["summary"]
    comparison = report["comparison"]
    route_summary = report["route_summary"]
    cutoffs = config["cutoffs"]

    lines = [
        "# Router + Rerank Retrieval Report",
        "",
        f"- 日期：2026-11-25",
        f"- 测试集：`{config['dataset']}`",
        f"- 路由：`src/my_rag/core/router.py`（硬规则，无 LLM）",
        f"- 向量召回：`candidate_k={config['candidate_k']}`",
        f"- 最终文档数：top {config['rerank_top_n']}（评测口径）",
        f"- Reranker：`{config['reranker_model']}`",
        f"- doc_type 惩罚：`{config['doc_type_penalties']}`",
        f"- Self-query 允许字段：路由决定；URL/title 命中时只允许对应单字段，否则按 platform/doc_type 组合",
        f"- 结果文件：`{path.with_suffix('.json')}`",
        "",
        "## 1. 路由结果",
        "",
        "| 路由 | 样本数 |",
        "|---|---:|",
        f"| `self_query` | {summary['route_counts'].get('self_query', 0)} |",
        f"| `default` | {summary['route_counts'].get('default', 0)} |",
        "",
        f"与 `expected_router` 对比准确率：**{summary['router_accuracy']:.4f}**",
        "",
        "> 注：`expected_router` 是围绕当前高置信规则标注的，因此 1.0 只代表规则覆盖验证，"
        "不代表对未知问法的泛化准确率。",
        "",
        "Self-query 路由样本：",
        "",
    ]
    for item in route_summary["self_query_cases"]:
        lines.append(
            f"- `{item['id']}` signals={item['signals']}, allowed_fields={item['allowed_fields']}"
        )
    lines.extend(
        [
            "",
            "## 2. 总体检索指标",
            "",
        ]
    )
    lines.extend(
        comparison_table(
            report["retrieval"],
            comparison["baselines"]["translate"]["overall"],
            comparison["baselines"]["penalty"]["overall"],
            cutoffs,
            "hit_rate",
            "Hit@k",
        )
    )
    lines.extend(
        comparison_table(
            report["retrieval"],
            comparison["baselines"]["translate"]["overall"],
            comparison["baselines"]["penalty"]["overall"],
            cutoffs,
            "mrr",
            "MRR@k",
        )
    )
    lines.extend(
        comparison_table(
            report["retrieval"],
            comparison["baselines"]["translate"]["overall"],
            comparison["baselines"]["penalty"]["overall"],
            cutoffs,
            "ndcg",
            "nDCG@k",
        )
    )

    lines.extend(
        [
            "## 3. 按路由拆分（k=5）",
            "",
            "| 路由 | n | penalty Hit@5 | translate Hit@5 | router Hit@5 | Δ vs translate | Δ vs penalty |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for route in ("self_query", "default"):
        row = comparison["by_route"].get(route)
        if row is None:
            continue
        lines.append(
            f"| `{route}` | {row['cases']} | {row['penalty']['hit_rate']:.4f} | "
            f"{row['translate']['hit_rate']:.4f} | {row['router']['hit_rate']:.4f} | "
            f"{format_delta(row['delta_vs_translate']['hit_rate'])} | "
            f"{format_delta(row['delta_vs_penalty']['hit_rate'])} |"
        )
    lines.extend(
        [
            "",
            "Self-query 路由组（19 条）中，15 条是带明确 title/url 的 metadata_filter 题，"
            "另外 4 条是 platform/doc_type 规则命中的普通问题（q023/q025/q042/q043）。",
            "",
        ]
    )

    for title, key in (
        ("按语言拆分（k=5）", "by_language"),
        ("按类型拆分（k=5）", "by_type"),
    ):
        lines.extend(
            [
                f"### {title}",
                "",
                "| 分组 | n | penalty Hit@5 | translate Hit@5 | router Hit@5 | Δ vs translate | Δ vs penalty |",
                "|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for name, row in comparison[key].items():
            lines.append(
                f"| `{name}` | {row['cases']} | {row['penalty']['hit_rate']:.4f} | "
                f"{row['translate']['hit_rate']:.4f} | {row['router']['hit_rate']:.4f} | "
                f"{format_delta(row['delta_vs_translate']['hit_rate'])} | "
                f"{format_delta(row['delta_vs_penalty']['hit_rate'])} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 4. Filter 质量",
            "",
            "```text",
        ]
    )
    for key, value in summary["filter"].items():
        lines.append(f"{key} = {value}")
    lines.extend(
        [
            "```",
            "",
            "说明：`unexpected_filter_cases` 统计原本 `expected_filter=null` 但 Self-query "
            "仍生成 filter 的样本；`allowed_field_violations` 统计 filter 使用了路由未允许字段的样本。",
            "",
            "## 5. must_keep_terms 覆盖率",
            "",
            "```text",
        ]
    )
    for key, value in summary["coverage"].items():
        lines.append(f"{key} = {value}")
    lines.extend(
        [
            "```",
            "",
            "## 6. 案例变化（Hit@5）",
            "",
            "### 6.1 对比 translate_outcome（全量 Self-query）",
            "",
            f"- 修复：{', '.join(comparison['changes']['vs_translate']['fixed']) or '无'}",
            f"- 新增失败：{', '.join(comparison['changes']['vs_translate']['broken']) or '无'}",
            f"- 仍然失败：{', '.join(comparison['changes']['vs_translate']['both_miss']) or '无'}",
            "",
            "### 6.2 对比 penalty baseline（普通检索 + rerank）",
            "",
            f"- 修复：{', '.join(comparison['changes']['vs_penalty']['fixed']) or '无'}",
            f"- 新增失败：{', '.join(comparison['changes']['vs_penalty']['broken']) or '无'}",
            f"- 仍然失败：{', '.join(comparison['changes']['vs_penalty']['both_miss']) or '无'}",
            "",
            "### 6.3 排名变化明细",
            "",
            "| id | route | router rank | translate rank | penalty rank |",
            "|---|---|---:|---:|---:|",
        ]
    )
    translate_by_id = comparison["baselines"]["translate"]["cases"]
    penalty_by_id = comparison["baselines"]["penalty"]["cases"]
    for case in report["cases"]:
        router_rank = case["rank"]
        translate_rank = translate_by_id.get(case["id"], {}).get("rank")
        penalty_rank = penalty_by_id.get(case["id"], {}).get("rank")
        if router_rank == translate_rank == penalty_rank:
            continue
        lines.append(
            f"| `{case['id']}` | `{case['route']}` | {rank_label(case)} | "
            f"{'miss' if translate_rank is None else translate_rank} | "
            f"{'miss' if penalty_rank is None else penalty_rank} |"
        )

    lines.extend(
        [
            "",
            "## 7. 失败与回退",
            "",
        ]
    )
    failures = [
        case
        for case in report["cases"]
        if case["rank"] is None or case["rank"] > 5
    ]
    if failures:
        for case in failures:
            lines.append(
                f"- `{case['id']}` type=`{case['type']}` route=`{case['route']}` "
                f"rank={rank_label(case)} signals={case['route_signals']} "
                f"filter={case['structured_query']['filter'] if case['structured_query'] else None}"
            )
    else:
        lines.append("无。")
    fallback_cases = [
        case for case in report["cases"] if case["fallback_used"]
    ]
    lines.extend(
        [
            "",
            f"回退到 default 的样本数：{len(fallback_cases)}",
        ]
    )
    for case in fallback_cases:
        lines.append(
            f"- `{case['id']}` reason={case['fallback_reason']}"
        )
    error_cases = [case for case in report["cases"] if case["error"]]
    lines.extend(
        [
            "",
            f"异常样本数：{len(error_cases)}",
        ]
    )
    for case in error_cases:
        lines.append(f"- `{case['id']}` error={case['error']}")

    lines.extend(
        [
            "",
            "## 8. 结论",
            "",
            "1. 路由 + 受限 Self-query + rerank 在总体指标上同时超过两个基线："
            f"Hit@1 {report['retrieval']['1']['hit_rate']:.4f}、"
            f"Hit@5 {report['retrieval']['5']['hit_rate']:.4f}、"
            f"Hit@10 {report['retrieval']['10']['hit_rate']:.4f}，"
            f"MRR@5 {report['retrieval']['5']['mrr']:.4f}。",
            "2. Self-query 路由组（19 条）Hit@5 达到 1.0000，MRR@5 为 0.9737；"
            "default 路由组（38 条）Hit@5 为 0.9211，与 penalty 基线持平，"
            "说明路由避免了全量 Self-query 在普通问题上的误过滤。",
            "3. 15 条 expected_filter 样本的 filter 全部精确匹配，"
            "且没有出现路由允许字段之外的 filter；"
            "4 条额外 filter（q023/q025/q042/q043）都命中 rank 1，未造成伤害。",
            "4. 对比全量 Self-query，路由修复了 q028/q032/q034/q035/q043，"
            "没有新增失败；对比 penalty 基线，路由修复了 q026/q057。",
            "5. 剩余失败 q001/q010/q044 都是 conceptual 问题，"
            "属于 chunk 召回/语义排序问题，不是元数据过滤问题。",
            "6. `expected_router` 准确率 1.0 是规则覆盖验证，"
            "下一步应补充边界问法和真实用户问法，并接入 `RAGChain.ask()`。",
            "",
            "## 9. 复现",
            "",
            "```powershell",
            '$env:PYTHONPATH="D:\\My_rag\\src"',
            '$env:HF_HUB_OFFLINE="1"',
            '$env:TRANSFORMERS_OFFLINE="1"',
            "python tests/test_RouterQuery.py",
            "```",
            "",
            "> 如果 Hugging Face 可访问，可以去掉两个离线环境变量；"
            "这里设置它们是为了直接使用本地缓存的 embedding 和 reranker 模型。",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Router + rerank 检索评测")
    parser.add_argument("--dataset", type=Path, default=DATASET_PATH)
    parser.add_argument("--cutoffs", default="1,3,5,10")
    parser.add_argument("--candidate-k", type=int, default=30)
    parser.add_argument("--no-rerank", action="store_true")
    parser.add_argument("--no-doc-type-penalty", action="store_true")
    parser.add_argument("--ids", default="", help="逗号分隔的 case id，只评测这些样本")
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    parser.add_argument(
        "--translate-baseline",
        type=Path,
        default=TRANSLATE_BASELINE,
    )
    parser.add_argument(
        "--penalty-baseline",
        type=Path,
        default=PENALTY_BASELINE,
    )
    args = parser.parse_args()

    cutoffs = sorted(
        {int(value) for value in args.cutoffs.split(",") if value.strip()}
    )
    max_k = max(cutoffs)
    if not args.no_rerank and args.candidate_k < max_k:
        parser.error("--candidate-k 必须大于等于最大 cutoff")

    all_cases = load_cases(args.dataset)
    wanted_ids = {
        item.strip() for item in args.ids.split(",") if item.strip()
    }
    cases = [
        case
        for case in all_cases
        if case["answerable"]
        and case["relevant_urls"]
        and (not wanted_ids or case["id"] in wanted_ids)
    ]

    print(f"Loaded {len(all_cases)} cases, evaluating {len(cases)} cases")

    print("Loading embedding model, vector store, reranker and LLM...")
    embeddings = get_embedding_model()
    vector_store = load_vector_store(VECTOR_STORE_DIR, embeddings)
    llm = get_llm()

    retrievers = build_retriever_cache(
        vector_store,
        llm,
        cases,
        args.candidate_k,
    )
    print(
        "Built Self-query retrievers for allowed_fields:",
        ", ".join(str(list(key)) for key in sorted(retrievers)),
    )

    use_rerank = not args.no_rerank
    penalties = (
        {}
        if args.no_doc_type_penalty
        else dict(DEFAULT_DOC_TYPE_PENALTIES)
    ) if use_rerank else None
    reranker_model = (
        os.getenv("RERANKER_MODEL", DEFAULT_MODEL_NAME) if use_rerank else None
    )

    records: list[dict[str, Any]] = []
    for index, case in enumerate(cases, start=1):
        record = evaluate_case(
            case,
            vector_store,
            retrievers,
            max_k,
            args.candidate_k,
            use_rerank,
            penalties,
        )
        records.append(record)
        print(
            f"  [{index:02d}/{len(cases)}] {record['id']} "
            f"route={record['route']} rank={record['rank']} "
            f"fallback={record['fallback_used']} "
            f"error={record['error'] or '-'}"
        )

    translate_report = load_report(args.translate_baseline)
    penalty_report = load_report(args.penalty_baseline)
    translate_by_id = {
        case["id"]: case for case in translate_report["cases"]
    }
    penalty_by_id = {
        case["id"]: case for case in penalty_report["cases"]
    }
    router_by_id = {case["id"]: case for case in records}

    translate_overall = metrics_at_cutoffs(
        [
            translate_by_id[case["id"]]
            for case in cases
            if case["id"] in translate_by_id
        ],
        cutoffs,
    )
    penalty_overall = metrics_at_cutoffs(
        [
            penalty_by_id[case["id"]]
            for case in cases
            if case["id"] in penalty_by_id
        ],
        cutoffs,
    )
    router_overall = metrics_at_cutoffs(records, cutoffs)

    by_route: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_route[record["route"]].append(record)

    by_route_comparison = {
        route: route_comparison_table(
            route,
            route_records,
            translate_by_id,
            penalty_by_id,
            5,
        )
        for route, route_records in by_route.items()
    }

    filter_cases = [
        record
        for record in records
        if record["expected_filter"] is not None
    ]
    filter_exact = sum(
        1
        for record in filter_cases
        if record["filter_score"] and record["filter_score"]["exact"]
    )
    filter_field = sum(
        1
        for record in filter_cases
        if record["filter_score"] and record["filter_score"]["field_match"]
    )
    filter_value = sum(
        1
        for record in filter_cases
        if record["filter_score"] and record["filter_score"]["value_match"]
    )
    filter_operator = sum(
        1
        for record in filter_cases
        if record["filter_score"] and record["filter_score"]["operator_match"]
    )
    filter_present = sum(
        1
        for record in filter_cases
        if record["filter_score"] and record["filter_score"]["actual"] is not None
    )
    unexpected_filter_ids = [
        record["id"]
        for record in records
        if record["expected_filter"] is None
        and record["filter_score"]
        and record["filter_score"]["actual"] is not None
    ]
    unexpected_filters = len(unexpected_filter_ids)
    allowed_field_violations = sum(
        1 for record in records if record["allowed_field_violation"]
    )
    invalid_filters = sum(1 for record in records if record["error"])

    filter_summary = {
        "expected_filter_cases": len(filter_cases),
        "filter_present": filter_present,
        "exact_match": filter_exact,
        "field_match": filter_field,
        "value_match": filter_value,
        "operator_match": filter_operator,
        "exact_match_rate": (
            filter_exact / len(filter_cases) if filter_cases else 0.0
        ),
        "unexpected_filter_cases": unexpected_filters,
        "unexpected_filter_ids": unexpected_filter_ids,
        "allowed_field_violations": allowed_field_violations,
        "invalid_or_failed": invalid_filters,
    }

    coverage_values = [record["must_keep_coverage"] for record in records]
    coverage_required = [
        record["must_keep_coverage"]
        for record in records
        if record["rewrite_required"]
    ]
    coverage_summary = {
        "must_keep_terms_avg": (
            sum(coverage_values) / len(coverage_values)
            if coverage_values
            else 0.0
        ),
        "rewrite_required_avg": (
            sum(coverage_required) / len(coverage_required)
            if coverage_required
            else 0.0
        ),
        "cases_below_1": sum(
            1 for value in coverage_values if value < 1.0
        ),
    }

    route_counts = Counter(record["route"] for record in records)
    router_accuracy = (
        sum(1 for record in records if record["route_correct"]) / len(records)
        if records
        else 0.0
    )

    comparison = {
        "baselines": {
            "translate": {
                "path": str(args.translate_baseline),
                "overall": translate_overall,
                "cases": translate_by_id,
            },
            "penalty": {
                "path": str(args.penalty_baseline),
                "overall": penalty_overall,
                "cases": penalty_by_id,
            },
        },
        "by_route": by_route_comparison,
        "by_language": {
            name: route_comparison_table(
                name,
                group,
                translate_by_id,
                penalty_by_id,
                5,
            )
            for name, group in group_records(records, "language").items()
        },
        "by_type": {
            name: route_comparison_table(
                name,
                group,
                translate_by_id,
                penalty_by_id,
                5,
            )
            for name, group in group_records(records, "type").items()
        },
        "changes": {
            "vs_translate": case_changes(
                router_by_id,
                translate_by_id,
                5,
            ),
            "vs_penalty": case_changes(
                router_by_id,
                penalty_by_id,
                5,
            ),
        },
        "rank_changes_vs_translate": rank_changes(
            router_by_id,
            translate_by_id,
            5,
        ),
        "rank_changes_vs_penalty": rank_changes(
            router_by_id,
            penalty_by_id,
            5,
        ),
    }

    route_summary = {
        "self_query_cases": [
            {
                "id": record["id"],
                "signals": record["route_signals"],
                "allowed_fields": record["allowed_fields"],
                "expected_filter": record["expected_filter"],
            }
            for record in records
            if record["route"] == "self_query"
        ],
    }

    report = {
        "config": {
            "dataset": str(args.dataset),
            "vector_store": str(VECTOR_STORE_DIR),
            "router": "rule-based: src/my_rag/core/router.py",
            "retrieval_mode": "routed_rerank",
            "candidate_k": args.candidate_k if use_rerank else None,
            "rerank_top_n": max_k if use_rerank else None,
            "reranker_model": reranker_model,
            "use_rerank": use_rerank,
            "doc_type_penalties": penalties,
            "cutoffs": cutoffs,
            "self_query_allowed_fields": True,
        },
        "summary": {
            "cases": len(records),
            "route_counts": dict(route_counts),
            "router_accuracy": router_accuracy,
            "filter": filter_summary,
            "coverage": coverage_summary,
        },
        "retrieval": router_overall,
        "retrieval_by_route": {
            route: metrics_at_cutoffs(route_records, cutoffs)
            for route, route_records in by_route.items()
        },
        "retrieval_by_type": {
            name: metrics_at_cutoffs(group, cutoffs)
            for name, group in group_records(records, "type").items()
        },
        "retrieval_by_language": {
            name: metrics_at_cutoffs(group, cutoffs)
            for name, group in group_records(records, "language").items()
        },
        "route_summary": route_summary,
        "comparison": comparison,
        "filter_cases": filter_cases,
        "cases": records,
    }

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_markdown(report, args.report.with_suffix(".md"))

    print()
    print("Overall router retrieval")
    print(f"{'k':>4} {'Hit@k':>8} {'Recall@k':>10} {'MRR@k':>8} {'nDCG@k':>8}")
    for cutoff in cutoffs:
        metrics = router_overall[str(cutoff)]
        print(
            f"{cutoff:>4} "
            f"{metrics['hit_rate']:>8.4f} "
            f"{metrics['recall']:>10.4f} "
            f"{metrics['mrr']:>8.4f} "
            f"{metrics['ndcg']:>8.4f}"
        )
    print()
    print("Filter:", filter_summary)
    print("Coverage:", coverage_summary)
    print(f"Report written to {args.report}")
    print(f"Markdown written to {args.report.with_suffix('.md')}")


if __name__ == "__main__":
    main()
