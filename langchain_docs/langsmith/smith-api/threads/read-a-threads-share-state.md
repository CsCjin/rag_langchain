---
title: "Read a thread's share state - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/threads/read-a-threads-share-state
scraped_at: 2026-11-15T03:42:05.451519
word_count: 46
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

thread\_id

string

required

Thread ID

#### Query Parameters

project\_id

string<uuid>

required

Project UUID

#### Response

200

application/json

share\_token is omitted when the thread is not shared

share\_token

string<uuid>

Example:

`"018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"`