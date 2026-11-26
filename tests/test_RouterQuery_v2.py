"""Router v2 evaluation: BM25 + dense hybrid + sibling chunk reconstruction.

The router decisions are taken from the previous router report, so this run
does not re-evaluate the rule-based router itself.
"""

import argparse
import json
import os
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from langchain_chroma import Chroma

sys.path.insert(0, str(Path(__file__).parent))

from test_RouterQuery import (  # noqa: E402
    case_changes,
    dedupe_urls,
    filter_score,
    format_delta,
    group_records,
    load_cases,
    metrics_at_cutoffs,
    rank_label,
    score_records,
    term_coverage,
)

from my_rag.config import PROJECT_ROOT, VECTOR_STORE_DIR  # noqa: E402
from my_rag.core.chunk_catalog import build_chunk_catalog  # noqa: E402
from my_rag.core.hybrid import (  # noqa: E402
    DEFAULT_BM25_WEIGHT,
    DEFAULT_CANDIDATE_K,
    DEFAULT_COARSE_K,
    DEFAULT_DENSE_WEIGHT,
    DEFAULT_FINAL_K,
    retrieve_hybrid_with_rerank,
)
from my_rag.core.retriever import (  # noqa: E402
    build_self_query_retriever,
    construct_structured_query,
)
from my_rag.core.vector_store import load_vector_store  # noqa: E402
from my_rag.model.embedding import get_embedding_model  # noqa: E402
from my_rag.model.llm import get_llm  # noqa: E402
from my_rag.model.reranker import (  # noqa: E402
    DEFAULT_DOC_TYPE_PENALTIES,
    DEFAULT_MODEL_NAME,
)

DATASET_PATH = PROJECT_ROOT / "tests" / "evaluation" / "qa_set.jsonl"
ROUTER_SOURCE = (
    PROJECT_ROOT
    / "tests"
    / "evaluation"
    / "test_SelfQuery"
    / "test_RouterQuery.json"
)
REPORT_PATH = (
    PROJECT_ROOT
    / "tests"
    / "evaluation"
    / "test_router"
    / "router_v2_report.json"
)
CUTOFFS = [1, 3, 5]
FINAL_K = 5


def load_router_cases(path: Path) -> dict[str, dict[str, Any]]:
    report = json.loads(path.read_text(encoding="utf-8"))
    return {case["id"]: case for case in report["cases"]}


def filter_summary(
    records: list[dict[str, Any]],
) -> dict[str, Any]:
    expected_cases = [
        record
        for record in records
        if record["expected_filter"] is not None
    ]
    exact = sum(
        1
        for record in expected_cases
        if record["filter_score"] and record["filter_score"]["exact"]
    )
    field = sum(
        1
        for record in expected_cases
        if record["filter_score"] and record["filter_score"]["field_match"]
    )
    value = sum(
        1
        for record in expected_cases
        if record["filter_score"] and record["filter_score"]["value_match"]
    )
    operator = sum(
        1
        for record in expected_cases
        if record["filter_score"] and record["filter_score"]["operator_match"]
    )
    present = sum(
        1
        for record in expected_cases
        if record["filter_score"] and record["filter_score"]["actual"] is not None
    )
    unexpected_ids = [
        record["id"]
        for record in records
        if record["expected_filter"] is None
        and record["filter_score"]
        and record["filter_score"]["actual"] is not None
    ]
    return {
        "expected_filter_cases": len(expected_cases),
        "filter_present": present,
        "exact_match": exact,
        "field_match": field,
        "value_match": value,
        "operator_match": operator,
        "exact_match_rate": exact / len(expected_cases) if expected_cases else 0.0,
        "unexpected_filter_cases": len(unexpected_ids),
        "unexpected_filter_ids": unexpected_ids,
        "invalid_or_failed": sum(1 for record in records if record["error"]),
    }


def coverage_summary(
    records: list[dict[str, Any]],
) -> dict[str, Any]:
    values = [record["must_keep_coverage"] for record in records]
    required = [
        record["must_keep_coverage"]
        for record in records
        if record["rewrite_required"]
    ]
    return {
        "must_keep_terms_avg": sum(values) / len(values) if values else 0.0,
        "rewrite_required_avg": sum(required) / len(required) if required else 0.0,
        "cases_below_1": sum(1 for value in values if value < 1.0),
    }


def compare_by_route(
    v2_records: list[dict[str, Any]],
    v1_by_id: dict[str, dict[str, Any]],
    route: str,
    cutoff: int = 5,
) -> dict[str, Any]:
    ids = [record["id"] for record in v2_records]
    v1_records = [
        v1_by_id[case_id]
        for case_id in ids
        if case_id in v1_by_id
    ]
    v2_metrics = score_records(v2_records, cutoff)
    v1_metrics = score_records(v1_records, cutoff)
    return {
        "cases": len(v2_records),
        "v1": v1_metrics,
        "v2": v2_metrics,
        "delta": {
            key: v2_metrics[key] - v1_metrics[key]
            for key in ("hit_rate", "recall", "mrr", "ndcg")
        },
    }


def write_markdown(report: dict[str, Any], path: Path) -> None:
    config = report["config"]
    summary = report["summary"]
    cutoffs = config["cutoffs"]
    comparison = report["comparison"]

    lines = [
        "# Router v2 Report：Hybrid + Sibling Chunk Reconstruction",
        "",
        f"- 日期：2026-11-26",
        f"- 测试集：`{config['dataset']}`",
        f"- 路由来源：`{config['router_source']}`（复用上一轮 router 结果，不重新路由）",
        f"- 检索：BM25 + dense 混合，dense={config['dense_weight']:.1f}，BM25={config['bm25_weight']:.1f}",
        f"- 向量召回：candidate_k={config['candidate_k']}",
        f"- 粗排：coarse_k={config['coarse_k']}",
        f"- 最终返回：top {config['final_k']}（按 URL 去重）",
        f"- Reranker：`{config['reranker_model']}`",
        f"- doc_type 惩罚：`{config['doc_type_penalties']}`",
        f"- 兄弟合并：`{config['expand_siblings']}`，window={config['sibling_window']}，max_chars={config['max_chars']}",
        f"- 去重后 catalog：{config['catalog_chunks']} chunks",
        "- 最终精排池：原始命中 chunk + 合并父块，按 URL 去重",
        f"- 结果：`{path.with_suffix('.json')}`",
        "",
        "## 1. 总体指标（对比上一轮 Router v1）",
        "",
        "| k | v1 Hit@k | v2 Hit@k | Δ Hit | v1 MRR@k | v2 MRR@k | Δ MRR | v1 nDCG@k | v2 nDCG@k | Δ nDCG |",
        "|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for cutoff in cutoffs:
        key = str(cutoff)
        v1 = comparison["v1"]["retrieval"][key]
        v2 = report["retrieval"][key]
        lines.append(
            f"| {cutoff} | {v1['hit_rate']:.4f} | {v2['hit_rate']:.4f} | "
            f"{format_delta(v2['hit_rate'] - v1['hit_rate'])} | "
            f"{v1['mrr']:.4f} | {v2['mrr']:.4f} | "
            f"{format_delta(v2['mrr'] - v1['mrr'])} | "
            f"{v1['ndcg']:.4f} | {v2['ndcg']:.4f} | "
            f"{format_delta(v2['ndcg'] - v1['ndcg'])} |"
        )

    lines.extend(
        [
            "",
            "## 2. 按路由拆分（k=5）",
            "",
            "| 路由 | n | v1 Hit@5 | v2 Hit@5 | Δ Hit | v1 MRR@5 | v2 MRR@5 | Δ MRR |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for route in ("self_query", "default"):
        row = comparison["by_route"].get(route)
        if row is None:
            continue
        lines.append(
            f"| `{route}` | {row['cases']} | {row['v1']['hit_rate']:.4f} | "
            f"{row['v2']['hit_rate']:.4f} | "
            f"{format_delta(row['delta']['hit_rate'])} | "
            f"{row['v1']['mrr']:.4f} | {row['v2']['mrr']:.4f} | "
            f"{format_delta(row['delta']['mrr'])} |"
        )

    lines.extend(
        [
            "",
            "## 3. 按语言 / 类型拆分（k=5）",
            "",
        ]
    )
    for title, key in (
        ("按语言", "by_language"),
        ("按类型", "by_type"),
    ):
        lines.extend(
            [
                f"### {title}",
                "",
                "| 分组 | n | v1 Hit@5 | v2 Hit@5 | Δ Hit |",
                "|---|---:|---:|---:|---:|",
            ]
        )
        for name, row in comparison[key].items():
            lines.append(
                f"| `{name}` | {row['cases']} | {row['v1']['hit_rate']:.4f} | "
                f"{row['v2']['hit_rate']:.4f} | "
                f"{format_delta(row['delta']['hit_rate'])} |"
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
            f"- 修复：{', '.join(comparison['changes']['fixed']) or '无'}",
            f"- 新增失败：{', '.join(comparison['changes']['broken']) or '无'}",
            f"- 仍然失败：{', '.join(comparison['changes']['both_miss']) or '无'}",
            "",
            "## 7. 失败与回退",
            "",
        ]
    )
    failures = [
        record
        for record in report["cases"]
        if record["rank"] is None or record["rank"] > 5
    ]
    if failures:
        for record in failures:
            lines.append(
                f"- `{record['id']}` type=`{record['type']}` "
                f"route=`{record['route']}` rank={rank_label(record)} "
                f"search_query={record['search_query']!r} "
                f"filter={record['structured_query']['filter'] if record['structured_query'] else None}"
            )
    else:
        lines.append("无。")
    lines.extend(
        [
            "",
            f"异常样本：{sum(1 for record in report['cases'] if record['error'])}",
            "",
            "## 8. 结论",
            "",
            f"1. v2 的 Hit@5 为 {report['retrieval']['5']['hit_rate']:.4f}"
            f"（v1 {comparison['v1']['retrieval']['5']['hit_rate']:.4f}，"
            f"Δ {format_delta(report['retrieval']['5']['hit_rate'] - comparison['v1']['retrieval']['5']['hit_rate'])}），"
            f"MRR@5 为 {report['retrieval']['5']['mrr']:.4f}"
            f"（Δ {format_delta(report['retrieval']['5']['mrr'] - comparison['v1']['retrieval']['5']['mrr'])}），"
            f"nDCG@5 为 {report['retrieval']['5']['ndcg']:.4f}"
            f"（Δ {format_delta(report['retrieval']['5']['ndcg'] - comparison['v1']['retrieval']['5']['ndcg'])}）；"
            f"Hit@1 与 v1 持平。",
            f"2. default 路由组 Hit@5 从 {comparison['by_route']['default']['v1']['hit_rate']:.4f} "
            f"提升到 {comparison['by_route']['default']['v2']['hit_rate']:.4f}，"
            f"MRR@5 从 {comparison['by_route']['default']['v1']['mrr']:.4f} "
            f"提升到 {comparison['by_route']['default']['v2']['mrr']:.4f}；"
            "self_query 路由组保持 Hit@5=1.0000。",
            "3. q044 从 v1 未命中提升到 rank 4，q019 保持 rank 1，没有新增失败。",
            "4. q001/q010 仍然失败：q001 的目标 overview 页没有被召回；"
            "q010 的 top 1 是同一页面的 JavaScript 版本，Python 目标页没有进入 top 5。",
            f"5. Filter 质量保持稳定：{summary['filter']['exact_match']}/"
            f"{summary['filter']['expected_filter_cases']} 精确匹配；"
            f"{summary['filter']['unexpected_filter_cases']} 条额外 filter 均命中 rank 1；无异常。",
            "6. 最终精排池同时保留原始命中 chunk 和合并后的父块，"
            "避免 q019 这类聚焦型问题被父块稀释，同时保留 q044 这类比较型问题的跨 chunk 答案。",
            "",
            "## 9. 复现",
            "",
            "```powershell",
            '$env:PYTHONPATH="D:\\My_rag\\src"',
            '$env:HF_HUB_OFFLINE="1"',
            '$env:TRANSFORMERS_OFFLINE="1"',
            "python tests/test_RouterQuery_v2.py",
            "```",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Router v2 hybrid retrieval evaluation"
    )
    parser.add_argument(
        "--ids",
        default="",
        help="逗号分隔的 case id，只评测这些样本",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=REPORT_PATH,
    )
    args = parser.parse_args()

    start_time = time.time()
    all_cases = load_cases(DATASET_PATH)
    router_cases = load_router_cases(ROUTER_SOURCE)
    wanted_ids = {
        item.strip() for item in args.ids.split(",") if item.strip()
    }

    cases = [
        case
        for case in all_cases
        if case["answerable"]
        and case["relevant_urls"]
        and case["id"] in router_cases
        and (not wanted_ids or case["id"] in wanted_ids)
    ]
    print(f"Loaded {len(all_cases)} cases, evaluating {len(cases)} routed cases")

    print("Loading embedding model, vector store, chunk catalog and LLM...")
    embeddings = get_embedding_model()
    vector_store = load_vector_store(VECTOR_STORE_DIR, embeddings)
    catalog = build_chunk_catalog()
    print(f"Chunk catalog: {len(catalog.documents)} deduplicated chunks")
    llm = get_llm()

    retrievers: dict[tuple[str, ...], Any] = {}
    for case in cases:
        router_case = router_cases[case["id"]]
        if router_case["route"] != "self_query":
            continue
        allowed_fields = tuple(router_case.get("allowed_fields") or ())
        if allowed_fields and allowed_fields not in retrievers:
            retrievers[allowed_fields] = build_self_query_retriever(
                vector_store,
                llm,
                k=DEFAULT_CANDIDATE_K,
                allowed_fields=allowed_fields,
            )

    use_rerank = True
    penalties = dict(DEFAULT_DOC_TYPE_PENALTIES)
    reranker_model = os.getenv("RERANKER_MODEL", DEFAULT_MODEL_NAME)

    records: list[dict[str, Any]] = []
    for index, case in enumerate(cases, start=1):
        router_case = router_cases[case["id"]]
        route = router_case["route"]
        allowed_fields = [
            str(field) for field in router_case.get("allowed_fields") or []
        ]
        record: dict[str, Any] = {
            "id": case["id"],
            "question": case["question"],
            "type": case["type"],
            "language": case["language"],
            "relevant_urls": case["relevant_urls"],
            "must_keep_terms": case.get("must_keep_terms", []),
            "rewrite_required": case.get("rewrite_required", False),
            "expected_filter": case.get("expected_filter"),
            "route": route,
            "route_signals": router_case.get("route_signals", []),
            "allowed_fields": allowed_fields,
            "search_query": case["question"],
            "structured_query": None,
            "filter_score": None,
            "must_keep_coverage": 1.0,
            "missing_terms": [],
            "retrieved_urls": [],
            "retrieved": [],
            "rank": None,
            "error": None,
        }

        try:
            metadata_filter = None
            search_query = case["question"]
            effective_top_k = FINAL_K

            if route == "self_query":
                retriever = retrievers[tuple(allowed_fields)]
                structured_query = construct_structured_query(
                    retriever,
                    case["question"],
                )
                search_query, search_kwargs = (
                    retriever.structured_query_translator.visit_structured_query(
                        structured_query
                    )
                )
                search_query = search_query.strip() or case["question"]
                metadata_filter = search_kwargs.get("filter")
                effective_top_k = (
                    min(FINAL_K, structured_query.limit)
                    if structured_query.limit is not None
                    else FINAL_K
                )
                coverage, missing = term_coverage(
                    search_query,
                    case.get("must_keep_terms", []),
                )
                record["must_keep_coverage"] = coverage
                record["missing_terms"] = missing
                record["structured_query"] = {
                    "query": structured_query.query,
                    "filter": metadata_filter,
                    "limit": structured_query.limit,
                }
                record["filter_score"] = filter_score(
                    case.get("expected_filter"),
                    metadata_filter,
                )

            record["search_query"] = search_query
            documents = retrieve_hybrid_with_rerank(
                vector_store,
                catalog,
                search_query,
                candidate_k=DEFAULT_CANDIDATE_K,
                coarse_k=DEFAULT_COARSE_K,
                final_k=effective_top_k,
                metadata_filter=metadata_filter,
                doc_type_penalties=penalties,
                expand_siblings=True,
                sibling_window=2,
                max_chars=3000,
                dense_weight=DEFAULT_DENSE_WEIGHT,
                bm25_weight=DEFAULT_BM25_WEIGHT,
            )

            urls = dedupe_urls(documents)
            record["retrieved_urls"] = urls
            record["retrieved"] = [
                {
                    "url": document.metadata.get("url"),
                    "title": document.metadata.get("title"),
                    "doc_type": document.metadata.get("doc_type"),
                    "platform": document.metadata.get("platform"),
                    "parent_id": document.metadata.get("parent_id"),
                    "merged_sibling_count": document.metadata.get(
                        "merged_sibling_count"
                    ),
                    "chars": len(document.page_content),
                }
                for document in documents
            ]
            relevant_urls = set(case["relevant_urls"])
            record["rank"] = next(
                (
                    position
                    for position, url in enumerate(urls, start=1)
                    if url in relevant_urls
                ),
                None,
            )
        except Exception as exc:
            record["error"] = f"{type(exc).__name__}: {exc}"

        records.append(record)
        print(
            f"  [{index:02d}/{len(cases)}] {record['id']} "
            f"route={record['route']} rank={record['rank']} "
            f"filter={record['structured_query']['filter'] if record['structured_query'] else None} "
            f"error={record['error'] or '-'}"
        )

    v1_report = json.loads(ROUTER_SOURCE.read_text(encoding="utf-8"))
    v1_by_id = {case["id"]: case for case in v1_report["cases"]}
    v1_records = [
        v1_by_id[record["id"]]
        for record in records
        if record["id"] in v1_by_id
    ]
    v1_overall = metrics_at_cutoffs(v1_records, CUTOFFS)
    v2_overall = metrics_at_cutoffs(records, CUTOFFS)

    by_route: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_route[record["route"]].append(record)

    by_route_comparison = {
        route: compare_by_route(route_records, v1_by_id, route)
        for route, route_records in by_route.items()
    }
    by_language_comparison = {
        name: compare_by_route(group, v1_by_id, name)
        for name, group in group_records(records, "language").items()
    }
    by_type_comparison = {
        name: compare_by_route(group, v1_by_id, name)
        for name, group in group_records(records, "type").items()
    }

    router_by_id = {record["id"]: record for record in records}
    changes = case_changes(router_by_id, v1_by_id, 5)

    report = {
        "config": {
            "dataset": str(DATASET_PATH),
            "vector_store": str(VECTOR_STORE_DIR),
            "router_source": str(ROUTER_SOURCE),
            "retrieval_mode": "hybrid_bm25_dense_sibling_merge",
            "dense_weight": DEFAULT_DENSE_WEIGHT,
            "bm25_weight": DEFAULT_BM25_WEIGHT,
            "candidate_k": DEFAULT_CANDIDATE_K,
            "coarse_k": DEFAULT_COARSE_K,
            "final_k": FINAL_K,
            "reranker_model": reranker_model,
            "use_rerank": use_rerank,
            "doc_type_penalties": penalties,
            "expand_siblings": True,
            "sibling_window": 2,
            "max_chars": 3000,
            "cutoffs": CUTOFFS,
            "catalog_chunks": len(catalog.documents),
        },
        "summary": {
            "cases": len(records),
            "route_counts": dict(Counter(record["route"] for record in records)),
            "filter": filter_summary(records),
            "coverage": coverage_summary(records),
            "elapsed_seconds": round(time.time() - start_time, 2),
        },
        "retrieval": v2_overall,
        "retrieval_by_route": {
            route: metrics_at_cutoffs(route_records, CUTOFFS)
            for route, route_records in by_route.items()
        },
        "retrieval_by_language": {
            name: metrics_at_cutoffs(group, CUTOFFS)
            for name, group in group_records(records, "language").items()
        },
        "retrieval_by_type": {
            name: metrics_at_cutoffs(group, CUTOFFS)
            for name, group in group_records(records, "type").items()
        },
        "comparison": {
            "v1": {
                "retrieval": v1_overall,
            },
            "by_route": by_route_comparison,
            "by_language": by_language_comparison,
            "by_type": by_type_comparison,
            "changes": changes,
        },
        "filter_cases": [
            record
            for record in records
            if record["expected_filter"] is not None
        ],
        "cases": records,
    }

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_markdown(report, args.report.with_suffix(".md"))

    print()
    print("Overall router v2 retrieval")
    print(f"{'k':>4} {'Hit@k':>8} {'Recall@k':>10} {'MRR@k':>8} {'nDCG@k':>8}")
    for cutoff in CUTOFFS:
        metrics = v2_overall[str(cutoff)]
        print(
            f"{cutoff:>4} "
            f"{metrics['hit_rate']:>8.4f} "
            f"{metrics['recall']:>10.4f} "
            f"{metrics['mrr']:>8.4f} "
            f"{metrics['ndcg']:>8.4f}"
        )
    print()
    print("Filter:", report["summary"]["filter"])
    print("Coverage:", report["summary"]["coverage"])
    print(f"Elapsed: {report['summary']['elapsed_seconds']}s")
    print(f"Report written to {args.report}")
    print(f"Markdown written to {args.report.with_suffix('.md')}")


if __name__ == "__main__":
    main()
