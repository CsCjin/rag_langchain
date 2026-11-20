---
title: "List feedback ingest tokens - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/feedback/list-feedback-ingest-tokens
scraped_at: 2026-11-15T03:41:01.400819
word_count: 37
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

run\_id

string<uuid>

required

#### Response

200

application/json

Successful Response

id

string<uuid>

required

url

string

required

expires\_at

string<date-time>

required

feedback\_key

string

required