from dataclasses import dataclass

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.language_models import BaseLanguageModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from my_rag.core.retriever import build_self_query_retriever

PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是基于 LangChain 官方文档的问答助手。"
            "请仅依据给定的上下文回答问题；如果上下文不足以回答，"
            "请明确说明无法从文档中找到答案，不要编造。"
            "回答使用与用户提问相同的语言，并在引用信息时注明来源编号。",
        ),
        (
            "human",
            "上下文：\n{context}\n\n问题：{question}",
        ),
    ]
)


@dataclass
class RAGResponse:
    answer: str
    sources: list[Document]


def format_documents(documents: list[Document]) -> str:
    sections: list[str] = []
    for index, document in enumerate(documents, start=1):
        metadata = document.metadata
        title = metadata.get("title") or metadata.get("source") or "未知来源"
        lines = [f"[{index}] 标题: {title}"]
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
    ) -> None:
        self.retriever = build_self_query_retriever(vector_store, llm, k=k)
        self.answer_chain = PROMPT | llm | StrOutputParser() # langchain架构自带的LCEL表达式

    def ask(self, question: str) -> RAGResponse:
        documents = self.retriever.invoke(question) # invoke()函数的作用是将输入(question)传入组件中，执行并返回输出
        if not documents:
            return RAGResponse(
                answer="未在检索到的文档中找到相关信息。",
                sources=[],
            )
        answer = self.answer_chain.invoke(
            {
                "context": format_documents(documents),
                "question": question,
            }
        )
        return RAGResponse(answer=answer, sources=documents)


# 构筑rag_chain，返回RAGChain类
def build_rag_chain(
    vector_store: Chroma | None = None,
    llm: BaseLanguageModel | None = None,
    k: int = 4,
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
    return RAGChain(vector_store, llm, k=k)
