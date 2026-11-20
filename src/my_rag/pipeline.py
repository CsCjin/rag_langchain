from my_rag.config import VECTOR_STORE_DIR
from my_rag.core.vector_store import build_vector_store
from my_rag.ingestion.splitter import load_and_split
from my_rag.model.embedding import get_embedding_model


def build_index() -> int:
    documents = load_and_split()
    embeddings = get_embedding_model()
    build_vector_store(documents, embeddings, VECTOR_STORE_DIR)
    return len(documents)
    # 使用Chroma数据库，目标数据存于My_rag\data之中