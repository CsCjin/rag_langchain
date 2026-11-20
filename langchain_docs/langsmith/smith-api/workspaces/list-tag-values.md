---
title: "List tag values - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/list-tag-values
scraped_at: 2026-11-15T03:42:22.514498
word_count: 50
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

tag\_key\_id

string<uuid>

required

#### Response

200

application/json

Successful Response

value

string

required

Required string length: `1 - 255`

id

string<uuid>

required

tag\_key\_id

string<uuid>

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

description

string | null