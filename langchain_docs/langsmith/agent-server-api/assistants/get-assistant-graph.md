---
title: "Get Assistant Graph - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-graph
scraped_at: 2026-11-15T03:38:08.744250
word_count: 50
---

#### Path Parameters

assistant\_id

string<uuid>stringstring<uuid>string

required

The ID of the assistant.

#### Query Parameters

xray

booleanintegerbooleaninteger

default:false

Include graph representation of subgraphs. If an integer value is provided, only subgraphs with a depth less than or equal to the value will be included.

#### Response

200

application/json

Success

{key}

object[]