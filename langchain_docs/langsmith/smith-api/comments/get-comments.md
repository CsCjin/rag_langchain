---
title: "Get comments - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/comments/get-comments
scraped_at: 2026-11-15T03:40:44.953086
word_count: 60
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