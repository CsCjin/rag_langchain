---
title: "Get experiment view override configurations for a dataset - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/experiment-view-overrides/get-experiment-view-override-configurations-for-a-dataset
scraped_at: 2026-11-15T03:40:57.602212
word_count: 44
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

Dataset ID

#### Response

200

application/json

Successfully retrieved experiment view override configurations

column\_overrides

object[]

Show child attributes

created\_at

string

dataset\_id

string

id

string

modified\_at

string