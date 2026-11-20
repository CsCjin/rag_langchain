from my_rag.config import VECTOR_STORE_DIR


def main() -> None:
    from my_rag.pipeline import build_index

    print("Building index...")
    count = build_index()
    print(f"Indexed {count} chunks")
    print(f"Saved to {VECTOR_STORE_DIR}")
