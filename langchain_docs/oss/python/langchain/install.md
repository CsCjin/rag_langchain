---
title: "Install LangChain - Docs by LangChain"
url: https://docs.langchain.com/oss/python/langchain/install
scraped_at: 2026-11-15T03:45:04.349140
word_count: 167
---

To install the LangChain package:

pip

uv

```
pip install -U langchain
# Requires Python 3.10+
```

```
uv add langchain
# Requires Python 3.10+
```

LangChain provides integrations to hundreds of LLMs and thousands of other integrations. These live in independent provider packages.

pip

uv

```
# Installing the OpenAI integration
pip install -U langchain-openai

# Installing the Anthropic integration
pip install -U langchain-anthropic
```

```
# Installing the OpenAI integration
uv add langchain-openai

# Installing the Anthropic integration
uv add langchain-anthropic
```

See the [Integrations tab](/oss/python/integrations/providers/overview) for a full list of available integrations.

Now that you have LangChain installed, you can get started by following the [Quickstart guide](/oss/python/langchain/quickstart).

Set up [LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=oss-langchain-install) tracing to debug your first LangChain app. Follow the [tracing quickstart](/langsmith/trace-with-langchain) to get started. We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/install.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).