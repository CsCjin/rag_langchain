"""Rule-based query routing for metadata-aware retrieval.

Rules (highest-confidence signals first):
1. Explicit LangChain docs URL -> self_query, allowed field: url.
2. Explicit title: Chinese 《...》, or English doc/page titled "..." -> self_query, allowed field: title.
3. Explicit platform: JavaScript/JS/TypeScript, or Python with version/docs context -> self_query, allowed field: platform.
4. Explicit doc_type: changelog, release notes, troubleshooting/diagnostics, API reference,
   quickstart, tutorial document/page, release policy -> self_query, allowed field: doc_type.
5. Exclusion: exclude/不要/排除/仅限/只看 combined with a known metadata target.

If no rule matches, route to the default retrieval path.
The router is intentionally rule-based and does not call an LLM.
"""

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from my_rag.config import PROJECT_ROOT

URL_PATTERN = re.compile(
    r"https?://(?:www\.)?docs\.langchain\.com/[^\s<>\"')\]]+",
    re.IGNORECASE,
)
CHINESE_TITLE_PATTERN = re.compile(r"《[^》]{2,}》")
ENGLISH_TITLE_PATTERN = re.compile(
    r'(?i)(?:(?:doc(?:ument)?|page)\s+(?:titled\s+)?["“][^"”]{3,}["”]'
    r'|["“][^"”]{3,}["”]\s+(?:doc(?:ument)?|page))'
)
PLATFORM_JS_PATTERN = re.compile(r"\b(?:javascript|js|typescript)\b", re.IGNORECASE)
PLATFORM_PY_PATTERN = re.compile(
    r"\bpython\s*(?:版|版本|文档|docs?|documentation|implementation)\b",
    re.IGNORECASE,
)
DOC_TYPE_PATTERNS = {
    "changelog": re.compile(r"\bchangelog\b|更新日志|变更日志", re.IGNORECASE),
    "release": re.compile(r"release\s+notes?|发布说明|版本发布", re.IGNORECASE),
    "troubleshooting": re.compile(
        r"\btroubleshoot(?:ing)?\b|\bdiagnostics?\b|故障排查|排查|诊断",
        re.IGNORECASE,
    ),
    "api_reference": re.compile(
        r"\bapi\s+reference\b|\bapi\s+docs?\b|api\s*文档|api\s*参考",
        re.IGNORECASE,
    ),
    "quickstart": re.compile(
        r"(?<![\w-])quickstart\b|快速开始|快速入门",
        re.IGNORECASE,
    ),
    "tutorial": re.compile(
        r"(?:tutorial|教程)\s+(?:文档|doc(?:ument)?|page)|"
        r"(?:文档|doc(?:ument)?|page)\s+(?:tutorial|教程)",
        re.IGNORECASE,
    ),
    "policy": re.compile(
        r"release\s+(?:policy|stages)|版本策略",
        re.IGNORECASE,
    ),
}
EXCLUSION_PATTERN = re.compile(
    r"\b(?:exclude|excluding|without|except)\b|不要|排除|仅限|只看",
    re.IGNORECASE,
)
EXCLUSION_TARGETS = (
    "changelog",
    "release",
    "python",
    "javascript",
    "js",
    "troubleshooting",
    "api reference",
    "doc_type",
    "platform",
)


@dataclass(frozen=True)
class RouteDecision:
    route: str
    signals: tuple[str, ...]
    allowed_fields: tuple[str, ...]


def _mask_urls_and_titles(question: str) -> str:
    """Mask quoted URLs and titles so their words do not trigger other rules.

    For example the URL ``.../oss/javascript/...`` should count as a URL signal,
    not as an explicit JavaScript-platform request; ``Tracing quickstart`` should
    count as a title, not as a doc_type=quickstart request.
    """
    masked = question
    for pattern in (
        URL_PATTERN,
        CHINESE_TITLE_PATTERN,
        ENGLISH_TITLE_PATTERN,
    ):
        masked = pattern.sub(lambda match: " " * len(match.group(0)), masked)
    return masked


def route_query(question: str) -> RouteDecision:
    signals: list[str] = []
    url_hit = bool(URL_PATTERN.search(question))
    title_hit = bool(
        CHINESE_TITLE_PATTERN.search(question)
        or ENGLISH_TITLE_PATTERN.search(question)
    )

    if url_hit:
        signals.append("url")
    if title_hit:
        signals.append("title")

    # Do not let words inside an explicit URL or quoted title trigger the
    # platform/doc_type/exclusion rules.
    masked_question = _mask_urls_and_titles(question)
    secondary_fields: set[str] = set()

    if PLATFORM_JS_PATTERN.search(masked_question):
        signals.append("platform:javascript")
        secondary_fields.add("platform")

    if PLATFORM_PY_PATTERN.search(masked_question):
        signals.append("platform:python")
        secondary_fields.add("platform")

    for doc_type, pattern in DOC_TYPE_PATTERNS.items():
        if pattern.search(masked_question):
            signals.append(f"doc_type:{doc_type}")
            secondary_fields.add("doc_type")

    if EXCLUSION_PATTERN.search(masked_question):
        lower = masked_question.lower()
        if any(target in lower for target in EXCLUSION_TARGETS):
            signals.append("exclusion")
            if any(
                target in lower
                for target in ("changelog", "release", "troubleshooting", "api reference", "doc_type")
            ):
                secondary_fields.add("doc_type")
            if any(target in lower for target in ("python", "javascript", "js", "platform")):
                secondary_fields.add("platform")

    if not signals:
        return RouteDecision(
            route="default",
            signals=(),
            allowed_fields=(),
        )

    # A URL or a quoted title identifies a specific page. Restricting the
    # Self-query filter to that single field avoids redundant platform/doc_type
    # filters that could exclude the target page.
    if url_hit:
        allowed_fields = {"url"}
    elif title_hit:
        allowed_fields = {"title"}
    else:
        allowed_fields = secondary_fields

    return RouteDecision(
        route="self_query",
        signals=tuple(signals),
        allowed_fields=tuple(sorted(allowed_fields)),
    )


def load_cases(path: Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def evaluate(dataset: Path, report_path: Path) -> dict:
    cases = load_cases(dataset)
    results = []
    expected_counter = Counter()
    predicted_counter = Counter()

    for case in cases:
        expected = case.get("expected_router", "default")
        decision = route_query(case["question"])
        predicted = decision.route
        expected_counter[expected] += 1
        predicted_counter[predicted] += 1
        results.append(
            {
                "id": case["id"],
                "question": case["question"],
                "type": case.get("type"),
                "language": case.get("language"),
                "expected_router": expected,
                "predicted_router": predicted,
                "signals": list(decision.signals),
                "allowed_fields": list(decision.allowed_fields),
                "correct": expected == predicted,
            }
        )

    total = len(results)
    correct = sum(1 for item in results if item["correct"])
    expected_self = expected_counter["self_query"]
    predicted_self = predicted_counter["self_query"]
    true_positive = sum(
        1
        for item in results
        if item["expected_router"] == "self_query"
        and item["predicted_router"] == "self_query"
    )
    precision = true_positive / predicted_self if predicted_self else 0.0
    recall = true_positive / expected_self if expected_self else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0

    failures = [item for item in results if not item["correct"]]
    summary = {
        "total": total,
        "correct": correct,
        "accuracy": correct / total if total else 0.0,
        "expected_counts": dict(expected_counter),
        "predicted_counts": dict(predicted_counter),
        "self_query_precision": precision,
        "self_query_recall": recall,
        "self_query_f1": f1,
        "confusion_matrix": {
            "expected_self_query_predicted_self_query": true_positive,
            "expected_self_query_predicted_default": expected_self - true_positive,
            "expected_default_predicted_self_query": predicted_self - true_positive,
            "expected_default_predicted_default": total - expected_self - predicted_self + true_positive,
        },
    }

    report = {
        "dataset": str(dataset),
        "summary": summary,
        "failures": failures,
        "cases": results,
    }
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    markdown_path = report_path.with_suffix(".md")
    markdown_lines = [
        "# Router Evaluation Report",
        "",
        f"- Dataset: `{dataset}`",
        f"- Total: {total}",
        f"- Accuracy: {summary['accuracy']:.4f}",
        f"- Self-query precision: {precision:.4f}",
        f"- Self-query recall: {recall:.4f}",
        f"- Self-query F1: {f1:.4f}",
        "",
        "## Confusion Matrix",
        "",
        "```text",
        f"expected self_query, predicted self_query: {summary['confusion_matrix']['expected_self_query_predicted_self_query']}",
        f"expected self_query, predicted default:    {summary['confusion_matrix']['expected_self_query_predicted_default']}",
        f"expected default, predicted self_query:    {summary['confusion_matrix']['expected_default_predicted_self_query']}",
        f"expected default, predicted default:       {summary['confusion_matrix']['expected_default_predicted_default']}",
        "```",
        "",
        "## Failures",
        "",
    ]
    if failures:
        for item in failures:
            markdown_lines.append(
                f"- `{item['id']}` expected `{item['expected_router']}`, "
                f"predicted `{item['predicted_router']}`, signals={item['signals']}"
            )
    else:
        markdown_lines.append("None.")
    markdown_lines.append("")
    markdown_path.write_text("\n".join(markdown_lines), encoding="utf-8")

    return report


def main() -> None:
    parser = argparse.ArgumentParser(description="Rule-based query router evaluation")
    parser.add_argument(
        "--dataset",
        type=Path,
        default=PROJECT_ROOT / "tests" / "evaluation" / "qa_set.jsonl",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=PROJECT_ROOT / "tests" / "evaluation" / "router_report.json",
    )
    args = parser.parse_args()

    report = evaluate(args.dataset, args.report)
    summary = report["summary"]
    print(f"total: {summary['total']}")
    print(f"accuracy: {summary['accuracy']:.4f}")
    print(f"self_query precision: {summary['self_query_precision']:.4f}")
    print(f"self_query recall: {summary['self_query_recall']:.4f}")
    print(f"self_query f1: {summary['self_query_f1']:.4f}")
    print(f"report: {args.report}")
    print(f"markdown: {args.report.with_suffix('.md')}")
    if report["failures"]:
        print("failures:")
        for item in report["failures"]:
            print(
                f"  {item['id']}: expected {item['expected_router']}, "
                f"predicted {item['predicted_router']}, signals={item['signals']}"
            )


if __name__ == "__main__":
    main()
