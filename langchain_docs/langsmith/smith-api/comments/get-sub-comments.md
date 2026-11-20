---
title: "Get sub comments - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/comments/get-sub-comments
scraped_at: 2026-11-15T03:40:45.088924
word_count: 63
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

#### Query Parameters

limit

integer

default:20

Required range: `1 <= x <= 100`

offset

integer

default:0

Required range: `x >= 0`

#### Response

200

application/json

Successful Response

comments

Comment · object[]

required

Show child attributes

total

integer

required