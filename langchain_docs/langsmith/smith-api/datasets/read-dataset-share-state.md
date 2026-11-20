---
title: "Read dataset share state - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/read-dataset-share-state
scraped_at: 2026-11-15T03:40:50.138773
word_count: 36
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

#### Response

200

application/json

DatasetShareSchema · object | null

Successful Response

dataset\_id

string<uuid>

required

share\_token

string<uuid>

required