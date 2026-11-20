---
title: "Get tags - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tags/get-tags
scraped_at: 2026-11-15T03:41:59.215905
word_count: 46
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

repo

string

required

#### Response

200

application/json

Successful Response

id

string<uuid>

required

repo\_id

string<uuid>

required

commit\_id

string<uuid>

required

commit\_hash

string

required

tag\_name

string

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required