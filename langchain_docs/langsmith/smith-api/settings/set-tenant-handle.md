---
title: "Set tenant handle - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/settings/set-tenant-handle
scraped_at: 2026-11-15T03:41:58.238571
word_count: 38
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

tenant\_handle

string

required

#### Response

200

application/json

Successful Response

id

string<uuid>

required

display\_name

string

required

created\_at

string<date-time>

required

tenant\_handle

string | null