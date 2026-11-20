---
title: "Update dataset splits - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/update-dataset-splits
scraped_at: 2026-11-15T03:40:52.086127
word_count: 71
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

#### Body

application/json

split\_name

string

required

Split to add the examples to, or remove them from.

examples

string<uuid>[]

required

IDs of the examples to change. IDs of examples in other datasets are ignored.

remove

boolean

default:false

Remove the examples from the split instead of adding them.

#### Response

200

application/json

Successful Response