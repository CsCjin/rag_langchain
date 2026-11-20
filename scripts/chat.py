import argparse
import sys

from my_rag.core.rag_chain import RAGChain, build_rag_chain


def print_answer(chain: RAGChain, question: str) -> None:
    try:
        response = chain.ask(question) # 调用rag_chain.py中的RAGChain类，chain可以看做是一个已经构筑好的对象
    except Exception as exc:
        print(f"请求失败：{exc}", file=sys.stderr)
        return

    print(f"\n{response.answer}\n") # 调用RAGChain类的answer属性
    if not response.sources:
        return

    print("来源：")
    seen: set[str] = set() # 创建一个空集合，元素类型为字符串，
    for document in response.sources:
        key = document.metadata.get("url") or document.metadata.get("source")
        if not key or key in seen:
            continue # 去重/去空
        seen.add(key)
        title = document.metadata.get("title") or "未知标题"
        print(f"- {title}: {key}")


def main() -> None:
    parser = argparse.ArgumentParser(description="LangChain 文档问答") # 创建一个命令栏解析器对象
    parser.add_argument("question", nargs="?", help="只问一个问题后退出") # 添加参数
    args = parser.parse_args() # 解析对象

    print("正在加载模型和索引...")
    try:
        chain = build_rag_chain()
    except Exception as exc:
        print(f"初始化失败：{exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    if args.question: # 单次问答模式
        print_answer(chain, args.question)
        return

    print("输入问题开始问答，输入 exit/quit/q 退出。")
    while True: # 循环问答模式，调出词为exit, quit, q（不区分大小写），用户强行关闭循环也可以
        try:
            question = input("\n问题> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not question:
            continue
        if question.lower() in {"exit", "quit", "q"}:
            break
        print_answer(chain, question)


if __name__ == "__main__":
    main()
