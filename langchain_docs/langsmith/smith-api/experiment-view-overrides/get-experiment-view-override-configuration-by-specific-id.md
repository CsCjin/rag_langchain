---
title: "Get experiment view override configuration by specific ID - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/experiment-view-overrides/get-experiment-view-override-configuration-by-specific-id
scraped_at: 2026-11-15T03:40:58.143905
word_count: 51
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

id

string<uuid>

required

Experiment view override ID

#### Response

200

application/json

Successfully retrieved experiment view override configuration

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