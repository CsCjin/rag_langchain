---
title: "Share dataset - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/share-dataset
scraped_at: 2026-11-15T03:40:50.786527
word_count: 50
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

share\_projects

boolean

default:false

deprecated

Deprecated and has no effect. A shared dataset always shows its experiments.

#### Response

200

application/json

Successful Response

dataset\_id

string<uuid>

required

share\_token

string<uuid>

required