import json
import re
from datetime import date, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

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


def derive_doc_type(url: str, title: str) -> str:
    path = urlparse(url or "").path.lower()
    name = Path(path).name
    title_lower = (title or "").lower()

    if "release-policy" in path or "release-stages" in path:
        return "policy"

    if "changelog" in name or "changelog" in title_lower:
        return "changelog"

    if "/releases/" in path:
        return "release"

    if path.startswith(
        (
            "/langsmith/smith-api/",
            "/langsmith/agent-server-api/",
            "/api-reference/",
        )
    ):
        return "api_reference"

    troubleshooting_terms = (
        "troubleshoot",
        "troubleshooting",
        "diagnostics",
        "common-issues",
        "faq",
    )
    if any(term in path or term in title_lower for term in troubleshooting_terms):
        return "troubleshooting"

    if "quickstart" in path or "quickstart" in title_lower:
        return "quickstart"

    if "tutorial" in path or "tutorial" in title_lower:
        return "tutorial"

    concept_terms = (
        "concepts",
        "overview",
        "architecture",
        "philosophy",
        "introduction",
        "fundamentals",
    )
    if any(term in path or term in title_lower for term in concept_terms):
        return "concept"

    return "guide"


def derive_platform(url: str, title: str = "") -> str:
    segments = [
        segment
        for segment in urlparse(url or "").path.lower().strip("/").split("/")
        if segment
    ]
    if any(
        segment == "python"
        or segment.startswith("python-")
        or segment.endswith("-python")
        for segment in segments
    ):
        return "python"
    if any(
        segment == "javascript"
        or segment.startswith("javascript-")
        or segment.endswith("-javascript")
        for segment in segments
    ):
        return "javascript"

    title_lower = (title or "").lower()
    if "(python only)" in title_lower or "python extensions" in title_lower:
        return "python"
    if "(javascript only)" in title_lower or "(js only)" in title_lower:
        return "javascript"
    return "agnostic"


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
        if "doc_type" not in document.metadata:
            document.metadata["doc_type"] = derive_doc_type(
                document.metadata.get("url", ""),
                document.metadata.get("title", ""),
            )
        if "platform" not in document.metadata:
            document.metadata["platform"] = derive_platform(
                document.metadata.get("url", ""),
                document.metadata.get("title", ""),
            )
    return documents
