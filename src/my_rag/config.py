import os
from pathlib import Path


def _resolve_project_root() -> Path:
    env_root = os.getenv("MY_RAG_ROOT")
    if env_root:
        return Path(env_root).expanduser().resolve()
    package_root = Path(__file__).resolve().parents[2]
    if (package_root / "langchain_docs").is_dir():
        return package_root
    current = Path.cwd().resolve()
    for candidate in (current, *current.parents):
        if (candidate / "langchain_docs").is_dir():
            return candidate
    return package_root


PROJECT_ROOT = _resolve_project_root()
DOCS_DIR = PROJECT_ROOT / "langchain_docs"
VECTOR_STORE_DIR = PROJECT_ROOT / "data" / "vector_store"
