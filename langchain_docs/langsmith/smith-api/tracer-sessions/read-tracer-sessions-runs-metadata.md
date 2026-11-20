---
title: "Read tracer sessions runs metadata - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/read-tracer-sessions-runs-metadata
scraped_at: 2026-11-15T03:42:11.888870
word_count: 49
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

#### Query Parameters

metadata\_keys

string[] | null

start\_time

string<date-time> | null

k

integer

default:10

Required range: `x >= 1`

root\_runs\_only

boolean

default:false

#### Response

200

application/json

Successful Response

{key}

string[]