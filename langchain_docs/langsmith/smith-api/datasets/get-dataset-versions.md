---
title: "Get dataset versions - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/get-dataset-versions
scraped_at: 2026-11-15T03:40:49.942495
word_count: 61
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

dataset\_id

string<uuid>

required

#### Query Parameters

search

string | null

example

string<uuid> | null

limit

integer

default:100

Required range: `1 <= x <= 100`

offset

integer

default:0

Required range: `x >= 0`

#### Response

200

application/json

Successful Response

as\_of

string<date-time>

required

tags

string[] | null