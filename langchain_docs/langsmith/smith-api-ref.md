---
title: "LangSmith API reference - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api-ref
scraped_at: 2026-11-15T03:40:22.794394
word_count: 85
---

The LangSmith REST API provides programmatic access to LangSmith platform features including tracing, datasets, experiments, annotations, and more.
Browse the full API reference in the **LangSmith REST API** section in the sidebar.

## Authentication

Pass the `X-Api-Key` header with each request. The value should be a valid [LangSmith API key](/langsmith/create-account-api-key).

```
curl --request GET \
  --url https://api.smith.langchain.com/api/v1/workspaces \
  --header 'X-Api-Key: LANGSMITH_API_KEY'
```

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/smith-api-ref.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).