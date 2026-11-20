---
title: "MCP Post - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/mcp/mcp-post
scraped_at: 2026-11-15T03:38:11.850641
word_count: 43
---

#### Headers

Accept

enum<string>

required

Accept header must include both 'application/json' and 'text/event-stream' media types.

Available options:

`application/json, text/event-stream`

#### Body

application/json

A JSON-RPC 2.0 request, notification, or response object.

#### Response

200

application/json

Successful JSON-RPC response.

The response is of type `object`.