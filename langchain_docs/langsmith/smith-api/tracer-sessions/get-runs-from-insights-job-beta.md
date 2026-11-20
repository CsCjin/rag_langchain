---
title: "Get runs from insights job (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/get-runs-from-insights-job-beta
scraped_at: 2026-11-15T03:42:10.538906
word_count: 75
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

session\_id

string<uuid>

required

job\_id

string<uuid>

required

#### Query Parameters

cluster\_id

string<uuid> | null

limit

integer

default:100

Required range: `1 <= x <= 100`

offset

integer

default:0

Required range: `x >= 0`

attribute\_sort\_key

string | null

attribute\_sort\_order

enum<string> | null

Available options:

`asc`,

`desc`

#### Response

200

application/json

Successful Response

runs

Runs · object[]

required

offset

integer | null

required