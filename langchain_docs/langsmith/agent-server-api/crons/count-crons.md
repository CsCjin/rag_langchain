---
title: "Count Crons - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/crons/count-crons
scraped_at: 2026-11-15T03:38:10.395360
word_count: 52
---

#### Body

application/json

Payload for counting crons

assistant\_id

string<uuid>

The assistant ID or graph name to search for.

thread\_id

string<uuid>

The thread ID to search for.

metadata

Metadata · object

Metadata to filter by. Exact match filter for each KV pair.

#### Response

200

application/json

Success

The response is of type `integer`.