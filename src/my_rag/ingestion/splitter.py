import hashlib
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

from .loader import DOCS_DIR, load_markdown_documents

HEADERS_TO_SPLIT_ON = [
    ("#", "h1"),
    ("##", "h2"),
    ("###", "h3"),
] # 定义切分符


def _parent_path(metadata: dict) -> str:
    """Return the parent heading path used to group sibling chunks."""
    h1 = metadata.get("h1") or ""
    h2 = metadata.get("h2") or ""
    h3 = metadata.get("h3") or ""

    if h3:
        return " > ".join(part for part in (h1, h2) if part)
    if h2:
        return h1
    return ""


def split_documents(documents: list[Document]) -> list[Document]:
    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=HEADERS_TO_SPLIT_ON,
        strip_headers=False,
    )
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=50,
        separators=["\n", ""],
    )
    chunks: list[Document] = []
    for doc in documents:
        doc_id = doc.metadata.get("url") or doc.metadata.get("source")
        section_index = 0
        chunk_index = 0
        for section in splitter.split_text(doc.page_content):
            if not section.page_content.strip():
                continue
            section.metadata = {**doc.metadata, **section.metadata} # **表示字典解包，将键值对丢到新的字典中，如果键相同，则新值覆盖旧值
            parent_path = _parent_path(section.metadata)
            parent_id = f"{doc_id}::{parent_path}" if parent_path else doc_id

            for chunk in text_splitter.split_documents([section]): # 利用recursiveTextSplitter进行进一步切分，防止块过大
                text = chunk.page_content.strip()
                if not text:
                    continue
                chunk.metadata.update(
                    {
                        "doc_id": doc_id,
                        "parent_id": parent_id,
                        "section_index": section_index,
                        "chunk_index": chunk_index,
                        "content_hash": hashlib.sha1(
                            text.encode("utf-8")
                        ).hexdigest(),
                    }
                )
                chunks.append(chunk)
                chunk_index += 1
            section_index += 1
    return chunks


def load_and_split(docs_dir: Path = DOCS_DIR) -> list[Document]:
    return split_documents(load_markdown_documents(docs_dir))


if __name__ == "__main__":
    docs = load_and_split()
    print(f"Loaded {len(docs)} chunks")
    if docs:
        print(f"Metadata: {docs[0].metadata}")
        print(f"Content preview:\n{docs[0].page_content[:300]}")
