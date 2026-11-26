"""Document structure graph and retrieval-time context expansion.

The graph is intentionally built from the existing chunk metadata
(``doc_id``, ``parent_id``, ``section_index``, ``chunk_index``) instead of
LLM-extracted entities. It is a lightweight, deterministic graph layer:

Page -> Section -> Chunk
Chunk -> next chunk
Section -> next section
Page -> same-topic page (Python/JavaScript variants)

In production this graph can be persisted in Neo4j / Kuzu; for the current
prototype NetworkX keeps the implementation local and dependency-free beyond
the existing environment.
"""

from collections import defaultdict
from typing import Any

import networkx as nx
from langchain_core.documents import Document

from my_rag.core.chunk_catalog import (
    ChunkCatalog,
    content_hash as make_content_hash,
)

SectionKey = tuple[str, str, int]


def canonical_topic_url(url: str) -> str:
    """Normalize Python/JavaScript variants to a stable topic key."""
    url = url or ""
    replacements = (
        ("/oss/javascript/", "/oss/python/"),
        ("/langsmith/javascript/", "/langsmith/python/"),
        ("/oss/js/", "/oss/python/"),
    )
    for old, new in replacements:
        url = url.replace(old, new)
    return url


class DocumentGraph:
    """Structure graph built from the deduplicated chunk catalog."""

    def __init__(self, catalog: ChunkCatalog) -> None:
        self.catalog = catalog
        self.graph = nx.Graph()
        self.section_chunks: dict[SectionKey, list[Document]] = defaultdict(
            list
        )
        self.page_sections: dict[str, list[SectionKey]] = defaultdict(list)
        self.section_nodes: dict[SectionKey, tuple[Any, ...]] = {}
        self.page_nodes: dict[str, tuple[Any, ...]] = {}
        self.same_topic_pages: dict[str, set[str]] = defaultdict(set)

        for document in catalog.documents:
            metadata = document.metadata
            doc_id = str(
                metadata.get("doc_id")
                or metadata.get("url")
                or metadata.get("source")
            )
            parent_id = str(metadata.get("parent_id") or doc_id)
            section_index = int(metadata.get("section_index", 0))
            chunk_index = int(metadata.get("chunk_index", 0))
            digest = str(
                metadata.get("content_hash")
                or make_content_hash(document.page_content)
            )

            section_key: SectionKey = (
                doc_id,
                parent_id,
                section_index,
            )
            page_node = ("page", doc_id)
            section_node = ("section", doc_id, parent_id, section_index)
            chunk_node = ("chunk", doc_id, digest)

            if doc_id not in self.page_nodes:
                self.page_nodes[doc_id] = page_node
                self.graph.add_node(
                    page_node,
                    kind="page",
                    doc_id=doc_id,
                    url=metadata.get("url"),
                    title=metadata.get("title"),
                    doc_type=metadata.get("doc_type"),
                    platform=metadata.get("platform"),
                )

            if section_key not in self.section_nodes:
                self.section_nodes[section_key] = section_node
                self.graph.add_node(
                    section_node,
                    kind="section",
                    doc_id=doc_id,
                    parent_id=parent_id,
                    section_index=section_index,
                    h1=metadata.get("h1"),
                    h2=metadata.get("h2"),
                    h3=metadata.get("h3"),
                )
                self.page_sections[doc_id].append(section_key)
                self.graph.add_edge(
                    page_node,
                    section_node,
                    type="HAS_SECTION",
                )

            self.graph.add_node(
                chunk_node,
                kind="chunk",
                doc_id=doc_id,
                content_hash=digest,
                chunk_index=chunk_index,
            )
            self.graph.add_edge(
                section_node,
                chunk_node,
                type="HAS_CHUNK",
            )
            self.section_chunks[section_key].append(document)

        for section_key, documents in self.section_chunks.items():
            documents.sort(
                key=lambda document: document.metadata.get(
                    "chunk_index", 0
                )
            )
            for previous, current in zip(documents, documents[1:]):
                previous_node = (
                    "chunk",
                    section_key[0],
                    previous.metadata.get("content_hash")
                    or make_content_hash(previous.page_content),
                )
                current_node = (
                    "chunk",
                    section_key[0],
                    current.metadata.get("content_hash")
                    or make_content_hash(current.page_content),
                )
                self.graph.add_edge(
                    previous_node,
                    current_node,
                    type="NEXT_CHUNK",
                )

        for doc_id, sections in self.page_sections.items():
            sections.sort(key=lambda key: key[2])
            for previous, current in zip(sections, sections[1:]):
                self.graph.add_edge(
                    self.section_nodes[previous],
                    self.section_nodes[current],
                    type="NEXT_SECTION",
                )

        # Link Python/JavaScript variants of the same documentation topic.
        topic_pages: dict[str, list[str]] = defaultdict(list)
        for doc_id, node in self.page_nodes.items():
            url = self.graph.nodes[node].get("url") or ""
            if url:
                topic_pages[canonical_topic_url(url)].append(doc_id)
        for doc_ids in topic_pages.values():
            for index, left in enumerate(doc_ids):
                for right in doc_ids[index + 1 :]:
                    if left == right:
                        continue
                    self.same_topic_pages[left].add(right)
                    self.same_topic_pages[right].add(left)
                    self.graph.add_edge(
                        self.page_nodes[left],
                        self.page_nodes[right],
                        type="SAME_TOPIC_AS",
                    )

    def stats(self) -> dict[str, int]:
        return {
            "nodes": self.graph.number_of_nodes(),
            "edges": self.graph.number_of_edges(),
            "pages": len(self.page_nodes),
            "sections": len(self.section_nodes),
            "chunks": sum(
                len(documents)
                for documents in self.section_chunks.values()
            ),
            "same_topic_links": sum(
                len(pages) for pages in self.same_topic_pages.values()
            ) // 2,
        }

    def _section_shape(
        self,
        section_key: SectionKey,
    ) -> tuple[Any, Any, Any, int]:
        attributes = self.graph.nodes[self.section_nodes[section_key]]
        return (
            attributes.get("h1"),
            attributes.get("h2"),
            attributes.get("h3"),
            section_key[2],
        )

    def _merge_section(
        self,
        section_key: SectionKey,
        max_chars: int,
    ) -> Document | None:
        documents = self.section_chunks.get(section_key, [])
        if not documents:
            return None

        seen_hashes: set[str] = set()
        parts: list[str] = []
        for document in documents:
            digest = str(
                document.metadata.get("content_hash")
                or make_content_hash(document.page_content)
            )
            if digest in seen_hashes:
                continue
            seen_hashes.add(digest)
            parts.append(document.page_content)
            if sum(len(part) for part in parts) >= max_chars:
                break

        content = "\n\n".join(parts)[:max_chars]
        if not content:
            return None

        first = documents[0]
        metadata = {
            **first.metadata,
            "content_hash": make_content_hash(content),
            "parent_id": section_key[1],
            "section_index": section_key[2],
            "graph_expanded": True,
            "graph_section": True,
            "merged_chunk_count": len(parts),
        }
        return Document(page_content=content, metadata=metadata)

    def expand_sections(
        self,
        documents: list[Document],
        window: int = 3,
        max_sections: int = 8,
        max_chars: int = 3000,
        include_same_topic: bool = True,
    ) -> list[Document]:
        """Expand seed chunks to adjacent sections and same-topic pages."""
        seeds_by_page: dict[str, set[SectionKey]] = defaultdict(set)
        for document in documents:
            metadata = document.metadata
            doc_id = str(
                metadata.get("doc_id")
                or metadata.get("url")
                or metadata.get("source")
            )
            parent_id = str(metadata.get("parent_id") or doc_id)
            section_index = int(metadata.get("section_index", 0))
            if doc_id in self.page_sections:
                seeds_by_page[doc_id].add(
                    (doc_id, parent_id, section_index)
                )

        expanded: list[Document] = []
        for doc_id, seeds in seeds_by_page.items():
            sections = self.page_sections.get(doc_id, [])
            if not sections:
                continue

            if len(sections) <= max_sections:
                selected = list(sections)
            else:
                seed_indices = {
                    section[2] for section in seeds
                }
                selected = [
                    section
                    for section in sections
                    if any(
                        abs(section[2] - seed_index) <= window
                        for seed_index in seed_indices
                    )
                ]
                # Always include the exact seed sections.
                selected.extend(
                    section for section in seeds if section in sections
                )
                selected = list(dict.fromkeys(selected))[:max_sections]

            for section_key in selected:
                merged = self._merge_section(section_key, max_chars)
                if merged is not None:
                    expanded.append(merged)

            if not include_same_topic:
                continue

            # Include the corresponding section from a Python/JavaScript twin.
            seed_shapes = {
                self._section_shape(section)
                for section in seeds
                if section in self.section_nodes
            }
            for twin_doc_id in self.same_topic_pages.get(doc_id, set()):
                for section in self.page_sections.get(twin_doc_id, []):
                    if self._section_shape(section) in seed_shapes:
                        merged = self._merge_section(
                            section, max_chars
                        )
                        if merged is not None:
                            expanded.append(merged)

        return expanded

    def expand_context(
        self,
        documents: list[Document],
        window: int = 5,
        max_sections: int = 30,
        max_chars: int = 4000,
        max_docs: int = 24,
    ) -> list[Document]:
        """Build a context set without changing the retrieval ranking.

        The original top-k documents remain the retrieval result. This method
        replaces a selected section by its merged section version and adds
        adjacent/twin sections as extra generation context.
        """
        expanded = self.expand_sections(
            documents,
            window=window,
            max_sections=max_sections,
            max_chars=max_chars,
            include_same_topic=True,
        )

        by_section: dict[tuple[str, str, int], Document] = {}
        order: list[tuple[str, str, int]] = []

        def section_key(document: Document) -> tuple[str, str, int]:
            metadata = document.metadata
            url = str(
                metadata.get("url")
                or metadata.get("doc_id")
                or metadata.get("source")
                or ""
            )
            return (
                url,
                str(metadata.get("parent_id") or ""),
                int(metadata.get("section_index", 0)),
            )

        for document in documents:
            key = section_key(document)
            if key not in by_section:
                order.append(key)
            by_section[key] = document

        for document in expanded:
            key = section_key(document)
            if key not in by_section:
                order.append(key)
            # Prefer the merged section version for the same section.
            by_section[key] = document

        return [
            by_section[key]
            for key in order
            if key in by_section
        ][:max_docs]


def build_document_graph(catalog: ChunkCatalog) -> DocumentGraph:
    return DocumentGraph(catalog)
