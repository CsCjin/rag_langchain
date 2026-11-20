---
title: "Count Assistants - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/assistants/count-assistants
scraped_at: 2026-11-15T03:38:08.334502
word_count: 79
---

#### Body

application/json

Payload for counting assistants.

metadata

Metadata · object

Metadata to filter by. Exact match filter for each KV pair.

graph\_id

string

The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.

name

string

Name of the assistant to filter by. The filtering logic will match (case insensitive) assistants where 'name' is a substring of the assistant name.

#### Response

200

application/json

Success

The response is of type `integer`.