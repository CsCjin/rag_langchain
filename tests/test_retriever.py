import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any

from langchain_chroma import Chroma
from langchain_core.documents import Document

from my_rag.config import PROJECT_ROOT, VECTOR_STORE_DIR
from my_rag.core.retriever import retrieve_documents
from my_rag.core.vector_store import load_vector_store
from my_rag.model.embedding import get_embedding_model

DATASET_PATH = PROJECT_ROOT / "tests" / "evaluation" / "qa_set.jsonl"
REPORT_PATH = PROJECT_ROOT / "tests" / "evaluation" / "retrieval_report.json"


def load_cases(path: Path) -> list[dict[str, Any]]: # 加载测试用例
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines() # read_text()函数作用和open类似
        if line.strip()
    ]


def dedupe_urls(documents: list[Document]) -> list[str]: # 返回检索结果的list of urls
    urls: list[str] = []
    seen: set[str] = set()
    for document in documents:
        url = document.metadata.get("url")
        if url and url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def evaluate_cases(
    cases: list[dict[str, Any]],
    vector_store: Chroma,
    max_k: int,
) -> list[dict[str, Any]]: # 收集原始检索结果
    records: list[dict[str, Any]] = []
    for index, case in enumerate(cases, start=1): # case代表一个具体的测试用例
        documents = retrieve_documents(
            vector_store,
            case["question"],
            k=max_k,
        )
        urls = dedupe_urls(documents)
        relevant_urls = set(case["relevant_urls"]) # 测试用例的参考URL
        rank = next(
            (position for position, url in enumerate(urls, start=1) if url in relevant_urls),
            None,
        ) # 返回第一个命中的url的rank，值越小代表越早命中，检索的性能越好
        records.append(
            {
                "id": case["id"],
                "question": case["question"],
                "type": case["type"],
                "language": case["language"],
                "relevant_urls": list(relevant_urls),
                "retrieved_urls": urls,
                "rank": rank,
            }
        )
        if index % 10 == 0 or index == len(cases):
            print(f"  evaluated {index}/{len(cases)}")
    return records


def score_records(records: list[dict[str, Any]], cutoff: int) -> dict[str, float]: # cutoff表示截断位置
    count = len(records) # records为evaluate函数中的返回结果，列表中的元素代表检索的结果和命中位置
    if count == 0: # 表示未命中
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

    for record in records: # 计算指标
        urls = record["retrieved_urls"][:cutoff] # 截断位置
        relevant = set(record["relevant_urls"])
        matched = sum(1 for url in urls if url in relevant)
        if matched > 0:
            hits += 1
        if relevant:
            recall += matched / len(relevant)

        rank = record["rank"]
        if rank is not None and rank <= cutoff:
            reciprocal_rank += 1.0 / rank

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
    } # 对所有计算结果取平均，得到测试指标


def group_records(
    records: list[dict[str, Any]],
    key: str,
) -> dict[str, list[dict[str, Any]]]: # 按照字段分组，方便维护指标
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list) # 如果键值不存在则自动创建
    for record in records:
        groups[str(record[key])].append(record)
    return dict(groups) # 按照特定字段分组之后，key是该字段的不同值，value是这个值之下的list of record


def print_metrics_table(records: list[dict[str, Any]], cutoffs: list[int]) -> None:
    print()
    print(f"{'k':>4} {'Hit@k':>8} {'Recall@k':>10} {'MRR@k':>8} {'nDCG@k':>8}")
    # f string格式，右对齐
    for cutoff in cutoffs: # 针对每一次截断，调用一次计算指标函数，截断的是retrieved url
        metrics = score_records(records, cutoff) # 调用打分函数，返回打分dict
        print(
            f"{cutoff:>4} "
            f"{metrics['hit_rate']:>8.4f} "
            f"{metrics['recall']:>10.4f} "
            f"{metrics['mrr']:>8.4f} "
            f"{metrics['ndcg']:>8.4f}"
        ) # :>代表右对齐函数


def print_breakdown(
    records: list[dict[str, Any]],
    key: str,
    cutoff: int,
) -> None:
    print()
    print(f"By {key} @{cutoff}")
    groups = group_records(records, key) # 返回分组后的dict， key为分组的标准
    for name in sorted(groups): # 调用key
        metrics = score_records(groups[name], cutoff) # 计算指标
        print(
            f"  {name:<16} n={int(metrics['count']):>3} "
            f"Hit={metrics['hit_rate']:.4f} "
            f"MRR={metrics['mrr']:.4f} "
            f"nDCG={metrics['ndcg']:.4f}"
        )


def print_failures(
    records: list[dict[str, Any]],
    cutoff: int,
    limit: int,
) -> None:
    failures = [
        record
        for record in records
        if record["rank"] is None or record["rank"] > cutoff
    ] # 收集没有检索到内容的案例，或者第一个命中超过cutoff的案例
    print()
    print(f"Failures @{cutoff}: {len(failures)}/{len(records)}") # 计算占比
    for record in failures[:limit]: # limit为限制输出的数量
        print(f"- {record['id']} rank={record['rank']} | {record['question'][:120]}")
        print(f"  relevant: {record['relevant_urls']}") # 实际相关
        print(f"  top3: {record['retrieved_urls'][:3]}") # 检索到的


def main() -> None: # 整合流程
    parser = argparse.ArgumentParser(description="纯向量检索评测（不含 Self-query）")
    parser.add_argument("--dataset", type=Path, default=DATASET_PATH)
    parser.add_argument("--cutoffs", default="1,3,5,10")
    parser.add_argument("--breakdown-k", type=int, default=5)
    parser.add_argument("--failures", type=int, default=10)
    parser.add_argument("--report", type=Path, default=REPORT_PATH)
    args = parser.parse_args() # 启动明铃兰读取器

    cutoffs = sorted({int(value) for value in args.cutoffs.split(",") if value.strip()})
    max_k = max(cutoffs)
    # 使用命令行参数解析器，可以通过解析器修改测试参数，不需要修改源码，方便测试

    cases = load_cases(args.dataset)
    answerable = [
        case
        for case in cases
        if case["answerable"] and case["relevant_urls"]
    ] # 收集可以回答的问题
    print(f"Loaded {len(cases)} cases, evaluating {len(answerable)} answerable cases")
    print(f"Excluded {len(cases) - len(answerable)} unanswerable/invalid cases")
    # 对于无法回答的问题，在这里不进行测试，因为检索必然为空

    print("Loading embedding model and vector store...")
    embeddings = get_embedding_model()
    vector_store = load_vector_store(VECTOR_STORE_DIR, embeddings)

    records = evaluate_cases(answerable, vector_store, max_k)

    print_metrics_table(records, cutoffs)
    print_breakdown(records, "type", args.breakdown_k) # 根据问题计算得分
    print_breakdown(records, "language", args.breakdown_k) # 根据语言计算得分
    print_failures(records, args.breakdown_k, args.failures) #

    report = {
        "dataset": str(args.dataset),
        "vector_store": str(VECTOR_STORE_DIR),
        "max_k": max_k,
        "cutoffs": cutoffs,
        "evaluated": len(records),
        "excluded": len(cases) - len(answerable),
        "metrics": {
            str(cutoff): score_records(records, cutoff)
            for cutoff in cutoffs
        },
        "breakdown": {
            "type": {
                name: score_records(group, args.breakdown_k)
                for name, group in group_records(records, "type").items()
            },
            "language": {
                name: score_records(group, args.breakdown_k)
                for name, group in group_records(records, "language").items()
            },
        },
        "cases": records,
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8",
    ) # 绘制简报
    print()
    print(f"Report written to {args.report}")


if __name__ == "__main__":
    main()
