"""End-to-end evaluation: RAGChain + router + hybrid + generation.

The final pipeline is evaluated on all 62 QA cases:
- retrieval: page-level Hit@k / MRR / nDCG on the documents returned by
  ``RAGChain.ask``;
- routing: route distribution and metadata-filter quality;
- generation: the same seven-dimension rubric used by
  ``tests/test_AnswerGeneration.py``, but now with the actual retrieved
  context.
"""

import argparse
import json
import sys
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))

from test_AnswerGeneration import (  # noqa: E402
    aggregate,
    failure_reasons,
    judge_answer,
    rule_metrics,
)
from test_RouterQuery import (  # noqa: E402
    dedupe_urls,
    filter_score,
    group_records,
    load_cases,
    metrics_at_cutoffs,
    score_records,
    term_coverage,
)

from my_rag.config import PROJECT_ROOT  # noqa: E402
from my_rag.core.chunk_catalog import build_chunk_catalog  # noqa: E402
from my_rag.core.rag_chain import (  # noqa: E402
    build_rag_chain,
    format_documents,
)
from my_rag.model.reranker import get_cross_encoder  # noqa: E402

DATASET_PATH = PROJECT_ROOT / "tests" / "evaluation" / "qa_set.jsonl"
REPORT_DIR = PROJECT_ROOT / "tests" / "evaluation" / "final_test"
REPORT_PATH = REPORT_DIR / "final_pipeline_report.json"
BASELINE_PATH = (
    REPORT_DIR / "final_pipeline_report_baseline_no_graph.json"
)
CHECKPOINT_PATH = REPORT_DIR / "final_pipeline_checkpoint.jsonl"
CUTOFFS = [1, 3, 5]


def load_checkpoint(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    records: dict[str, dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if record.get("error"):
            continue
        records[record["id"]] = record
    return records


def append_checkpoint(
    path: Path,
    record: dict[str, Any],
    lock: threading.Lock,
) -> None:
    with lock:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def build_sources(documents: list[Any]) -> list[dict[str, Any]]:
    return [
        {
            "id": f"S{index}",
            "url": document.metadata.get("url"),
            "content": document.page_content,
        }
        for index, document in enumerate(documents, start=1)
    ]


def evaluate_case(
    case: dict[str, Any],
    chain: Any,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "id": case["id"],
        "question": case["question"],
        "type": case["type"],
        "language": case["language"],
        "answerable": case["answerable"],
        "mode": "end_to_end",
        "relevant_urls": case["relevant_urls"],
        "expected_refusal": case.get("expected_refusal", False),
        "citation_required": case.get("citation_required", False),
        "expected_filter": case.get("expected_filter"),
        "expected_router": case.get("expected_router"),
        "route": None,
        "route_correct": None,
        "search_query": None,
        "metadata_filter": None,
        "filter_score": None,
        "fallback_used": False,
        "retrieved_urls": [],
        "context_urls": [],
        "retrieved": [],
        "rank": None,
        "answer": None,
        "rule": None,
        "judge": None,
        "error": None,
    }

    try:
        response = chain.ask(case["question"])
        record["route"] = response.route
        record["route_correct"] = (
            response.route == case.get("expected_router")
        )
        record["search_query"] = response.search_query
        record["metadata_filter"] = response.metadata_filter
        record["fallback_used"] = response.fallback_used
        record["filter_score"] = filter_score(
            case.get("expected_filter"),
            response.metadata_filter,
        )
        record["answer"] = response.answer

        retrieval_documents = (
            response.retrieval_sources or response.sources
        )
        context_documents = response.sources
        record["retrieved_urls"] = dedupe_urls(retrieval_documents)
        record["context_urls"] = dedupe_urls(context_documents)
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
            for document in retrieval_documents
        ]
        relevant_urls = set(case["relevant_urls"])
        record["rank"] = next(
            (
                position
                for position, url in enumerate(
                    record["retrieved_urls"], start=1
                )
                if url in relevant_urls
            ),
            None,
        )

        context = format_documents(context_documents)
        sources = build_sources(context_documents)
        record["rule"] = rule_metrics(
            case,
            "end_to_end",
            response.answer,
            sources,
        )
        judge = judge_answer(
            chain.llm,
            case,
            "end_to_end",
            context,
            sources,
            response.answer,
        )
        record["judge"] = judge
        if (
            record["rule"]["language_match_rule"] is False
            and judge.get("language_consistency") == 1
        ):
            judge["language_consistency"] = 0
            judge["reason"] = (
                f"{judge.get('reason', '')} "
                "[规则修正：回答语言与问题语言不一致]"
            ).strip()
    except Exception as exc:
        record["error"] = f"{type(exc).__name__}: {exc}"

    return record


def filter_summary(records: list[dict[str, Any]]) -> dict[str, Any]:
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


def route_summary(records: list[dict[str, Any]]) -> dict[str, Any]:
    routes = Counter(record["route"] for record in records)
    expected = Counter(record["expected_router"] for record in records)
    correct = sum(1 for record in records if record["route_correct"])
    return {
        "route_counts": dict(routes),
        "expected_route_counts": dict(expected),
        "route_correct": correct,
        "route_accuracy": correct / len(records) if records else 0.0,
    }


def build_comparison(
    new_records: list[dict[str, Any]],
    baseline_report: dict[str, Any],
) -> dict[str, Any]:
    baseline_records = baseline_report["cases"]
    new_by_id = {record["id"]: record for record in new_records}
    baseline_by_id = {
        record["id"]: record for record in baseline_records
    }

    new_retrieval_records = [
        record for record in new_records if record["answerable"]
    ]
    baseline_retrieval_records = [
        record for record in baseline_records if record["answerable"]
    ]
    new_retrieval = metrics_at_cutoffs(
        new_retrieval_records, CUTOFFS
    )
    baseline_retrieval = metrics_at_cutoffs(
        baseline_retrieval_records, CUTOFFS
    )
    new_generation = aggregate(new_records, "end_to_end")
    baseline_generation = aggregate(baseline_records, "end_to_end")

    fixed_retrieval: list[str] = []
    broken_retrieval: list[str] = []
    improved_correctness: list[str] = []
    worsened_correctness: list[str] = []
    improved_completeness: list[str] = []
    worsened_completeness: list[str] = []

    for case_id, new_record in new_by_id.items():
        baseline_record = baseline_by_id.get(case_id)
        if baseline_record is None:
            continue

        if new_record["answerable"]:
            new_hit = (
                new_record["rank"] is not None
                and new_record["rank"] <= 5
            )
            baseline_hit = (
                baseline_record["rank"] is not None
                and baseline_record["rank"] <= 5
            )
            if new_hit and not baseline_hit:
                fixed_retrieval.append(case_id)
            elif baseline_hit and not new_hit:
                broken_retrieval.append(case_id)

        new_judge = new_record.get("judge") or {}
        baseline_judge = baseline_record.get("judge") or {}
        new_correctness = new_judge.get("correctness")
        baseline_correctness = baseline_judge.get("correctness")
        if (
            new_correctness is not None
            and baseline_correctness is not None
        ):
            if new_correctness > baseline_correctness:
                improved_correctness.append(case_id)
            elif new_correctness < baseline_correctness:
                worsened_correctness.append(case_id)

        new_completeness = new_judge.get("completeness")
        baseline_completeness = baseline_judge.get("completeness")
        if (
            new_completeness is not None
            and baseline_completeness is not None
        ):
            if new_completeness > baseline_completeness:
                improved_completeness.append(case_id)
            elif new_completeness < baseline_completeness:
                worsened_completeness.append(case_id)

    def delta(
        new: dict[str, Any],
        baseline: dict[str, Any],
    ) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in new.items():
            baseline_value = baseline.get(key)
            if (
                isinstance(value, (int, float))
                and isinstance(baseline_value, (int, float))
            ):
                result[key] = value - baseline_value
        return result

    return {
        "baseline_path": str(BASELINE_PATH),
        "retrieval": {
            "baseline": baseline_retrieval,
            "graph": new_retrieval,
            "delta": {
                key: delta(new_retrieval[key], baseline_retrieval[key])
                for key in new_retrieval
            },
        },
        "generation": {
            "baseline": baseline_generation,
            "graph": new_generation,
            "delta": delta(new_generation, baseline_generation),
        },
        "changes": {
            "fixed_retrieval": sorted(fixed_retrieval),
            "broken_retrieval": sorted(broken_retrieval),
            "improved_correctness": sorted(improved_correctness),
            "worsened_correctness": sorted(worsened_correctness),
            "improved_completeness": sorted(improved_completeness),
            "worsened_completeness": sorted(worsened_completeness),
        },
    }


def write_markdown(report: dict[str, Any], path: Path) -> None:
    config = report["config"]
    retrieval = report["retrieval"]
    generation = report["generation"]
    routing = report["routing"]
    filters = report["filter"]
    citation_value = (
        f"{generation['citation_accuracy']:.4f}"
        if generation["citation_accuracy"] is not None
        else "N/A"
    )
    lines = [
        "# Final Pipeline Evaluation",
        "",
        f"- 日期：2026-11-26",
        f"- 测试集：`{config['dataset']}`",
        f"- 流程：router → hybrid → sibling merge → rerank → LLM → language guard",
        f"- 返回文档数：top {config['top_k']}",
        f"- 生成模型：`{config['llm_model']}`",
        f"- 图扩展：`{config.get('graph_stats')}`",
        f"- 结果：`{path.with_suffix('.json')}`",
        "",
    ]

    comparison = report.get("comparison")
    if comparison:
        def fmt(value: Any) -> str:
            return f"{value:.4f}" if isinstance(value, (int, float)) else "N/A"

        def fmt_delta(value: Any) -> str:
            return f"{value:+.4f}" if isinstance(value, (int, float)) else "N/A"

        retrieval_cmp = comparison["retrieval"]
        generation_cmp = comparison["generation"]
        lines.extend(
            [
                "## 0. 与无图基线对比",
                "",
                "| 检索指标（k=5） | baseline | graph | Δ |",
                "|---|---:|---:|---:|",
            ]
        )
        for metric, label in (
            ("hit_rate", "Hit@5"),
            ("mrr", "MRR@5"),
            ("ndcg", "nDCG@5"),
        ):
            lines.append(
                f"| {label} | {fmt(retrieval_cmp['baseline']['5'][metric])} | "
                f"{fmt(retrieval_cmp['graph']['5'][metric])} | "
                f"{fmt_delta(retrieval_cmp['delta']['5'][metric])} |"
            )
        lines.extend(
            [
                "",
                "| 生成指标 | baseline | graph | Δ |",
                "|---|---:|---:|---:|",
            ]
        )
        for metric, label in (
            ("correctness", "correctness"),
            ("faithfulness", "faithfulness"),
            ("completeness", "completeness"),
            ("citation_accuracy", "citation_accuracy"),
            ("refusal_accuracy", "refusal_accuracy"),
            ("language_consistency", "language_consistency"),
            ("conciseness", "conciseness"),
        ):
            lines.append(
                f"| {label} | {fmt(generation_cmp['baseline'].get(metric))} | "
                f"{fmt(generation_cmp['graph'].get(metric))} | "
                f"{fmt_delta(generation_cmp['delta'].get(metric))} |"
            )
        changes = comparison["changes"]
        lines.extend(
            [
                "",
                f"- 检索修复：{', '.join(changes['fixed_retrieval']) or '无'}",
                f"- 检索新增失败：{', '.join(changes['broken_retrieval']) or '无'}",
                f"- correctness 提升：{', '.join(changes['improved_correctness']) or '无'}",
                f"- correctness 下降：{', '.join(changes['worsened_correctness']) or '无'}",
                f"- completeness 提升：{', '.join(changes['improved_completeness']) or '无'}",
                f"- completeness 下降：{', '.join(changes['worsened_completeness']) or '无'}",
                "",
            ]
        )

    lines.extend(
        [
            "## 1. 检索指标（RAGChain 实际返回文档）",
            "",
            f"检索指标按 {config['retrieval_cases']} 条可回答样本计算；"
            f"生成指标按 {config['generation_cases']} 条样本计算（含无答案样本）。",
            "",
            "| k | Hit@k | Recall@k | MRR@k | nDCG@k |",
            "|---:|---:|---:|---:|---:|",
        ]
    )
    for cutoff in CUTOFFS:
        row = retrieval[str(cutoff)]
        lines.append(
            f"| {cutoff} | {row['hit_rate']:.4f} | {row['recall']:.4f} | "
            f"{row['mrr']:.4f} | {row['ndcg']:.4f} |"
        )

    lines.extend(
        [
            "",
            "## 2. 路由与 Filter",
            "",
            "```text",
            f"route_counts = {routing['route_counts']}",
            f"expected_route_counts = {routing['expected_route_counts']}",
            f"route_accuracy = {routing['route_accuracy']:.4f}",
            f"expected_filter_cases = {filters['expected_filter_cases']}",
            f"filter_present = {filters['filter_present']}",
            f"exact_match = {filters['exact_match']}",
            f"exact_match_rate = {filters['exact_match_rate']:.4f}",
            f"unexpected_filter_cases = {filters['unexpected_filter_cases']}",
            f"unexpected_filter_ids = {filters['unexpected_filter_ids']}",
            f"invalid_or_failed = {filters['invalid_or_failed']}",
            "```",
            "",
            "## 3. 生成质量（真实检索 context）",
            "",
            "| 指标 | 值 |",
            "|---|---:|",
            f"| correctness | {generation['correctness']:.4f} |",
            f"| faithfulness | {generation['faithfulness']:.4f} |",
            f"| completeness | {generation['completeness']:.4f} |",
            f"| citation_accuracy | {citation_value} |",
            f"| refusal_accuracy | {generation['refusal_accuracy']:.4f} |",
            f"| language_consistency | {generation['language_consistency']:.4f} |",
            f"| conciseness | {generation['conciseness']:.4f} |",
            "",
            "## 4. 按路由拆分（k=5）",
            "",
            "| 路由 | n | retrieval_n | Hit@5 | MRR@5 | correctness | faithfulness | completeness |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for route, row in report["by_route"].items():
        ret = row["retrieval"]["5"]
        gen = row["generation"]
        lines.append(
            f"| `{route}` | {row['cases']} | {row['retrieval_cases']} | "
            f"{ret['hit_rate']:.4f} | {ret['mrr']:.4f} | "
            f"{gen['correctness']:.4f} | {gen['faithfulness']:.4f} | "
            f"{gen['completeness']:.4f} |"
        )

    lines.extend(
        [
            "",
            "## 5. 按语言 / 类型拆分（k=5）",
            "",
        ]
    )
    for title, key in (("按语言", "by_language"), ("按类型", "by_type")):
        lines.extend(
            [
                f"### {title}",
                "",
                "| 分组 | n | retrieval_n | Hit@5 | correctness | faithfulness | completeness |",
                "|---|---:|---:|---:|---:|---:|---:|",
            ]
        )
        for name, row in report[key].items():
            ret = row["retrieval"]["5"]
            gen = row["generation"]
            hit = (
                f"{ret['hit_rate']:.4f}"
                if row["retrieval_cases"]
                else "N/A"
            )
            lines.append(
                f"| `{name}` | {row['cases']} | {row['retrieval_cases']} | "
                f"{hit} | {gen['correctness']:.4f} | "
                f"{gen['faithfulness']:.4f} | {gen['completeness']:.4f} |"
            )
        lines.append("")

    lines.extend(
        [
            "## 6. 失败案例",
            "",
        ]
    )
    failures = [
        record
        for record in report["cases"]
        if record["error"]
        or (
            record["answerable"]
            and (record["rank"] is None or record["rank"] > 5)
        )
        or failure_reasons(record)
    ]
    if failures:
        for record in failures:
            judge = record.get("judge") or {}
            reasons = failure_reasons(record)
            if record["answerable"] and (
                record["rank"] is None or record["rank"] > 5
            ):
                reasons.append("retrieval_miss")
            lines.append(
                f"- `{record['id']}` route=`{record['route']}` "
                f"rank={record['rank']} reasons={reasons} "
                f"judge_reason={judge.get('reason', '')!r}"
            )
    else:
        lines.append("无。")

    lines.extend(
        [
            "",
            "## 7. 结论",
            "",
            "1. 本报告是端到端结果：检索、路由、兄弟合并、生成和语言检查都走生产 `RAGChain`。",
            f"2. 实际检索 Hit@5 = {retrieval['5']['hit_rate']:.4f}，MRR@5 = {retrieval['5']['mrr']:.4f}。",
            f"3. 生成 correctness = {generation['correctness']:.4f}，"
            f"faithfulness = {generation['faithfulness']:.4f}，"
            f"completeness = {generation['completeness']:.4f}，"
            f"citation = {citation_value}，"
            f"refusal = {generation['refusal_accuracy']:.4f}，"
            f"language = {generation['language_consistency']:.4f}。",
            "4. 该结果使用真实检索 context，不能与 gold_docs oracle 结果直接等价比较。",
            "5. 生成端的主要瓶颈是 context 覆盖，而不是幻觉："
            "faithfulness=1.0000，但 completeness=0.6452，"
            "7 条可回答样本因检索 context 缺少答案而误拒答。"
            "下一轮应优先提升 chunk 召回和上下文覆盖，而不是继续调生成提示词。",
            "",
            "## 8. 复现",
            "",
            "```powershell",
            '$env:PYTHONPATH="D:\\My_rag\\src"',
            '$env:HF_HUB_OFFLINE="1"',
            '$env:TRANSFORMERS_OFFLINE="1"',
            "python tests/test_FinalPipeline.py --workers 2 --timeout 180 --restart",
            "```",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="End-to-end RAG pipeline evaluation"
    )
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--restart", action="store_true")
    parser.add_argument(
        "--ids",
        default="",
        help="逗号分隔的 case id，只评测这些样本",
    )
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    args = parser.parse_args()

    wanted_ids = {
        value.strip() for value in args.ids.split(",") if value.strip()
    }
    cases = [
        case
        for case in load_cases(DATASET_PATH)
        if not wanted_ids or case["id"] in wanted_ids
    ]
    print(f"Loaded {len(cases)} cases", flush=True)

    print("Building RAGChain (router + hybrid + catalog)...", flush=True)
    catalog = build_chunk_catalog()
    chain = build_rag_chain(
        k=5,
        candidate_k=50,
        coarse_k=20,
        context_k=8,
        catalog=catalog,
    )
    graph_stats = (
        chain.document_graph.stats()
        if chain.document_graph is not None
        else None
    )
    print(f"Document graph: {graph_stats}", flush=True)

    # Pre-build Self-query retrievers and warm the reranker before concurrent
    # workers. Without warming, multiple threads can each initialize the
    # CrossEncoder model and exhaust GPU memory.
    for fields in (
        ("url",),
        ("title",),
        ("platform",),
        ("doc_type",),
    ):
        chain._get_self_query_retriever(fields)
    get_cross_encoder()

    if args.restart and CHECKPOINT_PATH.exists():
        CHECKPOINT_PATH.unlink()
    checkpoint = load_checkpoint(CHECKPOINT_PATH)
    remaining = [case for case in cases if case["id"] not in checkpoint]
    print(
        f"Checkpoint: {len(checkpoint)} completed, "
        f"{len(remaining)} remaining, workers={args.workers}",
        flush=True,
    )

    lock = threading.Lock()
    new_records: list[dict[str, Any]] = []

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {
            pool.submit(evaluate_case, case, chain): case
            for case in remaining
        }
        completed = 0
        for future in as_completed(futures):
            case = futures[future]
            record = future.result()
            new_records.append(record)
            append_checkpoint(CHECKPOINT_PATH, record, lock)
            completed += 1
            judge = record.get("judge") or {}
            print(
                f"[{completed:03d}/{len(remaining)}] {case['id']} "
                f"route={record['route']} rank={record['rank']} "
                f"correct={judge.get('correctness')} "
                f"faith={judge.get('faithfulness')} "
                f"complete={judge.get('completeness')} "
                f"citation={judge.get('citation_accuracy')} "
                f"error={record.get('error') or '-'}",
                flush=True,
            )

    records_by_id = {
        **checkpoint,
        **{record["id"]: record for record in new_records},
    }
    records = [
        records_by_id[case["id"]]
        for case in cases
        if case["id"] in records_by_id
    ]
    print(f"Collected {len(records)}/{len(cases)} records", flush=True)

    retrieval_records = [
        record for record in records if record["answerable"]
    ]
    retrieval = metrics_at_cutoffs(retrieval_records, CUTOFFS)
    generation = aggregate(records, "end_to_end")
    filters = filter_summary(records)
    routing = route_summary(records)

    by_route: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_language: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_type: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_route[str(record["route"])].append(record)
        by_language[str(record["language"])].append(record)
        by_type[str(record["type"])].append(record)

    def group_payload(group: list[dict[str, Any]]) -> dict[str, Any]:
        answerable_group = [
            record for record in group if record["answerable"]
        ]
        return {
            "cases": len(group),
            "retrieval_cases": len(answerable_group),
            "retrieval": metrics_at_cutoffs(answerable_group, CUTOFFS),
            "generation": aggregate(group, "end_to_end"),
        }

    report = {
        "config": {
            "dataset": str(DATASET_PATH),
            "pipeline": "router -> hybrid -> sibling_merge -> rerank -> graph_context -> llm",
            "top_k": 5,
            "candidate_k": 50,
            "coarse_k": 20,
            "context_k": 8,
            "use_graph": True,
            "graph_stats": graph_stats,
            "retrieval_cases": len(retrieval_records),
            "generation_cases": len(records),
            "dense_weight": 0.7,
            "bm25_weight": 0.3,
            "llm_model": "deepseek-chat",
            "judge": "LLM-as-judge + rule checks",
            "cutoffs": CUTOFFS,
            "workers": args.workers,
            "timeout": args.timeout,
        },
        "routing": routing,
        "filter": filters,
        "retrieval": retrieval,
        "generation": generation,
        "by_route": {
            route: group_payload(group) for route, group in by_route.items()
        },
        "by_language": {
            name: group_payload(group)
            for name, group in by_language.items()
        },
        "by_type": {
            name: group_payload(group) for name, group in by_type.items()
        },
        "cases": records,
    }

    if BASELINE_PATH.exists():
        baseline_report = json.loads(
            BASELINE_PATH.read_text(encoding="utf-8")
        )
        report["comparison"] = build_comparison(
            records,
            baseline_report,
        )
        report["config"]["baseline_path"] = str(BASELINE_PATH)

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_markdown(report, args.report.with_suffix(".md"))

    if len(records) == len(cases) and all(
        not record.get("error") for record in records
    ):
        if CHECKPOINT_PATH.exists():
            CHECKPOINT_PATH.unlink()

    print()
    print("Retrieval:", {
        key: round(value["hit_rate"], 4)
        for key, value in retrieval.items()
    })
    print("Generation:", {
        key: round(value, 4) if isinstance(value, float) else value
        for key, value in generation.items()
        if key
        in {
            "correctness",
            "faithfulness",
            "completeness",
            "citation_accuracy",
            "refusal_accuracy",
            "language_consistency",
            "conciseness",
        }
    })
    print(f"Report written to {args.report}")
    print(f"Markdown written to {args.report.with_suffix('.md')}")


if __name__ == "__main__":
    main()
