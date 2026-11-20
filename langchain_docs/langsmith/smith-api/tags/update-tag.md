---
title: "Update tag - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tags/update-tag
scraped_at: 2026-11-15T03:41:59.581907
word_count: 72
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

owner

string

required

repo

string

required

tag\_name

string

required

#### Body

application/json

Fields to update a prompt tag

commit\_id

string<uuid>

required

skip\_webhooks

booleanstring<uuid>[]booleanstring<uuid>[]

default:false

#### Response

200

application/json

Successful Response

Fields for a prompt tag

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