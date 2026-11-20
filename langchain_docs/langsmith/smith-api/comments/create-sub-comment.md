---
title: "Create sub comment - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/comments/create-sub-comment
scraped_at: 2026-11-15T03:40:44.522313
word_count: 74
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

parent\_comment\_id

string<uuid>

required

#### Body

application/json

content

string

required

#### Response

200

application/json

Successful Response

id

string<uuid>

required

comment\_on

string<uuid>

required

content

string

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

num\_sub\_comments

integer

required

num\_likes

integer

required

comment\_by

string<uuid> | null

parent\_id

string<uuid> | null

comment\_by\_name

string | null

liked\_by\_auth\_user

boolean | null