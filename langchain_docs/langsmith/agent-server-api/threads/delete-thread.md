---
title: "Delete Thread - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/threads/delete-thread
scraped_at: 2026-11-15T03:38:17.633139
word_count: 44
---

#### Path Parameters

thread\_id

string<uuid>

required

The ID of the thread.

#### Query Parameters

sync\_checkpoint\_delete

boolean

default:false

If true, delete checkpoints before responding instead of deferring them to background deletion. Use when thread data must be gone on return.

#### Response

200

application/json

Success