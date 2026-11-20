---
title: "Create tag key - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/create-tag-key
scraped_at: 2026-11-15T03:42:17.070386
word_count: 57
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

key

string

required

Required string length: `1 - 255`

description

string | null

#### Response

200

application/json

Successful Response

key

string

required

Required string length: `1 - 255`

id

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