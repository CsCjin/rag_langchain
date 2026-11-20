from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

COLLECTION_NAME = "langchain_docs"
BATCH_SIZE = 1000 # 设置batch_size分批传入，防止一次性数据量过大报错


def build_vector_store(
    documents: list[Document],
    embeddings: Embeddings,
    persist_directory: Path,
) -> Chroma:
    persist_directory.mkdir(parents=True, exist_ok=True)
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(persist_directory),
    )
    vector_store.reset_collection()
    for start in range(0, len(documents), BATCH_SIZE):
        vector_store.add_documents(documents[start : start + BATCH_SIZE])
    return vector_store


def load_vector_store(
    persist_directory: Path, embeddings: Embeddings
) -> Chroma:
    if not persist_directory.exists():
        raise FileNotFoundError(f"Vector store not found: {persist_directory}")
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(persist_directory),
    )
