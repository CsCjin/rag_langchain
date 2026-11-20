---
title: "List runs of one trace in a public shared thread - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/threads/list-runs-of-one-trace-in-a-public-shared-thread
scraped_at: 2026-11-15T03:42:04.201822
word_count: 45
---

#### Headers

Accept

string

application/json or text/event-stream

#### Path Parameters

share\_token

string<uuid>

required

Share token UUID

trace\_id

string<uuid>

required

Trace root UUID

#### Query Parameters

selects

string[]

required

repeatable public run fields to include

#### Response

200

application/json

OK

items

object[]

required

Show child attributes