---
title: "Share run - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/share-run
scraped_at: 2026-11-15T03:41:40.319651
word_count: 34
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