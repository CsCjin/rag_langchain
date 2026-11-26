import re
from typing import Any

from langchain_chroma import Chroma
from langchain_classic.chains.query_constructor.prompt import SCHEMA_WITH_LIMIT_PROMPT
from langchain_classic.chains.query_constructor.schema import AttributeInfo
from langchain_classic.retrievers.contextual_compression import (
    ContextualCompressionRetriever,
)
from langchain_classic.retrievers.self_query.base import SelfQueryRetriever
from langchain_community.query_constructors.chroma import ChromaTranslator
from langchain_core.documents import Document
from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import PromptTemplate
from langchain_core.retrievers import BaseRetriever
from langchain_core.structured_query import StructuredQuery

from my_rag.model.reranker import build_reranker

DEFAULT_CANDIDATE_K = 30

SELF_QUERY_SCHEMA_PROMPT = PromptTemplate(
    template=SCHEMA_WITH_LIMIT_PROMPT.template
    + """

Translation rules:
- The document corpus is English. Always write the `query` field in English.
- If the user asks in Chinese or another language, translate the semantic query
  into English while preserving its meaning.
- Do not translate metadata filter values. Keep titles, URLs, product names,
  code identifiers, environment variables and version strings exactly as they
  appear in the documents.
""",
    input_variables=["allowed_comparators", "allowed_operators"],
)

SELF_QUERY_EXAMPLES = [
    (
        "LangChain 中如何创建结构化输出？",
        {
            "query": "How do I create structured output in LangChain?",
            "filter": "NO_FILTER",
        },
    ),
    (
        "LangChain 的 Deep Agents 和 Managed Deep Agents 有什么区别？",
        {
            "query": "What is the difference between Deep Agents and Managed Deep Agents?",
            "filter": "NO_FILTER",
        },
    ),
    (
        "在《Tracing quickstart》中，EU 账号应该设置什么 endpoint？",
        {
            "query": "What LANGSMITH_ENDPOINT should EU accounts use?",
            "filter": 'eq("title", "Tracing quickstart - Docs by LangChain")',
        },
    ),
    (
        "根据 https://docs.langchain.com/oss/python/langchain/messages 这篇文档，ToolMessage 有哪些字段？",
        {
            "query": "What fields does ToolMessage require?",
            "filter": 'eq("url", "https://docs.langchain.com/oss/python/langchain/messages")',
        },
    ),
    (
        "Python 版如何安装 LangChain？",
        {
            "query": "How do I install LangChain in Python?",
            "filter": 'eq("platform", "python")',
        },
    ),
    (
        "SmithDB Pod 一直是 Pending，怎么排查？",
        {
            "query": "How do I troubleshoot SmithDB Pod Pending status?",
            "filter": 'eq("doc_type", "troubleshooting")',
        },
    ),
    (
        "列出 3 条 LangSmith evaluation 教程。",
        {
            "query": "LangSmith evaluation tutorials",
            "filter": "NO_FILTER",
            "limit": 3,
        },
    ),
]

# metadata字段名表达式
METADATA_FIELD_INFO = [
    AttributeInfo(
        name="source",
        description="Markdown 文件路径",
        type="string",
    ),
    AttributeInfo(
        name="doc_type",
        description="文档类型：guide、tutorial、quickstart、concept、troubleshooting、changelog、release、policy、api_reference",
        type="string",
    ),
    AttributeInfo(
        name="platform",
        description="文档适用的 SDK 平台：python、javascript、agnostic",
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


# 降级方案，无元数据过滤的检索
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


def retrieve_documents_with_rerank(
    vector_store: Chroma,
    query: str,
    k: int = 4,
    candidate_k: int = DEFAULT_CANDIDATE_K,
    metadata_filter: dict[str, Any] | None = None,
    doc_type_penalties: dict[str, float] | None = None,
) -> list[Document]: # 加入重排序功能的普通检索
    candidates = retrieve_documents(
        vector_store,
        query,
        k=candidate_k,
        metadata_filter=metadata_filter,
    )
    if not candidates:
        return []
    return build_reranker(
        top_n=k,
        penalties=doc_type_penalties,
    ).compress_documents(candidates, query)


def _filter_self_query_examples(
    allowed_fields: set[str] | None,
) -> list[tuple[str, dict[str, Any]]]:
    """Keep only examples whose filter fields are allowed by the route."""
    if allowed_fields is None:
        return SELF_QUERY_EXAMPLES

    examples: list[tuple[str, dict[str, Any]]] = []
    for question, output in SELF_QUERY_EXAMPLES:
        filter_expression = output.get("filter")
        if filter_expression == "NO_FILTER":
            examples.append((question, output))
            continue
        match = re.search(r'eq\("([^"]+)"', filter_expression or "")
        if match and match.group(1) in allowed_fields:
            examples.append((question, output))
    return examples


def build_self_query_retriever(
    vector_store: Chroma,
    llm: BaseLanguageModel,
    k: int = 4,
    allowed_fields: set[str] | tuple[str, ...] | None = None,
) -> SelfQueryRetriever: # 独立的self-query模块（不包含重排），用于测试，正式版直接使用build_reranked_self_query_retriever即可
    """Build a SelfQueryRetriever.

    When ``allowed_fields`` is set, only those metadata fields are exposed to
    the query constructor. This lets the rule-based router prevent a query from
    inventing additional filters such as ``platform`` or ``doc_type``.
    """
    allowed = set(allowed_fields) if allowed_fields is not None else None
    metadata_field_info = METADATA_FIELD_INFO
    if allowed is not None:
        metadata_field_info = [
            field_info
            for field_info in METADATA_FIELD_INFO
            if field_info.name in allowed
        ]
        if not metadata_field_info:
            raise ValueError(
                f"None of the allowed fields {sorted(allowed)} exist in the metadata schema"
            )

    return SelfQueryRetriever.from_llm(
        llm=llm,
        vectorstore=vector_store,
        document_contents="LangChain 文档的 Markdown 片段，按标题层级切分",
        metadata_field_info=metadata_field_info,
        structured_query_translator=ChromaTranslator(), # 将大模型的输出格式转化为Chroma所需要的格式
        search_kwargs={"k": k},
        enable_limit=True,
        chain_kwargs={
            "examples": _filter_self_query_examples(allowed),
            "schema_prompt": SELF_QUERY_SCHEMA_PROMPT,
        },
    )


def build_reranking_retriever(
    base_retriever: BaseRetriever,
    top_n: int = 4,
    doc_type_penalties: dict[str, float] | None = None,
) -> ContextualCompressionRetriever:
    return ContextualCompressionRetriever(
        base_compressor=build_reranker(
            top_n=top_n,
            penalties=doc_type_penalties,
        ),
        base_retriever=base_retriever,
    )


def build_reranked_self_query_retriever(
    vector_store: Chroma,
    llm: BaseLanguageModel,
    candidate_k: int = DEFAULT_CANDIDATE_K,
    top_n: int = 4,
    doc_type_penalties: dict[str, float] | None = None,
    allowed_fields: set[str] | tuple[str, ...] | None = None,
) -> ContextualCompressionRetriever:
    base_retriever = build_self_query_retriever(
        vector_store,
        llm,
        k=candidate_k,
        allowed_fields=allowed_fields,
    )
    return build_reranking_retriever(
        base_retriever,
        top_n=top_n,
        doc_type_penalties=doc_type_penalties, # 基于doc_type的惩罚项
    )


def construct_structured_query(
    retriever: SelfQueryRetriever,
    query: str,
) -> StructuredQuery: # 利用之前组好的self-query retriever，将query转化为包含元数据过滤条件和查询内容的structed query
    return retriever.query_constructor.invoke({"query": query})
