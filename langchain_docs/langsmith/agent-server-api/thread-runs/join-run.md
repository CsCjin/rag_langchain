---
title: "Join Run - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/join-run
scraped_at: 2026-11-15T03:38:16.558499
word_count: 41
---

#### Path Parameters

thread\_id

string<uuid>

required

The ID of the thread.

run\_id

string<uuid>

required

The ID of the run.

#### Query Parameters

cancel\_on\_disconnect

boolean

default:false

If true, the run will be cancelled if the client disconnects.

#### Response

200

application/json

Success