import re
from dataclasses import dataclass

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.language_models import BaseLanguageModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from my_rag.core.chunk_catalog import (
    ChunkCatalog,
    build_chunk_catalog,
)
from my_rag.core.document_graph import (
    DocumentGraph,
    build_document_graph,
)
from my_rag.core.hybrid import (
    DEFAULT_CANDIDATE_K,
    DEFAULT_COARSE_K,
    DEFAULT_DENSE_WEIGHT,
    DEFAULT_BM25_WEIGHT,
    retrieve_hybrid_with_rerank,
)
from my_rag.core.retriever import (
    build_reranked_self_query_retriever,
    build_self_query_retriever,
    construct_structured_query,
)
from my_rag.core.router import route_query
from my_rag.model.reranker import (
    DEFAULT_DOC_TYPE_PENALTIES,
    build_reranker,
)

PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是基于 LangChain 官方文档的问答助手。"
            "请仅依据给定的上下文回答问题；如果上下文不足以回答，"
            "请明确说明无法从文档中找到答案，不要编造。\n\n"
            "语言规则（最高优先级）：\n"
            "1. 先判断用户问题的主要语言。\n"
            "2. 用户用中文提问，必须用中文回答；用户用英文提问，必须用英文回答。\n"
            "3. 即使上下文主要是英文，也不能把中文问题的回答改成英文；"
            "即使上下文主要是中文，也不能把英文问题的回答改成中文。\n"
            "4. 代码、API 名称、参数名、命令、URL 和专有名词保持原样，不要翻译。\n"
            "5. 引用信息时使用上下文中标注的来源编号（例如 [S1]、[S2]）。",
        ),
        (
            "human",
            "上下文：\n{context}\n\n"
            "问题：{question}\n\n"
            "回答语言：{answer_language}。"
            "请严格使用该语言回答，不要使用其他语言。",
        ),
    ]
)

LANGUAGE_RETRY_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是语言一致性校正器。"
            "保持原回答的事实、引用和结构不变，只把语言改写为目标语言。"
            "不要添加新事实，不要删减关键结论，不要翻译代码、API 名称、"
            "参数名、命令和 URL。",
        ),
        (
            "human",
            "目标语言：{answer_language}\n"
            "问题：{question}\n"
            "原回答：\n{answer}\n\n"
            "请只输出目标语言版本的答案。",
        ),
    ]
)


def detect_answer_language(question: str) -> str:
    """Return the answer language label from the question language."""
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", question or ""))
    non_space = len(re.sub(r"\s", "", question or ""))
    ratio = chinese_chars / max(non_space, 1)
    return "中文" if chinese_chars >= 2 and ratio >= 0.05 else "英文"


def language_matches(answer: str, answer_language: str) -> bool:
    """Deterministic language check used as a post-generation guard."""
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", answer or ""))
    non_space = len(re.sub(r"\s", "", answer or ""))
    ratio = chinese_chars / max(non_space, 1)
    if answer_language == "中文":
        # Code-heavy Chinese answers may have a low Chinese ratio.
        return chinese_chars >= 2
    return ratio < 0.05


@dataclass
class RAGResponse:
    answer: str
    sources: list[Document]
    retrieval_sources: list[Document] | None = None
    route: str | None = None
    search_query: str | None = None
    metadata_filter: dict | None = None
    fallback_used: bool = False


def format_documents(documents: list[Document]) -> str:
    sections: list[str] = []
    for index, document in enumerate(documents, start=1):
        metadata = document.metadata
        title = metadata.get("title") or metadata.get("source") or "未知来源"
        lines = [f"[S{index}] 标题: {title}"]
        if url := metadata.get("url"):
            lines.append(f"URL: {url}")
        headings = " > ".join(
            value
            for key in ("h1", "h2", "h3")
            if (value := metadata.get(key))
        )
        if headings:
            lines.append(f"章节: {headings}")
        lines.append(f"内容: {document.page_content}")
        sections.append("\n".join(lines))
    return "\n\n".join(sections)
# 结构化检索到的文本，便于LLM理解

class RAGChain:
    def __init__(
        self,
        vector_store: Chroma,
        llm: BaseLanguageModel,
        k: int = 4,
        candidate_k: int = DEFAULT_CANDIDATE_K,
        coarse_k: int = DEFAULT_COARSE_K,
        context_k: int = 8,
        use_rerank: bool = True,
        use_router: bool = True,
        use_graph: bool = True,
        catalog: ChunkCatalog | None = None,
        document_graph: DocumentGraph | None = None,
    ) -> None:
        self.vector_store = vector_store
        self.llm = llm
        self.k = k
        self.candidate_k = candidate_k
        self.coarse_k = coarse_k
        self.context_k = context_k
        self.use_rerank = use_rerank
        self.use_router = use_router
        self.catalog = (
            catalog
            if catalog is not None
            else (build_chunk_catalog() if use_router else None)
        )
        self.use_graph = use_graph
        self.document_graph = (
            document_graph
            if document_graph is not None
            else (
                build_document_graph(self.catalog)
                if use_graph and self.catalog is not None
                else None
            )
        )
        self.self_query_retrievers: dict[
            tuple[str, ...],
            object,
        ] = {}

        # Legacy path retained for callers that explicitly disable routing.
        self.retriever = None
        if not use_router:
            if use_rerank:
                self.retriever = build_reranked_self_query_retriever(
                    vector_store,
                    llm,
                    candidate_k=candidate_k,
                    top_n=k,
                )
            else:
                self.retriever = build_self_query_retriever(
                    vector_store,
                    llm,
                    k=k,
                )

        self.answer_chain = PROMPT | llm | StrOutputParser() # langchain架构自带的LCEL表达式
        self.language_retry_chain = (
            LANGUAGE_RETRY_PROMPT | llm | StrOutputParser()
        )

    def _get_self_query_retriever(
        self,
        allowed_fields: tuple[str, ...],
    ):
        if allowed_fields not in self.self_query_retrievers:
            self.self_query_retrievers[allowed_fields] = (
                build_self_query_retriever(
                    self.vector_store,
                    self.llm,
                    k=self.candidate_k,
                    allowed_fields=allowed_fields,
                )
            )
        return self.self_query_retrievers[allowed_fields]

    def _retrieve(
        self,
        question: str,
    ) -> tuple[
        list[Document],
        str,
        str,
        dict | None,
        bool,
    ]:
        decision = route_query(question)
        route = decision.route
        search_query = question
        metadata_filter = None

        if route == "self_query":
            retriever = self._get_self_query_retriever(
                tuple(decision.allowed_fields)
            )
            structured_query = construct_structured_query(
                retriever,
                question,
            )
            search_query, search_kwargs = (
                retriever.structured_query_translator.visit_structured_query(
                    structured_query
                )
            )
            search_query = search_query.strip() or question
            metadata_filter = search_kwargs.get("filter")

        documents = retrieve_hybrid_with_rerank(
            self.vector_store,
            self.catalog,
            search_query,
            candidate_k=self.candidate_k,
            coarse_k=self.coarse_k,
            final_k=self.k,
            metadata_filter=metadata_filter,
            doc_type_penalties=DEFAULT_DOC_TYPE_PENALTIES,
            expand_siblings=True,
            sibling_window=2,
            max_chars=3000,
            dense_weight=DEFAULT_DENSE_WEIGHT,
            bm25_weight=DEFAULT_BM25_WEIGHT,
        )

        fallback_used = False
        if not documents and metadata_filter is not None:
            fallback_used = True
            documents = retrieve_hybrid_with_rerank(
                self.vector_store,
                self.catalog,
                question,
                candidate_k=self.candidate_k,
                coarse_k=self.coarse_k,
                final_k=self.k,
                metadata_filter=None,
                doc_type_penalties=DEFAULT_DOC_TYPE_PENALTIES,
                expand_siblings=True,
                sibling_window=2,
                max_chars=3000,
                dense_weight=DEFAULT_DENSE_WEIGHT,
                bm25_weight=DEFAULT_BM25_WEIGHT,
            )
            search_query = question
            metadata_filter = None

        return (
            documents,
            route,
            search_query,
            metadata_filter,
            fallback_used,
        )

    def ask(self, question: str) -> RAGResponse:
        if self.use_router:
            (
                documents,
                route,
                search_query,
                metadata_filter,
                fallback_used,
            ) = self._retrieve(question)
        else:
            documents = self.retriever.invoke(question)
            route = "legacy_self_query"
            search_query = question
            metadata_filter = None
            fallback_used = False

        if not documents:
            return RAGResponse(
                answer="未在检索到的文档中找到相关信息。",
                sources=[],
                retrieval_sources=[],
                route=route,
                search_query=search_query,
                metadata_filter=metadata_filter,
                fallback_used=fallback_used,
            )

        # Retrieval ranking stays unchanged. The graph only enriches the
        # generation context with adjacent/twin sections of the retrieved
        # pages, so retrieval metrics remain comparable to the baseline.
        context_documents = documents
        if self.document_graph is not None:
            expanded = self.document_graph.expand_context(documents)
            if expanded:
                # Graph expansion adds adjacent/twin sections; rerank the
                # expanded context so only the most relevant sections reach
                # the generation prompt.
                context_documents = list(
                    build_reranker(
                        top_n=min(self.context_k, len(expanded)),
                        penalties=DEFAULT_DOC_TYPE_PENALTIES,
                    ).compress_documents(expanded, question)
                )

        answer_language = detect_answer_language(question)
        answer = self.answer_chain.invoke(
            {
                "context": format_documents(context_documents),
                "question": question,
                "answer_language": answer_language,
            }
        )

        # Hard guard: prompt instructions are probabilistic, so retry once
        # with a dedicated language-correction prompt when the output language
        # does not match the question language.
        if not language_matches(answer, answer_language):
            answer = self.language_retry_chain.invoke(
                {
                    "answer_language": answer_language,
                    "question": question,
                    "answer": answer,
                }
            )

        return RAGResponse(
            answer=answer,
            sources=context_documents,
            retrieval_sources=documents,
            route=route,
            search_query=search_query,
            metadata_filter=metadata_filter,
            fallback_used=fallback_used,
        )


# 构筑rag_chain，返回RAGChain类
def build_rag_chain(
    vector_store: Chroma | None = None,
    llm: BaseLanguageModel | None = None,
    k: int = 4,
    candidate_k: int = DEFAULT_CANDIDATE_K,
    coarse_k: int = DEFAULT_COARSE_K,
    context_k: int = 8,
    use_rerank: bool = True,
    use_router: bool = True,
    use_graph: bool = True,
    catalog: ChunkCatalog | None = None,
    document_graph: DocumentGraph | None = None,
) -> RAGChain:
    if llm is None:
        from my_rag.model.llm import get_llm

        llm = get_llm()
    if vector_store is None:
        from my_rag.config import VECTOR_STORE_DIR
        from my_rag.core.vector_store import load_vector_store
        from my_rag.model.embedding import get_embedding_model

        vector_store = load_vector_store(
            VECTOR_STORE_DIR,
            get_embedding_model(),
        )
    return RAGChain(
        vector_store,
        llm,
        k=k,
        candidate_k=candidate_k,
        coarse_k=coarse_k,
        context_k=context_k,
        use_rerank=use_rerank,
        use_router=use_router,
        use_graph=use_graph,
        catalog=catalog,
        document_graph=document_graph,
    )
