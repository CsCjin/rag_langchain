---
title: "Create new experiment view override configuration for a dataset - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/experiment-view-overrides/create-new-experiment-view-override-configuration-for-a-dataset
scraped_at: 2026-11-15T03:40:57.293924
word_count: 59
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

#### Body

application/json

column\_overrides

object[]

required

Required array length: `1 - 50` elements

Show child attributes

#### Response

201

application/json

Successfully created experiment view override

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