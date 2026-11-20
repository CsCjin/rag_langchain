---
title: "Update existing experiment view override configuration - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/experiment-view-overrides/update-existing-experiment-view-override-configuration
scraped_at: 2026-11-15T03:40:57.683546
word_count: 66
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

#### Body

application/json

column\_overrides

object[]

required

Required array length: `1 - 50` elements

Show child attributes

#### Response

200

application/json

Successfully updated experiment view override

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