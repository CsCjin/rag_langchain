import os

from dotenv import load_dotenv
from langchain_core.language_models import BaseLanguageModel
from langchain_deepseek import ChatDeepSeek

from my_rag.config import PROJECT_ROOT

load_dotenv(PROJECT_ROOT / ".env")


def get_llm() -> BaseLanguageModel:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError(
            "未设置 DEEPSEEK_API_KEY，请在项目根目录的 .env 中配置"
        )
    return ChatDeepSeek(
        model=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
        api_key=api_key,
        temperature=0,
    )
