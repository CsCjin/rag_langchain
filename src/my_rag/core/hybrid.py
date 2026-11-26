"""BM25 + dense hybrid retrieval with sibling expansion."""

from dataclasses import dataclass
from typing import Any

import numpy as np
from langchain_chroma import Chroma
from langchain_core.documents import Document

from my_rag.core.chunk_catalog import (
    ChunkCatalog,
    content_hash,
)
from my_rag.core.document_graph import DocumentGraph
from my_rag.model.reranker import build_reranker

DEFAULT_DENSE_WEIGHT = 0.7
DEFAULT_BM25_WEIGHT = 0.3
DEFAULT_CANDIDATE_K = 50
DEFAULT_COARSE_K = 20
DEFAULT_FINAL_K = 5


@dataclass
class HybridHit:
    document: Document
    fused_score: float
    dense_score: float
    bm25_score: float


def _min_max(values: list[float]) -> list[float]:
    if not values:
        return []
    low = min(values)
    high = max(values)
    if high - low < 1e-12:
        return [1.0 if high > 0 else 0.0 for _ in values]
    return [(value - low) / (high - low) for value in values]


def _dense_norm(distances: list[float]) -> list[float]:
    if not distances:
        return []
    low = min(distances)
    high = max(distances)
    if high - low < 1e-12:
        # All candidates are equally close; keep them all as best.
        return [1.0] * len(distances)
    return [
        1.0 - (distance - low) / (high - low)
        for distance in distances
    ]


def _document_key(document: Document) -> tuple[str, str]:
    doc_id = (
        document.metadata.get("doc_id")
        or document.metadata.get("url")
        or document.metadata.get("source")
    )
    digest = (
        document.metadata.get("content_hash")
        or content_hash(document.page_content)
    )
    return str(doc_id), str(digest)


def retrieve_hybrid(
    vector_store: Chroma,
    catalog: ChunkCatalog,
    query: str,
    candidate_k: int = DEFAULT_CANDIDATE_K,
    metadata_filter: dict[str, Any] | None = None,
    dense_weight: float = DEFAULT_DENSE_WEIGHT,
    bm25_weight: float = DEFAULT_BM25_WEIGHT,
) -> list[HybridHit]:
    """Retrieve and fuse dense and BM25 candidates.

    Dense distances and BM25 scores are normalized per query to [0, 1].
    The fused score is ``dense_weight * dense_norm + bm25_weight * bm25_norm``.
    """

    dense_results = vector_store.similarity_search_with_score(
        query,
        k=candidate_k,
        filter=metadata_filter,
    )
    dense_documents = [
        catalog.enrich(document) for document, _ in dense_results
    ]
    dense_distances = [float(distance) for _, distance in dense_results]
    dense_norm = _dense_norm(dense_distances)

    allowed_mask = catalog.metadata_mask(metadata_filter)
    bm25_results = catalog.bm25.search(
        query,
        k=candidate_k,
        allowed_mask=allowed_mask,
    )
    bm25_documents = [
        catalog.documents[index] for index, _ in bm25_results
    ]
    bm25_scores = [score for _, score in bm25_results]
    bm25_norm = _min_max(bm25_scores)

    fused: dict[tuple[str, str], HybridHit] = {}

    for document, norm in zip(dense_documents, dense_norm):
        key = _document_key(document)
        hit = fused.get(key)
        if hit is None:
            fused[key] = HybridHit(
                document=document,
                fused_score=0.0,
                dense_score=norm,
                bm25_score=0.0,
            )
        else:
            hit.dense_score = max(hit.dense_score, norm)

    for document, norm in zip(bm25_documents, bm25_norm):
        key = _document_key(document)
        hit = fused.get(key)
        if hit is None:
            fused[key] = HybridHit(
                document=document,
                fused_score=0.0,
                dense_score=0.0,
                bm25_score=norm,
            )
        else:
            hit.bm25_score = max(hit.bm25_score, norm)

    for hit in fused.values():
        hit.fused_score = (
            dense_weight * hit.dense_score
            + bm25_weight * hit.bm25_score
        )

    return sorted(
        fused.values(),
        key=lambda hit: hit.fused_score,
        reverse=True,
    )


def retrieve_hybrid_with_rerank(
    vector_store: Chroma,
    catalog: ChunkCatalog,
    query: str,
    candidate_k: int = DEFAULT_CANDIDATE_K,
    coarse_k: int = DEFAULT_COARSE_K,
    final_k: int = DEFAULT_FINAL_K,
    metadata_filter: dict[str, Any] | None = None,
    doc_type_penalties: dict[str, float] | None = None,
    expand_siblings: bool = True,
    sibling_window: int = 2,
    max_chars: int = 3000,
    dense_weight: float = DEFAULT_DENSE_WEIGHT,
    bm25_weight: float = DEFAULT_BM25_WEIGHT,
    diversify_urls: bool = True,
    document_graph: DocumentGraph | None = None,
    graph_window: int = 3,
    graph_max_sections: int = 8,
    graph_max_chars: int = 3000,
    graph_include_same_topic: bool = True,
) -> list[Document]:
    """Hybrid retrieval, coarse rerank, sibling expansion, final rerank."""

    hits = retrieve_hybrid(
        vector_store,
        catalog,
        query,
        candidate_k=candidate_k,
        metadata_filter=metadata_filter,
        dense_weight=dense_weight,
        bm25_weight=bm25_weight,
    )
    if not hits:
        return []

    candidates = [hit.document for hit in hits]
    coarse_documents = build_reranker(
        top_n=min(coarse_k, len(candidates)),
        penalties=doc_type_penalties,
    ).compress_documents(candidates, query)

    if not coarse_documents:
        return []

    # Keep both the original hit chunks and their merged parent blocks in
    # the final rerank pool. A merged parent helps comparison questions, but
    # a precise single chunk can be better for focused how-to questions.
    expanded_documents: list[Document] = []
    if expand_siblings:
        expanded_documents = catalog.expand_siblings(
            coarse_documents,
            max_chars=max_chars,
            window=sibling_window,
        )

    graph_documents: list[Document] = []
    if document_graph is not None:
        graph_documents = document_graph.expand_sections(
            coarse_documents,
            window=graph_window,
            max_sections=graph_max_sections,
            max_chars=graph_max_chars,
            include_same_topic=graph_include_same_topic,
        )

    rerank_pool: list[Document] = []
    seen_keys: set[tuple[str, str]] = set()
    for document in [
        *coarse_documents,
        *expanded_documents,
        *graph_documents,
    ]:
        key = _document_key(document)
        if key in seen_keys:
            continue
        seen_keys.add(key)
        rerank_pool.append(document)

    if not rerank_pool:
        return []

    # Rerank a slightly larger pool, then keep at most one chunk per URL.
    # This prevents several near-duplicate chunks from the same page from
    # taking all final slots.
    reranked = list(
        build_reranker(
            top_n=max(final_k * 3, 15),
            penalties=doc_type_penalties,
        ).compress_documents(rerank_pool, query)
    )

    if not diversify_urls:
        return reranked[:final_k]

    selected: list[Document] = []
    seen_urls: set[str] = set()
    for document in reranked:
        key = (
            document.metadata.get("url")
            or document.metadata.get("doc_id")
            or document.metadata.get("source")
        )
        key = str(key)
        if key in seen_urls:
            continue
        selected.append(document)
        seen_urls.add(key)
        if len(selected) >= final_k:
            break

    if len(selected) < final_k:
        selected_ids = {id(document) for document in selected}
        for document in reranked:
            if id(document) in selected_ids:
                continue
            selected.append(document)
            if len(selected) >= final_k:
                break

    return selected[:final_k]
