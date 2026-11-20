---
title: "Share a thread - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/threads/share-a-thread
scraped_at: 2026-11-15T03:42:05.558719
word_count: 47
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

#### Body

application/json

project\_id

string<uuid>

required

project\_id is the tracing project UUID containing the thread.

Example:

`"018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"`

#### Response

200

application/json

OK

share\_token

string<uuid>

Example:

`"018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"`