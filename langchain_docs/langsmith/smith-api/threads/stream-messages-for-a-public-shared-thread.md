---
title: "Stream messages for a public shared thread - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/threads/stream-messages-for-a-public-shared-thread
scraped_at: 2026-11-15T03:42:05.980992
word_count: 52
---

#### Headers

Accept

string

required

must be text/event-stream

#### Path Parameters

share\_token

string<uuid>

required

Share token UUID

#### Query Parameters

page\_size

integer

messages page size

cursor

string

opaque cursor from a previous page

trace\_id

string<uuid>

anchor the page on this trace

#### Response

200

text/event-stream

text/event-stream

The response is of type `string`.