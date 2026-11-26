"""Chunk catalog, BM25 index and sibling expansion.

The catalog is built from the same markdown splitter used to build the vector
store. It provides:

- a deduplicated chunk view for BM25 and sibling expansion;
- a ``(doc_id, content_hash)`` lookup to enrich dense-retrieval hits with
  parent/section metadata;
- a BM25 index with optional metadata filtering;
- sibling expansion by ``parent_id``.
"""

import hashlib
import pickle
import re
import time
from collections import defaultdict
from pathlib import Path
from typing import Any

import numpy as np
from langchain_core.documents import Document
from sklearn.feature_extraction.text import CountVectorizer

from my_rag.config import DOCS_DIR, PROJECT_ROOT
from my_rag.ingestion.splitter import load_and_split

CACHE_VERSION = 1
DEFAULT_CACHE_PATH = (
    PROJECT_ROOT / "data" / "cache" / "chunk_catalog.pkl"
)

TOKEN_PATTERN = re.compile(
    r"[A-Za-z_][A-Za-z0-9_.\-]*|\d+(?:\.\d+)*|[\u4e00-\u9fff]"
)


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in TOKEN_PATTERN.findall(text or "")]


def content_hash(text: str) -> str:
    return hashlib.sha1((text or "").strip().encode("utf-8")).hexdigest()


class BM25Index:
    """Minimal BM25Okapi implementation over a sparse document-term matrix."""

    def __init__(
        self,
        documents: list[Document],
        k1: float = 1.5,
        b: float = 0.75,
    ) -> None:
        self.k1 = k1
        self.b = b
        self.documents = documents
        texts = [document.page_content for document in documents]
        self.vectorizer = CountVectorizer(
            analyzer=tokenize,
            dtype=np.int32,
        )
        self.matrix = self.vectorizer.fit_transform(texts)
        self.n_docs = self.matrix.shape[0]
        self.doc_len = np.asarray(
            self.matrix.sum(axis=1)
        ).ravel().astype(float)
        self.avgdl = (
            float(self.doc_len.mean()) if self.n_docs else 0.0
        )
        document_frequency = np.bincount(
            self.matrix.indices,
            minlength=self.matrix.shape[1],
        )
        self.idf = np.log(
            (self.n_docs - document_frequency + 0.5)
            / (document_frequency + 0.5)
            + 1.0
        )
        self.vocabulary = self.vectorizer.vocabulary_

    def search(
        self,
        query: str,
        k: int = 50,
        allowed_mask: np.ndarray | None = None,
    ) -> list[tuple[int, float]]:
        if self.n_docs == 0:
            return []

        scores = np.zeros(self.n_docs, dtype=float)
        for term in tokenize(query):
            term_index = self.vocabulary.get(term)
            if term_index is None:
                continue

            column = (
                self.matrix[:, term_index]
                .toarray()
                .ravel()
                .astype(float)
            )
            non_zero = column > 0
            if allowed_mask is not None:
                non_zero &= allowed_mask
            if not np.any(non_zero):
                continue

            denominator = column[non_zero] + self.k1 * (
                1.0
                - self.b
                + self.b * self.doc_len[non_zero] / self.avgdl
            )
            scores[non_zero] += (
                self.idf[term_index]
                * column[non_zero]
                * (self.k1 + 1.0)
                / denominator
            )

        if allowed_mask is not None:
            scores[~allowed_mask] = -np.inf

        finite_scores = np.isfinite(scores)
        if not np.any(finite_scores):
            return []

        k = min(k, int(np.count_nonzero(finite_scores)))
        if k <= 0:
            return []
        if k >= self.n_docs:
            top_indices = np.argsort(scores)[::-1][:k]
        else:
            top_indices = np.argpartition(scores, -k)[-k:]
            top_indices = top_indices[
                np.argsort(scores[top_indices])[::-1]
            ]

        return [
            (int(index), float(scores[index]))
            for index in top_indices
            if np.isfinite(scores[index])
        ]


def dedupe_documents(documents: list[Document]) -> list[Document]:
    """Deduplicate chunks by page, parent section and content hash.

    Identical text can legitimately appear under different parent sections,
    so ``parent_id`` is part of the key. The function also backfills the
    metadata needed by the sibling merge logic.
    """
    deduped: list[Document] = []
    seen: set[tuple[str, str, str]] = set()
    for document in documents:
        doc_id = (
            document.metadata.get("doc_id")
            or document.metadata.get("url")
            or document.metadata.get("source")
        )
        digest = (
            document.metadata.get("content_hash")
            or content_hash(document.page_content)
        )
        parent_id = str(
            document.metadata.get("parent_id") or doc_id
        )
        key = (str(doc_id), parent_id, str(digest))
        if key in seen:
            continue
        seen.add(key)

        metadata = {
            **document.metadata,
            "doc_id": doc_id,
            "content_hash": digest,
        }
        metadata.setdefault(
            "parent_id",
            doc_id,
        )
        metadata.setdefault(
            "section_index",
            0,
        )
        metadata.setdefault(
            "chunk_index",
            len(deduped),
        )
        deduped.append(
            Document(
                page_content=document.page_content,
                metadata=metadata,
            )
        )
    return deduped


class ChunkCatalog:
    """Deduplicated chunk view with parent/sibling operations."""

    def __init__(self, documents: list[Document]) -> None:
        self.documents = dedupe_documents(documents)
        self.by_key: dict[tuple[str, str], int] = {}
        self.parent_groups: dict[tuple[str, str], list[int]] = defaultdict(
            list
        )
        for index, document in enumerate(self.documents):
            doc_id = str(document.metadata.get("doc_id"))
            digest = str(document.metadata.get("content_hash"))
            self.by_key[(doc_id, digest)] = index
            parent_id = str(document.metadata.get("parent_id"))
            self.parent_groups[(doc_id, parent_id)].append(index)

        for indices in self.parent_groups.values():
            indices.sort(
                key=lambda index: self.documents[index].metadata.get(
                    "chunk_index", 0
                )
            )

        self.bm25 = BM25Index(self.documents)

    @staticmethod
    def _matches(
        metadata: dict[str, Any],
        filter_: Any,
    ) -> bool:
        if not filter_:
            return True
        if not isinstance(filter_, dict):
            return True

        for key, value in filter_.items():
            if key == "$and":
                if not all(
                    ChunkCatalog._matches(metadata, item)
                    for item in value
                ):
                    return False
                continue
            if key == "$or":
                if not any(
                    ChunkCatalog._matches(metadata, item)
                    for item in value
                ):
                    return False
                continue

            actual = metadata.get(key)
            if isinstance(value, dict):
                for operator, operand in value.items():
                    if operator == "$eq" and actual != operand:
                        return False
                    if operator == "$ne" and actual == operand:
                        return False
                    if operator == "$in" and actual not in operand:
                        return False
                    if operator == "$nin" and actual in operand:
                        return False
                    if operator == "$gt" and not (
                        actual is not None and actual > operand
                    ):
                        return False
                    if operator == "$gte" and not (
                        actual is not None and actual >= operand
                    ):
                        return False
                    if operator == "$lt" and not (
                        actual is not None and actual < operand
                    ):
                        return False
                    if operator == "$lte" and not (
                        actual is not None and actual <= operand
                    ):
                        return False
                continue

            if actual != value:
                return False

        return True

    def metadata_mask(self, filter_: Any) -> np.ndarray | None:
        if not filter_:
            return None
        return np.asarray(
            [
                self._matches(document.metadata, filter_)
                for document in self.documents
            ],
            dtype=bool,
        )

    def enrich(self, document: Document) -> Document:
        """Attach catalog metadata to a dense-retrieval document."""
        digest = (
            document.metadata.get("content_hash")
            or content_hash(document.page_content)
        )
        candidates = [
            (
                document.metadata.get("doc_id")
                or document.metadata.get("url")
                or document.metadata.get("source"),
                digest,
            ),
            (document.metadata.get("url"), digest),
            (document.metadata.get("source"), digest),
        ]
        for key in candidates:
            if key[0] is None:
                continue
            index = self.by_key.get((str(key[0]), str(key[1])))
            if index is not None:
                metadata = {
                    **document.metadata,
                    **self.documents[index].metadata,
                }
                return Document(
                    page_content=document.page_content,
                    metadata=metadata,
                )
        return document

    def expand_siblings(
        self,
        documents: list[Document],
        max_chars: int = 3000,
        window: int = 1,
    ) -> list[Document]:
        """Merge sibling chunks under the same parent heading."""
        groups: dict[tuple[str, str], list[Document]] = defaultdict(list)
        for document in documents:
            doc_id = document.metadata.get("doc_id")
            parent_id = document.metadata.get("parent_id")
            if doc_id is None or parent_id is None:
                continue
            groups[(str(doc_id), str(parent_id))].append(document)

        expanded: list[Document] = []
        for (doc_id, parent_id), hits in groups.items():
            indices = self.parent_groups.get((doc_id, parent_id), [])
            siblings = [self.documents[index] for index in indices]
            if not siblings:
                expanded.extend(hits)
                continue

            all_text = "\n\n".join(
                sibling.page_content for sibling in siblings
            )
            if len(all_text) <= max_chars:
                selected = siblings
            else:
                hit_sections = {
                    hit.metadata.get("section_index", -999)
                    for hit in hits
                }
                selected = [
                    sibling
                    for sibling in siblings
                    if any(
                        abs(
                            sibling.metadata.get(
                                "section_index", -999
                            )
                            - hit_section
                        )
                        <= window
                        for hit_section in hit_sections
                    )
                ]
                if not selected:
                    selected = hits

            seen_hashes: set[str] = set()
            parts: list[str] = []
            for sibling in selected:
                digest = str(
                    sibling.metadata.get("content_hash")
                    or content_hash(sibling.page_content)
                )
                if digest in seen_hashes:
                    continue
                seen_hashes.add(digest)
                parts.append(sibling.page_content)

            merged = "\n\n".join(parts)[:max_chars]
            if not merged:
                continue

            metadata = {
                **hits[0].metadata,
                "doc_id": doc_id,
                "parent_id": parent_id,
                "merged_sibling_count": len(selected),
            }
            expanded.append(
                Document(
                    page_content=merged,
                    metadata=metadata,
                )
            )

        return expanded


def _source_fingerprint(
    docs_dir: Path = DOCS_DIR,
) -> dict[str, Any]:
    files = list(docs_dir.rglob("*.md"))
    if not files:
        return {
            "file_count": 0,
            "max_mtime": 0.0,
            "total_size": 0,
        }
    return {
        "file_count": len(files),
        "max_mtime": max(path.stat().st_mtime for path in files),
        "total_size": sum(path.stat().st_size for path in files),
    }


def build_chunk_catalog(
    documents: list[Document] | None = None,
    cache_path: Path | None = DEFAULT_CACHE_PATH,
    force_rebuild: bool = False,
) -> ChunkCatalog:
    """Build or load the deduplicated chunk catalog and BM25 cache."""
    fingerprint = _source_fingerprint()

    if cache_path and cache_path.exists() and not force_rebuild:
        try:
            with cache_path.open("rb") as handle:
                payload = pickle.load(handle)
            if (
                isinstance(payload, dict)
                and payload.get("version") == CACHE_VERSION
                and payload.get("fingerprint") == fingerprint
                and isinstance(payload.get("catalog"), ChunkCatalog)
            ):
                print(f"Loaded chunk catalog cache: {cache_path}")
                return payload["catalog"]
        except Exception as exc:
            print(f"Chunk catalog cache invalid, rebuilding: {exc}")

    if documents is None:
        documents = load_and_split()

    catalog = ChunkCatalog(documents)

    if cache_path:
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "version": CACHE_VERSION,
            "fingerprint": fingerprint,
            "created_at": time.time(),
            "chunk_count": len(catalog.documents),
            "catalog": catalog,
        }
        with cache_path.open("wb") as handle:
            pickle.dump(
                payload,
                handle,
                protocol=pickle.HIGHEST_PROTOCOL,
            )
        print(
            f"Saved chunk catalog cache: {cache_path} "
            f"({len(catalog.documents)} chunks)"
        )

    return catalog
