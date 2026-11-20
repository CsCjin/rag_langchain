---
title: "Get service accounts - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/service-accounts/get-service-accounts
scraped_at: 2026-11-15T03:41:57.636177
word_count: 40
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Response

200 - application/json

Successful Response

id

string<uuid>

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

name

string

required

organization\_id

string<uuid>

required

default\_workspace\_id

string<uuid> | null

required