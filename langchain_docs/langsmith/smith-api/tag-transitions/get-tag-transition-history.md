---
title: "Get tag transition history - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tag-transitions/get-tag-transition-history
scraped_at: 2026-11-15T03:41:58.651183
word_count: 66
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

Repository owner (tenant handle)

repo

string

required

Repository handle

tag\_name

string

required

Tag name

#### Query Parameters

limit

integer

default:50

Required range: `1 <= x <= 100`

offset

integer

default:0

Required range: `x >= 0`

#### Response

200

application/json

OK

total

integer

transitions

object[]

Show child attributes