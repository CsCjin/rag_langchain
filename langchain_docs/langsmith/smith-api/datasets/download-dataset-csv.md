---
title: "Download dataset csv - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/download-dataset-csv
scraped_at: 2026-11-15T03:40:48.179409
word_count: 52
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

Only modifications made on or before this time are included. If None, the latest version of the dataset is used.

#### Response

200

application/json

Successful Response