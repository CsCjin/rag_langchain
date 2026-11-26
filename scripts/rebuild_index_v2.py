"""Rebuild the vector store with parent/sibling metadata and cache BM25.

Build sequence:
1. load + split + deduplicate chunks;
2. build and pickle the chunk catalog / BM25 cache;
3. move the old vector store to a backup;
4. build the new Chroma store directly into ``data/vector_store``;
5. verify metadata and chunk count; restore the backup on failure.
"""

import json
import shutil
import time
from datetime import datetime
from pathlib import Path

from my_rag.config import PROJECT_ROOT, VECTOR_STORE_DIR
from my_rag.core.chunk_catalog import (
    build_chunk_catalog,
    dedupe_documents,
)
from my_rag.core.vector_store import build_vector_store
from my_rag.ingestion.splitter import load_and_split
from my_rag.model.embedding import get_embedding_model

BACKUP_DIR = PROJECT_ROOT / "data" / "vector_store_v1_backup"
CACHE_PATH = PROJECT_ROOT / "data" / "cache" / "chunk_catalog.pkl"
MANIFEST_PATH = (
    PROJECT_ROOT / "data" / "cache" / "index_manifest.json"
)
REQUIRED_METADATA = {
    "doc_id",
    "parent_id",
    "section_index",
    "chunk_index",
    "content_hash",
}


def main() -> None:
    started_at = time.time()
    print("Loading and splitting markdown documents...", flush=True)
    documents = dedupe_documents(load_and_split())
    print(f"Deduplicated chunks: {len(documents)}", flush=True)

    print("Building chunk catalog and BM25 cache...", flush=True)
    catalog = build_chunk_catalog(
        documents=documents,
        cache_path=CACHE_PATH,
        force_rebuild=True,
    )
    catalog_chunks = len(catalog.documents)
    del catalog
    print(f"Catalog cached with {catalog_chunks} chunks", flush=True)

    backup = BACKUP_DIR
    if backup.exists():
        backup = BACKUP_DIR.with_name(
            f"{BACKUP_DIR.name}_{int(time.time())}"
        )

    old_moved = False
    try:
        if VECTOR_STORE_DIR.exists():
            print(
                f"Moving old vector store to {backup}",
                flush=True,
            )
            shutil.move(str(VECTOR_STORE_DIR), str(backup))
            old_moved = True

        print("Loading embedding model...", flush=True)
        embeddings = get_embedding_model()

        print(
            f"Building vector store at {VECTOR_STORE_DIR}...",
            flush=True,
        )
        store = build_vector_store(
            documents,
            embeddings,
            VECTOR_STORE_DIR,
        )

        collection_count = store._collection.count()
        sample = store.get(limit=1, include=["metadatas"])
        sample_metadata = (sample.get("metadatas") or [{}])[0]
        missing_metadata = REQUIRED_METADATA - set(sample_metadata)
        print(
            f"Vector store count: {collection_count}; "
            f"missing metadata: {sorted(missing_metadata)}",
            flush=True,
        )
        if collection_count != len(documents):
            raise RuntimeError(
                f"Chunk count mismatch: store={collection_count}, "
                f"documents={len(documents)}"
            )
        if missing_metadata:
            raise RuntimeError(
                f"Missing metadata fields: {sorted(missing_metadata)}"
            )

        # Release the Chroma client before the process exits.
        del store

        manifest = {
            "built_at": datetime.now().isoformat(timespec="seconds"),
            "chunk_count": len(documents),
            "collection_count": collection_count,
            "catalog_chunks": catalog_chunks,
            "vector_store": str(VECTOR_STORE_DIR),
            "cache_path": str(CACHE_PATH),
            "embedding_model": "IEITYuan/Yuan-embedding-2.0-en",
            "required_metadata": sorted(REQUIRED_METADATA),
            "elapsed_seconds": round(time.time() - started_at, 2),
        }
        MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST_PATH.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(
            f"Done in {manifest['elapsed_seconds']}s; "
            f"manifest={MANIFEST_PATH}",
            flush=True,
        )
    except Exception:
        if VECTOR_STORE_DIR.exists():
            shutil.rmtree(VECTOR_STORE_DIR, ignore_errors=True)
        if old_moved and backup.exists():
            print(
                f"Build failed; restoring {backup} -> {VECTOR_STORE_DIR}",
                flush=True,
            )
            shutil.move(str(backup), str(VECTOR_STORE_DIR))
        raise


if __name__ == "__main__":
    main()
