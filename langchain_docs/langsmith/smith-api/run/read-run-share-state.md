---
title: "Read run share state - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/read-run-share-state
scraped_at: 2026-11-15T03:41:40.262001
word_count: 39
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

run\_id

string<uuid>

required

#### Response

200

application/json

RunShareSchema · object | null

Successful Response

run\_id

string<uuid>

required

shared\_trace\_id

string<uuid>

required

share\_token

string<uuid>

required