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
        for chunk in splitter.split_text(doc.page_content):
            if not chunk.page_content.strip():
                continue
            chunk.metadata = {**doc.metadata, **chunk.metadata} # **表示字典解包，将键值对丢到新的字典中，如果键相同，则新值覆盖旧值
            chunks.extend(text_splitter.split_documents([chunk])) # 利用recursiveTextSplitter进行进一步切分，防止块过大
    return chunks


def load_and_split(docs_dir: Path = DOCS_DIR) -> list[Document]:
    return split_documents(load_markdown_documents(docs_dir))


if __name__ == "__main__":
    docs = load_and_split()
    print(f"Loaded {len(docs)} chunks")
    if docs:
        print(f"Metadata: {docs[0].metadata}")
        print(f"Content preview:\n{docs[0].page_content[:300]}")
