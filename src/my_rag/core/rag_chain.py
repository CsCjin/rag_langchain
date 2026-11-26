import re
from dataclasses import dataclass

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.language_models import BaseLanguageModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from my_rag.core.retriever import (
    build_reranked_self_query_retriever,
    build_self_query_retriever,
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
            "5. 引用信息时使用上下文中标注的来源编号（例如 [1]、[2]）。",
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
        candidate_k: int = 30,
        use_rerank: bool = True,
    ) -> None:
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

    def ask(self, question: str) -> RAGResponse:
        documents = self.retriever.invoke(question) # invoke()函数的作用是将输入(question)传入组件中，执行并返回输出
        if not documents:
            return RAGResponse(
                answer="未在检索到的文档中找到相关信息。",
                sources=[],
            )

        answer_language = detect_answer_language(question)
        answer = self.answer_chain.invoke(
            {
                "context": format_documents(documents),
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

        return RAGResponse(answer=answer, sources=documents)


# 构筑rag_chain，返回RAGChain类
def build_rag_chain(
    vector_store: Chroma | None = None,
    llm: BaseLanguageModel | None = None,
    k: int = 4,
    candidate_k: int = 30,
    use_rerank: bool = True,
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
        use_rerank=use_rerank,
    )
