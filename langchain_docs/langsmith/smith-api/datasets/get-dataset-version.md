---
title: "Get dataset version - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/get-dataset-version
scraped_at: 2026-11-15T03:40:49.418980
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

as\_of

string<date-time> | null

tag

string | null

#### Response

200

application/json

Successful Response

Dataset version schema.

as\_of

string<date-time>

required

tags

string[] | null