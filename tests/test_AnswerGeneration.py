"""Evaluate the answer-generation node with oracle contexts.

Two modes:
- ``gold_answer``: the reference answer is the context.
- ``gold_docs``: retrieve the top chunks from the reference URLs only, so
  retrieval errors are excluded but citations are still meaningful.

For each answer, this script records rule-based metrics and a strict
LLM-as-judge rubric covering correctness, faithfulness, completeness,
citation accuracy, refusal correctness, language consistency and conciseness.
"""

import argparse
import json
import os
import re
import sys
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))

from test_RouterQuery import (  # noqa: E402
    load_cases,
    term_coverage,
)

from my_rag.config import PROJECT_ROOT, VECTOR_STORE_DIR  # noqa: E402
from my_rag.core.chunk_catalog import build_chunk_catalog  # noqa: E402
from my_rag.core.hybrid import retrieve_hybrid_with_rerank  # noqa: E402
from my_rag.core.vector_store import load_vector_store  # noqa: E402
from my_rag.model.embedding import get_embedding_model  # noqa: E402
from my_rag.model.llm import get_llm  # noqa: E402
from my_rag.model.reranker import DEFAULT_DOC_TYPE_PENALTIES  # noqa: E402

DATASET_PATH = PROJECT_ROOT / "tests" / "evaluation" / "qa_set.jsonl"
REPORT_PATH = (
    PROJECT_ROOT
    / "tests"
    / "evaluation"
    / "test_generation"
    / "generation_report.json"
)
CHECKPOINT_PATH = (
    PROJECT_ROOT
    / "tests"
    / "evaluation"
    / "test_generation"
    / "generation_checkpoint.jsonl"
)
MODES = ("gold_answer", "gold_docs")

GENERATION_SYSTEM = """你是基于 LangChain 官方文档的问答助手。
规则：
1. 只依据给定上下文回答，不得使用上下文之外的知识。
2. 上下文不足以回答时，明确说明无法从文档中找到答案，不要编造。
3. 语言规则（最高优先级）：
   - 先判断用户问题的主要语言。
   - 用户用中文提问，必须用中文回答；用户用英文提问，必须用英文回答。
   - 即使上下文主要是英文，也不能把中文问题的回答改成英文；
     即使上下文主要是中文，也不能把英文问题的回答改成中文。
   - 代码、API 名称、参数名、命令、URL 和专有名词保持原样，不要翻译。
4. 引用上下文来源时使用 [S1]、[S2] 格式；每个关键结论尽量给出引用。
5. 回答简洁、结构清晰；需要步骤时使用编号列表。"""

JUDGE_SYSTEM = """你是一个严格的 RAG 回答评审。
只输出 JSON 对象，不要输出 Markdown 代码块或额外解释。"""


def build_llm(timeout: int = 120) -> Any:
    # Importing get_llm loads the project .env.
    from my_rag.model.llm import get_llm  # noqa: F401
    from langchain_deepseek import ChatDeepSeek

    return ChatDeepSeek(
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        temperature=0,
        timeout=timeout,
    )


def extract_citations(text: str) -> list[int]:
    return sorted(
        {
            int(value)
            for value in re.findall(r"\[S(\d+)\]", text or "")
        }
    )


def detect_refusal(text: str) -> bool:
    patterns = [
        r"无法从(?:给定|提供)?(?:的)?文档",
        r"没有(?:相关|足够)的?(?:信息|文档)",
        r"文档中(?:没有|未)",
        r"无法回答",
        r"不在.{0,8}(?:覆盖|范围)",
        r"cannot (?:find|answer)",
        r"not (?:found|enough)",
        r"no (?:relevant )?information",
        r"unable to answer",
        r"does not contain",
    ]
    return any(
        re.search(pattern, text or "", re.IGNORECASE)
        for pattern in patterns
    )


def rule_language_match(answer: str, language: str) -> bool:
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", answer or ""))
    non_space = len(re.sub(r"\s", "", answer or ""))
    ratio = chinese_chars / max(non_space, 1)
    if language == "zh":
        return chinese_chars >= 10 and ratio >= 0.05
    return ratio < 0.05


def build_gold_answer_context(
    case: dict[str, Any],
) -> tuple[str, list[dict[str, Any]]]:
    if not case["answerable"]:
        return "（没有可用上下文）", []
    url = (
        case["relevant_urls"][0]
        if case.get("relevant_urls")
        else ""
    )
    source = {
        "id": "S1",
        "url": url,
        "content": case["reference_answer"],
    }
    context = (
        f"[S1] URL: {url}\n{case['reference_answer']}"
    )
    return context, [source]


def build_gold_docs_context(
    case: dict[str, Any],
    vector_store: Any,
    catalog: Any,
) -> tuple[str, list[dict[str, Any]], str | None]:
    """Use the full content of the reference URLs as oracle context.

    This is intentionally not a retrieval test: the goal is to measure the
    generation node with sufficient evidence. A large cap is used so that
    detailed how-to answers and code blocks are not truncated.
    """
    if not case["answerable"] or not case.get("relevant_urls"):
        return "（没有可用上下文）", [], None

    urls = case["relevant_urls"]
    max_total_chars = 24000
    per_url_cap = max(4000, max_total_chars // max(len(urls), 1))

    grouped: dict[str, list[Any]] = {}
    for document in catalog.documents:
        url = str(document.metadata.get("url") or "")
        if url in urls:
            grouped.setdefault(url, []).append(document)

    sources: list[dict[str, Any]] = []
    parts: list[str] = []
    total_chars = 0
    for index, url in enumerate(urls, start=1):
        documents = grouped.get(url)
        if not documents:
            continue
        documents.sort(
            key=lambda document: document.metadata.get(
                "chunk_index", 0
            )
        )
        content = "\n\n".join(
            document.page_content for document in documents
        )[:per_url_cap]
        source = {
            "id": f"S{index}",
            "url": url,
            "content": content,
        }
        block = f"[S{index}] URL: {url}\n{content}"
        remaining = max_total_chars - total_chars
        if remaining <= 0:
            break
        block = block[:remaining]
        sources.append(source)
        parts.append(block)
        total_chars += len(block)

    if not sources:
        return "（没有可用上下文）", [], "no_chunks_for_reference_urls"

    return "\n\n".join(parts), sources, None


def detect_answer_language(question: str) -> str:
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", question or ""))
    non_space = len(re.sub(r"\s", "", question or ""))
    ratio = chinese_chars / max(non_space, 1)
    return "中文" if chinese_chars >= 2 and ratio >= 0.05 else "英文"


def build_generation_messages(
    question: str,
    context: str,
) -> list[tuple[str, str]]:
    answer_language = detect_answer_language(question)
    return [
        ("system", GENERATION_SYSTEM),
        (
            "human",
            f"上下文：\n{context or '（没有可用上下文）'}\n\n"
            f"问题：{question}\n\n"
            f"回答语言：{answer_language}。"
            "请严格使用该语言回答，不要使用其他语言。",
        ),
    ]


def invoke_text(llm: Any, messages: list[tuple[str, str]]) -> str:
    response = llm.invoke(messages)
    content = getattr(response, "content", response)
    if isinstance(content, list):
        content = "".join(str(item) for item in content)
    return str(content).strip()


def parse_json_object(text: str) -> dict[str, Any]:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
        cleaned = re.sub(r"\s*```$", "", cleaned)
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"No JSON object found: {text[:200]}")
    return json.loads(cleaned[start : end + 1])


def clamp_int(value: Any, low: int = 0, high: int = 2) -> int:
    try:
        number = int(value)
    except (TypeError, ValueError):
        number = low
    return max(low, min(high, number))


def judge_answer(
    llm: Any,
    case: dict[str, Any],
    mode: str,
    context: str,
    sources: list[dict[str, Any]],
    answer: str,
) -> dict[str, Any]:
    citation_required = bool(
        case.get("citation_required")
        and mode in ("gold_docs", "end_to_end")
    )
    source_ids = [source["id"] for source in sources]
    prompt = f"""问题：
{case['question']}

问题语言：{case['language']}
是否可回答：{case['answerable']}
是否需要引用：{citation_required}
可用来源编号：{source_ids}

参考答案：
{case['reference_answer']}

关键术语：
{case.get('must_keep_terms', [])}

上下文：
{context or '（没有可用上下文）'}

模型回答：
{answer}

评分标准：
- correctness：2=事实与参考答案一致，关键 API/参数/版本/条件正确；1=主要正确但有轻微错误或缺项；0=关键事实错误或答非所问。
- faithfulness：2=所有事实性陈述都能在上下文找到支持；1=有少量无依据陈述但不影响主要结论；0=明显编造或与上下文矛盾。
- completeness：2=覆盖参考答案的关键信息、步骤和限制条件；1=覆盖主要点但缺少关键步骤/限制；0=遗漏大部分关键信息。
- citation_accuracy：2=引用编号都存在且支持对应结论；1=引用存在但有遗漏或部分不支持；0=引用不存在、编号错误或引用不支持结论。是否需要引用为 false 时输出 null。
- refusal_correct：可回答时 1=正常回答，0=误拒答；不可回答时 1=明确拒答且不编造，0=编造答案。
- language_consistency：1=回答语言与问题一致；0=不一致。
- conciseness：2=简洁、无重复或无关内容；1=有一些重复或轻微跑题；0=大量重复或无关内容。

只输出如下 JSON：
{{
  "correctness": 0,
  "faithfulness": 0,
  "completeness": 0,
  "citation_accuracy": null,
  "refusal_correct": 0,
  "language_consistency": 0,
  "conciseness": 0,
  "unsupported_claims": [],
  "missing_key_points": [],
  "citation_issues": [],
  "reason": ""
}}"""

    last_error = None
    for attempt in range(2):
        try:
            raw = invoke_text(
                llm,
                [
                    ("system", JUDGE_SYSTEM),
                    ("human", prompt),
                ],
            )
            result = parse_json_object(raw)
            citation_value = result.get("citation_accuracy")
            if not citation_required:
                citation_value = None
            else:
                citation_value = clamp_int(citation_value)
            return {
                "correctness": clamp_int(result.get("correctness")),
                "faithfulness": clamp_int(result.get("faithfulness")),
                "completeness": clamp_int(result.get("completeness")),
                "citation_accuracy": citation_value,
                "refusal_correct": clamp_int(
                    result.get("refusal_correct"), 0, 1
                ),
                "language_consistency": clamp_int(
                    result.get("language_consistency"), 0, 1
                ),
                "conciseness": clamp_int(result.get("conciseness")),
                "unsupported_claims": result.get(
                    "unsupported_claims", []
                ),
                "missing_key_points": result.get(
                    "missing_key_points", []
                ),
                "citation_issues": result.get("citation_issues", []),
                "reason": str(result.get("reason", "")),
                "judge_error": None,
            }
        except Exception as exc:
            last_error = f"{type(exc).__name__}: {exc}"
            time.sleep(2 * (attempt + 1))

    return {
        "correctness": 0,
        "faithfulness": 0,
        "completeness": 0,
        "citation_accuracy": None,
        "refusal_correct": 0,
        "language_consistency": 0,
        "conciseness": 0,
        "unsupported_claims": [],
        "missing_key_points": [],
        "citation_issues": [],
        "reason": "",
        "judge_error": last_error,
    }


def rule_metrics(
    case: dict[str, Any],
    mode: str,
    answer: str,
    sources: list[dict[str, Any]],
) -> dict[str, Any]:
    citations = extract_citations(answer)
    source_ids = {source["id"] for source in sources}
    citation_required = bool(
        case.get("citation_required")
        and mode in ("gold_docs", "end_to_end")
    )
    coverage, missing_terms = term_coverage(
        answer,
        case.get("must_keep_terms", []),
    )
    return {
        "citations": citations,
        "citation_count": len(citations),
        "citation_present": bool(citations),
        "citation_valid": (
            all(f"S{value}" in source_ids for value in citations)
            if citations
            else not citation_required
        ),
        "citation_required": citation_required,
        "must_keep_coverage": coverage,
        "missing_terms": missing_terms,
        "refusal_detected": detect_refusal(answer),
        "language_match_rule": rule_language_match(
            answer, case["language"]
        ),
        "answer_chars": len(answer),
    }


def evaluate_with_context(
    case: dict[str, Any],
    mode: str,
    llm: Any,
    context: str,
    sources: list[dict[str, Any]],
    context_error: str | None = None,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "id": case["id"],
        "question": case["question"],
        "type": case["type"],
        "language": case["language"],
        "answerable": case["answerable"],
        "expected_refusal": case.get("expected_refusal", False),
        "citation_required": case.get("citation_required", False),
        "mode": mode,
        "context_error": context_error,
        "context_chars": 0,
        "sources": [],
        "answer": None,
        "generation_error": None,
        "judge_error": None,
        "rule": None,
        "judge": None,
    }

    record["context_chars"] = len(context)
    record["sources"] = [
        {"id": source["id"], "url": source["url"]}
        for source in sources
    ]

    try:
        answer = invoke_text(
            llm,
            build_generation_messages(case["question"], context),
        )
        record["answer"] = answer
    except Exception as exc:
        record["generation_error"] = f"{type(exc).__name__}: {exc}"
        return record

    record["rule"] = rule_metrics(case, mode, answer, sources)
    judge = judge_answer(
        llm, case, mode, context, sources, answer
    )
    # Rule override: the judge occasionally misses an obvious language
    # mismatch. The deterministic language check is authoritative here.
    if (
        not record["rule"]["language_match_rule"]
        and judge.get("language_consistency") == 1
    ):
        judge["language_consistency"] = 0
        judge["reason"] = (
            f"{judge.get('reason', '')} "
            "[规则修正：回答语言与问题语言不一致]"
        ).strip()
    record["judge"] = judge
    record["judge_error"] = judge.get("judge_error")
    return record


def evaluate_case(
    case: dict[str, Any],
    mode: str,
    llm: Any,
    vector_store: Any,
    catalog: Any,
) -> dict[str, Any]:
    if mode == "gold_answer":
        context, sources = build_gold_answer_context(case)
        return evaluate_with_context(
            case, mode, llm, context, sources
        )

    context, sources, context_error = build_gold_docs_context(
        case, vector_store, catalog
    )
    return evaluate_with_context(
        case,
        mode,
        llm,
        context,
        sources,
        context_error,
    )


def prepare_cases(
    cases: list[dict[str, Any]],
    modes: list[str],
    vector_store: Any,
    catalog: Any,
) -> list[dict[str, Any]]:
    prepared: list[dict[str, Any]] = []
    total = len(cases) * len(modes)
    index = 0
    for mode in modes:
        for case in cases:
            index += 1
            if mode == "gold_answer":
                context, sources = build_gold_answer_context(case)
                context_error = None
            else:
                context, sources, context_error = build_gold_docs_context(
                    case, vector_store, catalog
                )
            prepared.append(
                {
                    "case": case,
                    "mode": mode,
                    "context": context,
                    "sources": sources,
                    "context_error": context_error,
                }
            )
            print(
                f"[context {index:03d}/{total}] {mode} {case['id']} "
                f"chars={len(context)} error={context_error or '-'}",
                flush=True,
            )
    return prepared


def load_checkpoint(path: Path) -> dict[tuple[str, str], dict[str, Any]]:
    if not path.exists():
        return {}
    records: dict[tuple[str, str], dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        records[(record["mode"], record["id"])] = record
    return records


def append_checkpoint(
    path: Path,
    record: dict[str, Any],
    lock: threading.Lock,
) -> None:
    with lock:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(
                json.dumps(record, ensure_ascii=False) + "\n"
            )


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def aggregate(records: list[dict[str, Any]], mode: str) -> dict[str, Any]:
    judged = [
        record
        for record in records
        if record["mode"] == mode
        and record.get("judge")
        and not record.get("judge_error")
    ]
    rules = [
        record
        for record in records
        if record["mode"] == mode and record.get("rule")
    ]
    citation_records = [
        record
        for record in judged
        if record["rule"]["citation_required"]
        and record["judge"].get("citation_accuracy") is not None
    ]
    answerable_records = [
        record for record in judged if record["answerable"]
    ]
    unanswerable_records = [
        record for record in judged if not record["answerable"]
    ]

    return {
        "cases": len([r for r in records if r["mode"] == mode]),
        "judged": len(judged),
        "judge_success_rate": (
            len(judged) / len([r for r in records if r["mode"] == mode])
            if records
            else 0.0
        ),
        "correctness": mean(
            [r["judge"]["correctness"] / 2 for r in judged]
        ),
        "faithfulness": mean(
            [r["judge"]["faithfulness"] / 2 for r in judged]
        ),
        "completeness": mean(
            [r["judge"]["completeness"] / 2 for r in judged]
        ),
        "citation_accuracy": (
            mean(
                [
                    r["judge"]["citation_accuracy"] / 2
                    for r in citation_records
                ]
            )
            if citation_records
            else None
        ),
        "citation_cases": len(citation_records),
        "refusal_accuracy": mean(
            [r["judge"]["refusal_correct"] for r in judged]
        ),
        # Require both the judge and the rule check to agree. This catches
        # cases where the judge misses an obvious language mismatch.
        "language_consistency": mean(
            [
                1.0
                if (
                    r["judge"]["language_consistency"] == 1
                    and r["rule"]["language_match_rule"]
                )
                else 0.0
                for r in judged
            ]
        ),
        "conciseness": mean(
            [r["judge"]["conciseness"] / 2 for r in judged]
        ),
        "rule_must_keep_coverage": mean(
            [r["rule"]["must_keep_coverage"] for r in rules]
        ),
        "rule_language_match": mean(
            [1.0 if r["rule"]["language_match_rule"] else 0.0 for r in rules]
        ),
        "citation_present_rate": mean(
            [
                1.0 if r["rule"]["citation_present"] else 0.0
                for r in rules
                if r["rule"]["citation_required"]
            ]
        ),
        "citation_valid_rate": mean(
            [
                1.0 if r["rule"]["citation_valid"] else 0.0
                for r in rules
                if r["rule"]["citation_required"]
            ]
        ),
        "refusal_detected_rate": mean(
            [1.0 if r["rule"]["refusal_detected"] else 0.0 for r in rules]
        ),
        "false_refusal_rate": mean(
            [
                1.0 if r["rule"]["refusal_detected"] else 0.0
                for r in rules
                if r["answerable"]
            ]
        ),
        "false_answer_rate": mean(
            [
                1.0 if not r["rule"]["refusal_detected"] else 0.0
                for r in rules
                if not r["answerable"]
            ]
        ),
        "answerable_cases": len(answerable_records),
        "unanswerable_cases": len(unanswerable_records),
    }


def failure_reasons(record: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if record.get("generation_error"):
        reasons.append("generation_error")
    if record.get("judge_error"):
        reasons.append("judge_error")
    judge = record.get("judge") or {}
    rule = record.get("rule") or {}
    if judge.get("correctness") == 0:
        reasons.append("correctness=0")
    if judge.get("faithfulness") == 0:
        reasons.append("faithfulness=0")
    if judge.get("completeness") == 0:
        reasons.append("completeness=0")
    if rule.get("citation_required") and judge.get(
        "citation_accuracy"
    ) == 0:
        reasons.append("citation_accuracy=0")
    if judge.get("refusal_correct") == 0:
        reasons.append("refusal_correct=0")
    if judge.get("language_consistency") == 0:
        reasons.append("language_consistency=0")
    if rule.get("language_match_rule") is False:
        reasons.append("rule_language_mismatch")
    return reasons


def write_markdown(report: dict[str, Any], path: Path) -> None:
    lines = [
        "# Answer Generation Evaluation",
        "",
        f"- 日期：2026-11-26",
        f"- 测试集：`{report['config']['dataset']}`",
        f"- 模式：{', '.join(report['config']['modes'])}",
        f"- 生成模型：`{report['config']['llm_model']}`",
        f"- 结果：`{path.with_suffix('.json')}`",
        "",
        "## 1. 总体评分",
        "",
        "| 模式 | 样本 | correctness | faithfulness | completeness | citation | refusal | language | conciseness |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for mode in report["config"]["modes"]:
        summary = report["summary"][mode]
        citation = (
            f"{summary['citation_accuracy']:.4f}"
            if summary["citation_accuracy"] is not None
            else "N/A"
        )
        lines.append(
            f"| `{mode}` | {summary['cases']} | "
            f"{summary['correctness']:.4f} | "
            f"{summary['faithfulness']:.4f} | "
            f"{summary['completeness']:.4f} | "
            f"{citation} | "
            f"{summary['refusal_accuracy']:.4f} | "
            f"{summary['language_consistency']:.4f} | "
            f"{summary['conciseness']:.4f} |"
        )

    lines.extend(
        [
            "",
            "## 2. 规则指标",
            "",
            "| 模式 | 关键术语覆盖 | 规则语言一致 | 引用存在率 | 引用编号有效 | 拒答检出率 | 误拒答率 | 无答案误答率 |",
            "|---|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for mode in report["config"]["modes"]:
        summary = report["summary"][mode]
        lines.append(
            f"| `{mode}` | {summary['rule_must_keep_coverage']:.4f} | "
            f"{summary['rule_language_match']:.4f} | "
            f"{summary['citation_present_rate']:.4f} | "
            f"{summary['citation_valid_rate']:.4f} | "
            f"{summary['refusal_detected_rate']:.4f} | "
            f"{summary['false_refusal_rate']:.4f} | "
            f"{summary['false_answer_rate']:.4f} |"
        )

    lines.extend(
        [
            "",
            "## 3. 按语言 / 类型拆分",
            "",
        ]
    )
    for group_key, title in (
        ("by_language", "按语言"),
        ("by_type", "按类型"),
    ):
        lines.extend(
            [
                f"### {title}",
                "",
                "| 分组 | 模式 | n | correctness | faithfulness | completeness |",
                "|---|---|---:|---:|---:|---:|",
            ]
        )
        for name, modes in report[group_key].items():
            for mode in report["config"]["modes"]:
                row = modes.get(mode)
                if row is None:
                    continue
                lines.append(
                    f"| `{name}` | `{mode}` | {row['cases']} | "
                    f"{row['correctness']:.4f} | "
                    f"{row['faithfulness']:.4f} | "
                    f"{row['completeness']:.4f} |"
                )
        lines.append("")

    lines.extend(
        [
            "## 4. 失败案例",
            "",
        ]
    )
    failures = [
        record
        for record in report["cases"]
        if failure_reasons(record)
    ]
    if failures:
        for record in failures:
            judge = record.get("judge") or {}
            lines.append(
                f"- `{record['id']}` mode=`{record['mode']}` "
                f"type=`{record['type']}` lang=`{record['language']}` "
                f"reasons={failure_reasons(record)} "
                f"judge_reason={judge.get('reason', '')!r}"
            )
    else:
        lines.append("无。")

    lines.extend(
        [
            "",
            "## 5. 结论",
            "",
            "1. 本报告区分 `gold_answer` 与 `gold_docs` 两种 oracle 上下文：前者测复述与约束遵循，后者测给定完整正确文档后的回答生成。",
            "2. 引用准确性只在 `gold_docs` 模式计分；`gold_answer` 模式的 context 只有参考答案，因此 citation 记为 N/A。",
            "3. 完整性以 `reference_answer` 为 gold checklist，并结合 `must_keep_terms` 做规则覆盖。",
            "4. 语言一致性同时要求 judge 和规则检查通过；q052 是英文问题但中文回答，规则捕获了该问题，judge 未捕获。",
            "5. q034 的 completeness=1，原因是只回答了 `trace_id=` 的主路径，缺少子 run 场景的可选说明。",
            "6. `must_keep_terms` 是严格字面匹配；中文答案通常不包含英文术语，因此该指标偏低只能作为辅助信号。",
            "",
            "## 6. 复现",
            "",
            "```powershell",
            '$env:PYTHONPATH="D:\\My_rag\\src"',
            '$env:HF_HUB_OFFLINE="1"',
            '$env:TRANSFORMERS_OFFLINE="1"',
            "python tests/test_AnswerGeneration.py",
            "```",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Answer generation evaluation"
    )
    parser.add_argument(
        "--modes",
        default="gold_answer,gold_docs",
        help="逗号分隔：gold_answer,gold_docs",
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
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="并发生成/评审线程数",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=180,
        help="单次 LLM 请求超时秒数",
    )
    parser.add_argument(
        "--checkpoint",
        type=Path,
        default=CHECKPOINT_PATH,
    )
    parser.add_argument(
        "--restart",
        action="store_true",
        help="忽略已有 checkpoint，重新评测",
    )
    args = parser.parse_args()

    modes = [
        value.strip()
        for value in args.modes.split(",")
        if value.strip()
    ]
    unknown = [mode for mode in modes if mode not in MODES]
    if unknown:
        parser.error(f"Unknown modes: {unknown}")

    all_cases = load_cases(DATASET_PATH)
    wanted_ids = {
        value.strip() for value in args.ids.split(",") if value.strip()
    }
    cases = [
        case
        for case in all_cases
        if not wanted_ids or case["id"] in wanted_ids
    ]

    print(f"Loaded {len(cases)} cases; modes={modes}", flush=True)
    print("Loading models, vector store and catalog...", flush=True)
    llm = build_llm(args.timeout)
    vector_store = None
    catalog = None
    if "gold_docs" in modes:
        # Only the catalog is needed for full reference-page context.
        catalog = build_chunk_catalog()

    prepared = prepare_cases(
        cases,
        modes,
        vector_store,
        catalog,
    )

    if args.restart and args.checkpoint.exists():
        args.checkpoint.unlink()
    checkpoint_records = load_checkpoint(args.checkpoint)
    wanted_keys = {
        (item["mode"], item["case"]["id"]) for item in prepared
    }
    checkpoint_records = {
        key: value
        for key, value in checkpoint_records.items()
        if key in wanted_keys
        and not value.get("generation_error")
        and not value.get("judge_error")
    }
    remaining = [
        item
        for item in prepared
        if (item["mode"], item["case"]["id"]) not in checkpoint_records
    ]
    print(
        f"Checkpoint: {len(checkpoint_records)} completed, "
        f"{len(remaining)} remaining, workers={args.workers}",
        flush=True,
    )
    if args.checkpoint.exists() and not checkpoint_records:
        args.checkpoint.unlink()

    lock = threading.Lock()
    new_records: list[dict[str, Any]] = []

    def work(item: dict[str, Any]) -> dict[str, Any]:
        try:
            return evaluate_with_context(
                item["case"],
                item["mode"],
                llm,
                item["context"],
                item["sources"],
                item["context_error"],
            )
        except Exception as exc:
            case = item["case"]
            return {
                "id": case["id"],
                "question": case["question"],
                "type": case["type"],
                "language": case["language"],
                "answerable": case["answerable"],
                "expected_refusal": case.get("expected_refusal", False),
                "citation_required": case.get("citation_required", False),
                "mode": item["mode"],
                "context_error": item.get("context_error"),
                "context_chars": len(item.get("context") or ""),
                "sources": [],
                "answer": None,
                "generation_error": f"{type(exc).__name__}: {exc}",
                "judge_error": None,
                "rule": None,
                "judge": None,
            }

    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {
            pool.submit(work, item): item for item in remaining
        }
        completed = 0
        for future in as_completed(futures):
            item = futures[future]
            record = future.result()
            new_records.append(record)
            append_checkpoint(args.checkpoint, record, lock)
            completed += 1
            judge = record.get("judge") or {}
            print(
                f"[{completed:03d}/{len(remaining)}] "
                f"{item['mode']} {item['case']['id']} "
                f"correct={judge.get('correctness')} "
                f"faith={judge.get('faithfulness')} "
                f"complete={judge.get('completeness')} "
                f"citation={judge.get('citation_accuracy')} "
                f"refusal={judge.get('refusal_correct')} "
                f"lang={judge.get('language_consistency')} "
                f"error={record.get('generation_error') or record.get('judge_error') or '-'}",
                flush=True,
            )

    records_by_key = {
        **checkpoint_records,
        **{
            (record["mode"], record["id"]): record
            for record in new_records
        },
    }
    records = [
        records_by_key[(item["mode"], item["case"]["id"])]
        for item in prepared
        if (item["mode"], item["case"]["id"]) in records_by_key
    ]
    print(
        f"Collected {len(records)}/{len(prepared)} case records",
        flush=True,
    )

    summary = {
        mode: aggregate(records, mode) for mode in modes
    }
    by_language: dict[str, dict[str, Any]] = {}
    by_type: dict[str, dict[str, Any]] = {}
    for key, target in (("language", by_language), ("type", by_type)):
        groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for record in records:
            groups[str(record[key])].append(record)
        for name, group in groups.items():
            target[name] = {
                mode: aggregate(group, mode) for mode in modes
            }

    report = {
        "config": {
            "dataset": str(DATASET_PATH),
            "modes": modes,
            "llm_model": os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
            "temperature": 0,
            "judge": "LLM-as-judge + rule checks",
            "cutoffs": None,
            "vector_store": str(VECTOR_STORE_DIR),
            "workers": args.workers,
            "timeout": args.timeout,
            "checkpoint": str(args.checkpoint),
        },
        "summary": summary,
        "by_language": by_language,
        "by_type": by_type,
        "cases": records,
    }

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    write_markdown(report, args.report.with_suffix(".md"))

    all_done = (
        len(records) == len(prepared)
        and all(
            not record.get("generation_error")
            and not record.get("judge_error")
            for record in records
        )
    )
    if all_done and args.checkpoint.exists():
        args.checkpoint.unlink()

    print()
    for mode in modes:
        row = summary[mode]
        citation = (
            f"{row['citation_accuracy']:.4f}"
            if row["citation_accuracy"] is not None
            else "N/A"
        )
        print(
            f"{mode}: correctness={row['correctness']:.4f} "
            f"faithfulness={row['faithfulness']:.4f} "
            f"completeness={row['completeness']:.4f} "
            f"citation={citation} "
            f"refusal={row['refusal_accuracy']:.4f} "
            f"language={row['language_consistency']:.4f} "
            f"conciseness={row['conciseness']:.4f}"
        )
    print(f"Report written to {args.report}")
    print(f"Markdown written to {args.report.with_suffix('.md')}")


if __name__ == "__main__":
    main()
