---
title: "Delete runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/delete-runs
scraped_at: 2026-11-15T03:41:38.351685
word_count: 30
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

session\_id

string<uuid> | null

trace\_ids

string<uuid>[] | null

#### Response

200

application/json

Successful Response