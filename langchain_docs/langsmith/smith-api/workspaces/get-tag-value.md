---
title: "Get tag value - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/get-tag-value
scraped_at: 2026-11-15T03:42:21.241167
word_count: 53
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

tag\_value\_id

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