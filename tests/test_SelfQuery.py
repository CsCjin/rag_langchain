import argparse
import json
import math
import os
import re
from collections import defaultdict
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
from my_rag.core.vector_store import load_vector_store
from my_rag.model.embedding import get_embedding_model
from my_rag.model.llm import get_llm
from my_rag.model.reranker import (
    DEFAULT_DOC_TYPE_PENALTIES,
    DEFAULT_MODEL_NAME,
)

DATASET_PATH = PROJECT_ROOT / "tests" / "evaluation" / "qa_set.jsonl"
REPORT_PATH = PROJECT_ROOT / "tests" / "evaluation" / "self_query_report.json"


def load_cases(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


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
                items.sort(key=lambda item: json.dumps(item, ensure_ascii=False, sort_keys=True))
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
    exact = json.dumps(expected_canonical, ensure_ascii=False, sort_keys=True) == json.dumps(
        actual_canonical, ensure_ascii=False, sort_keys=True
    )

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
            if condition[0] == expected_field and condition[2] == expected_value
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


def score_records(records: list[dict[str, Any]], cutoff: int) -> dict[str, float]:
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


def group_records(
    records: list[dict[str, Any]], key: str
) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        groups[str(record[key])].append(record)
    return dict(groups)


def evaluate_case(
    case: dict[str, Any],
    vector_store: Chroma,
    retriever: Any,
    max_k: int,
    candidate_k: int,
    use_rerank: bool,
    penalties: dict[str, float] | None,
) -> dict[str, Any]:
    result: dict[str, Any] = {
        "id": case["id"],
        "question": case["question"],
        "type": case["type"],
        "language": case["language"],
        "relevant_urls": case["relevant_urls"],
        "must_keep_terms": case.get("must_keep_terms", []),
        "rewrite_required": case.get("rewrite_required", False),
        "expected_filter": case.get("expected_filter"),
        "structured_query": None,
        "filter_score": None,
        "effective_top_k": None,
        "must_keep_coverage": 0.0,
        "missing_terms": [],
        "retrieved_urls": [],
        "rank": None,
        "error": None,
    }

    try:
        structured_query = construct_structured_query(retriever, case["question"])
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
        result["structured_query"]["filter"] = metadata_filter
        retrieval_k = (
            min(max_k, structured_query.limit)
            if structured_query.limit is not None
            else max_k
        )
        result["effective_top_k"] = retrieval_k
        candidate_n = max(candidate_k, retrieval_k)

        if use_rerank:
            documents = retrieve_documents_with_rerank(
                vector_store,
                search_query,
                k=retrieval_k,
                candidate_k=candidate_n,
                metadata_filter=metadata_filter,
                doc_type_penalties=penalties,
            )
        else:
            documents = retrieve_documents(
                vector_store,
                search_query,
                k=retrieval_k,
                metadata_filter=metadata_filter,
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
        result["filter_score"] = filter_score(
            case.get("expected_filter"),
            metadata_filter,
        )
    except Exception as exc:
        result["error"] = f"{type(exc).__name__}: {exc}"

    return result


def print_metrics(
    records: list[dict[str, Any]],
    cutoffs: list[int],
    title: str,
) -> None:
    print()
    print(title)
    print(f"{'k':>4} {'Hit@k':>8} {'Recall@k':>10} {'MRR@k':>8} {'nDCG@k':>8}")
    for cutoff in cutoffs:
        metrics = score_records(records, cutoff)
        print(
            f"{cutoff:>4} "
            f"{metrics['hit_rate']:>8.4f} "
            f"{metrics['recall']:>10.4f} "
            f"{metrics['mrr']:>8.4f} "
            f"{metrics['ndcg']:>8.4f}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description="Self-query 评测")
    parser.add_argument("--dataset", type=Path, default=DATASET_PATH)
    parser.add_argument("--cutoffs", default="1,3,4,5,10")
    parser.add_argument("--candidate-k", type=int, default=30)
    parser.add_argument("--no-rerank", action="store_true")
    parser.add_argument("--no-doc-type-penalty", action="store_true")
    parser.add_argument("--ids", default="", help="逗号分隔的 case id，只评测这些样本")
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    args = parser.parse_args()

    cutoffs = sorted({int(value) for value in args.cutoffs.split(",") if value.strip()})
    max_k = max(cutoffs)
    if not args.no_rerank and args.candidate_k < max_k:
        parser.error("--candidate-k 必须大于等于最大 cutoff")

    all_cases = load_cases(args.dataset)
    wanted_ids = {item.strip() for item in args.ids.split(",") if item.strip()}
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
    self_query_retriever = build_self_query_retriever(
        vector_store,
        llm,
        k=args.candidate_k,
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
            self_query_retriever,
            max_k,
            args.candidate_k,
            use_rerank,
            penalties,
        )
        records.append(record)
        print(
            f"  [{index:02d}/{len(cases)}] {record['id']} "
            f"rank={record['rank']} coverage={record['must_keep_coverage']:.2f} "
            f"error={record['error'] or '-'}"
        )

    print_metrics(records, cutoffs, "Overall self-query retrieval")
    print_metrics(
        [record for record in records if record["type"] == "metadata_filter"],
        cutoffs,
        "Self-query retrieval: metadata_filter",
    )
    print_metrics(
        [record for record in records if record["language"] == "zh"],
        cutoffs,
        "Self-query retrieval: Chinese",
    )

    filter_cases = [
        record
        for record in records
        if record["expected_filter"] is not None
    ]
    filter_exact = sum(
        1 for record in filter_cases
        if record["filter_score"] and record["filter_score"]["exact"]
    )
    filter_field = sum(
        1 for record in filter_cases
        if record["filter_score"] and record["filter_score"]["field_match"]
    )
    filter_value = sum(
        1 for record in filter_cases
        if record["filter_score"] and record["filter_score"]["value_match"]
    )
    filter_operator = sum(
        1 for record in filter_cases
        if record["filter_score"] and record["filter_score"]["operator_match"]
    )
    filter_present = sum(
        1 for record in filter_cases
        if record["filter_score"] and record["filter_score"]["actual"] is not None
    )
    invalid_filters = sum(1 for record in records if record["error"])

    coverage_values = [record["must_keep_coverage"] for record in records]
    coverage_required = [
        record["must_keep_coverage"]
        for record in records
        if record["rewrite_required"]
    ]
    unexpected_filters = sum(
        1
        for record in records
        if record["expected_filter"] is None
        and record["filter_score"]
        and record["filter_score"]["actual"] is not None
    )

    filter_summary = {
        "expected_filter_cases": len(filter_cases),
        "filter_present": filter_present,
        "exact_match": filter_exact,
        "field_match": filter_field,
        "value_match": filter_value,
        "operator_match": filter_operator,
        "exact_match_rate": filter_exact / len(filter_cases) if filter_cases else 0.0,
        "invalid_or_failed": invalid_filters,
        "unexpected_filter_cases": unexpected_filters,
    }
    coverage_summary = {
        "must_keep_terms_avg": sum(coverage_values) / len(coverage_values) if coverage_values else 0.0,
        "rewrite_required_avg": sum(coverage_required) / len(coverage_required) if coverage_required else 0.0,
        "cases_below_1": sum(1 for value in coverage_values if value < 1.0),
    }

    print()
    print("Filter:", filter_summary)
    print("Must-keep coverage:", coverage_summary)

    report = {
        "config": {
            "dataset": str(args.dataset),
            "vector_store": str(VECTOR_STORE_DIR),
            "reranker_model": reranker_model,
            "candidate_k": args.candidate_k if use_rerank else None,
            "rerank_top_n": max_k if use_rerank else None,
            "use_rerank": use_rerank,
            "doc_type_penalties": penalties,
            "cutoffs": cutoffs,
        },
        "summary": {
            "cases": len(records),
            "filter": filter_summary,
            "coverage": coverage_summary,
        },
        "retrieval": {
            str(cutoff): score_records(records, cutoff)
            for cutoff in cutoffs
        },
        "retrieval_metadata_filter": {
            str(cutoff): score_records(
                [record for record in records if record["type"] == "metadata_filter"],
                cutoff,
            )
            for cutoff in cutoffs
        },
        "retrieval_chinese": {
            str(cutoff): score_records(
                [record for record in records if record["language"] == "zh"],
                cutoff,
            )
            for cutoff in cutoffs
        },
        "breakdown_at_5": {
            "type": {
                name: score_records(group, 5)
                for name, group in group_records(records, "type").items()
            },
            "language": {
                name: score_records(group, 5)
                for name, group in group_records(records, "language").items()
            },
        },
        "filter_cases": filter_cases,
        "cases": records,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print()
    print(f"Report written to {args.report}")


if __name__ == "__main__":
    main()
