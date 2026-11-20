---
title: "Diff dataset versions - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/diff-dataset-versions
scraped_at: 2026-11-15T03:40:48.107900
word_count: 46
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

from\_version

string<date-time>stringstring<date-time>string

required

to\_version

string<date-time>stringstring<date-time>string

required

#### Response

200

application/json

Successful Response

Dataset diff schema.

examples\_modified

string<uuid>[]

required

examples\_added

string<uuid>[]

required

examples\_removed

string<uuid>[]

required