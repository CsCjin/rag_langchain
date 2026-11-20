---
title: "Get Assistant Subgraphs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-subgraphs
scraped_at: 2026-11-15T03:38:09.271840
word_count: 58
---

#### Path Parameters

assistant\_id

string<uuid>

required

The ID of the assistant.

#### Query Parameters

recurse

boolean

default:false

Recursively retrieve subgraphs of subgraphs.

#### Response

200

application/json

Success

Map of graph name to graph schema metadata (`input_schema`, `output_schema`, `state_schema`, `config_schema`, `context_schema`).

{key}

GraphSchemaNoId · object

Defines the structure and properties of a graph without an ID.

Show child attributes