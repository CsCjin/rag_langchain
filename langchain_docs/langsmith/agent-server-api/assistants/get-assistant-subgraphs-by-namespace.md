---
title: "Get Assistant Subgraphs by Namespace - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-subgraphs-by-namespace
scraped_at: 2026-11-15T03:38:09.507040
word_count: 68
---

#### Path Parameters

assistant\_id

string<uuid>

required

The ID of the assistant.

namespace

string

required

Namespace of the subgraph to filter by.

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