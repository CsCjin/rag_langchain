import os
from collections.abc import Sequence
from functools import lru_cache
from typing import Annotated

import torch
from dotenv import load_dotenv
from langchain_classic.retrievers.document_compressors import CrossEncoderReranker
from langchain_community.cross_encoders import HuggingFaceCrossEncoder
from langchain_core.callbacks import Callbacks
from langchain_core.documents import Document
from pydantic import Field

from my_rag.config import PROJECT_ROOT

load_dotenv(PROJECT_ROOT / ".env")

DEFAULT_MODEL_NAME = "BAAI/bge-reranker-v2-m3"
DEFAULT_DOC_TYPE_PENALTIES = {"changelog": 0.05, "release": 0.03}


def _resolve_device() -> str:
    configured = os.getenv("RERANKER_DEVICE") # 如果有配置则选择返回配置中选择的运行设备
    if configured:
        return configured
    return "cuda" if torch.cuda.is_available() else "cpu"


@lru_cache(maxsize=2)
def get_cross_encoder(model_name: str | None = None) -> HuggingFaceCrossEncoder:
    name = model_name or os.getenv("RERANKER_MODEL", DEFAULT_MODEL_NAME)
    encoder = HuggingFaceCrossEncoder(
        model_name=name,
        model_kwargs={"device": _resolve_device()},
    )
    print(f"Reranker model loaded: {name}")
    return encoder # 返回实例化的模型


def build_reranker(
    top_n: int = 4,
    model_name: str | None = None,
    penalties: dict[str, float] | None = None,
) -> CrossEncoderReranker:
    if penalties is None:
        penalties = dict(DEFAULT_DOC_TYPE_PENALTIES)
    return DocTypePenalizedReranker(
        model=get_cross_encoder(model_name),
        top_n=top_n, # 重排后保留的文档数量
        penalties=penalties,
    )# 构筑重排系统


class DocTypePenalizedReranker(CrossEncoderReranker):
    penalties: Annotated[
        dict[str, float],
        Field(default_factory=lambda: dict(DEFAULT_DOC_TYPE_PENALTIES)),
    ]

    def compress_documents(
        self,
        documents: Sequence[Document],
        query: str,
        callbacks: Callbacks | None = None,
    ) -> Sequence[Document]:
        scores = self.model.score(
            [(query, document.page_content) for document in documents]
        )
        docs_with_scores = []
        for document, score in zip(documents, scores):
            doc_type = document.metadata.get("doc_type")
            penalty = self.penalties.get(doc_type, 0.0)
            docs_with_scores.append((document, float(score) - penalty))
        result = sorted(
            docs_with_scores,
            key=lambda item: item[1],
            reverse=True,
        )
        return [document for document, _ in result[: self.top_n]]
