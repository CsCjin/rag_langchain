from typing import Any

from langchain_chroma import Chroma
from langchain_classic.chains.query_constructor.schema import AttributeInfo
from langchain_classic.retrievers.self_query.base import SelfQueryRetriever
from langchain_community.query_constructors.chroma import ChromaTranslator
from langchain_core.documents import Document
from langchain_core.language_models import BaseLanguageModel
from langchain_core.structured_query import StructuredQuery

# metadata字段名表达式
METADATA_FIELD_INFO = [
    AttributeInfo(
        name="source",
        description="Markdown 文件路径",
        type="string",
    ),
    AttributeInfo(
        name="title",
        description="文档标题，用于按页面主题过滤",
        type="string",
    ),
    AttributeInfo(
        name="url",
        description="文档原始 URL",
        type="string",
    ),
    AttributeInfo(
        name="scraped_at",
        description="文档抓取时间，ISO 8601 字符串",
        type="string",
    ),
    AttributeInfo(
        name="word_count",
        description="文档字数",
        type="integer",
    ),
    AttributeInfo(
        name="h1",
        description="一级标题",
        type="string",
    ),
    AttributeInfo(
        name="h2",
        description="二级标题",
        type="string",
    ),
    AttributeInfo(
        name="h3",
        description="三级标题",
        type="string",
    ),
]


def retrieve_documents(
    vector_store: Chroma,
    query: str,
    k: int = 4,
    metadata_filter: dict[str, Any] | None = None,
) -> list[Document]:
    return vector_store.similarity_search(
        query,
        k=k,
        filter=metadata_filter,
    )
# 降级方案，无元数据过滤的检索


def build_self_query_retriever(
    vector_store: Chroma,
    llm: BaseLanguageModel,
    k: int = 4,
) -> SelfQueryRetriever:
    return SelfQueryRetriever.from_llm(
        llm=llm,
        vectorstore=vector_store,
        document_contents="LangChain 文档的 Markdown 片段，按标题层级切分",
        metadata_field_info=METADATA_FIELD_INFO,
        structured_query_translator=ChromaTranslator(), # 将大模型的输出格式转化为Chroma所需要的格式
        search_kwargs={"k": k},
        enable_limit=True,
    )


def construct_structured_query(
    retriever: SelfQueryRetriever,
    query: str,
) -> StructuredQuery: # 利用之前组好的self-query retriever，将query转化为包含元数据过滤条件和查询内容的structed query
    return retriever.query_constructor.invoke({"query": query})
