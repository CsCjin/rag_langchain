---
title: "Delete runs abac - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/delete-runs-abac
scraped_at: 2026-11-15T03:41:38.672409
word_count: 28
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

string<uuid>

required

trace\_ids

string<uuid>[]

required

#### Response

200

application/json

Successful Response