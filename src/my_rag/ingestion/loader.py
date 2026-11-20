import json
import re
from datetime import date, datetime
from pathlib import Path
from typing import Any

import yaml
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_core.documents import Document

from my_rag.config import DOCS_DIR

FRONTMATTER_PATTERN = re.compile(
    r"\A(?:\ufeff)?---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)",
    re.DOTALL,
)


def _parse_frontmatter(text: str) -> tuple[dict[str, Any], str]: # 将.md文件开头的YAML frontmatter 作为元数据导入
    match = FRONTMATTER_PATTERN.match(text)
    if match is None:
        return {}, text
    try:
        raw = yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return {}, text
    if not isinstance(raw, dict):
        return {}, text

    frontmatter: dict[str, Any] = {}
    for key, value in raw.items():
        if isinstance(value, (str, int, float, bool)):
            frontmatter[str(key)] = value
        elif isinstance(value, (datetime, date)):
            frontmatter[str(key)] = value.isoformat()
        elif value is not None:
            frontmatter[str(key)] = json.dumps(value, ensure_ascii=False)
    return frontmatter, text[match.end() :].lstrip("\r\n")


def load_markdown_documents(docs_dir: Path = DOCS_DIR) -> list[Document]:
    loader = DirectoryLoader(
        str(docs_dir),
        glob="**/*.md", # **代表递归所有子文件夹，*.md代表是加载md文件忽略其他文件
        loader_cls=TextLoader, # textloader作为加载器的内核
        loader_kwargs={"encoding": "utf-8"}, # 编码器，自动识别编码格式进行读取
    )
    documents = loader.load()
    for document in documents:
        frontmatter, content = _parse_frontmatter(document.page_content)
        document.metadata = {**document.metadata, **frontmatter}
        document.page_content = content
    return documents
