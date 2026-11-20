---
title: "List rule logs (v2) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/list-rule-logs-v2
scraped_at: 2026-11-15T03:41:39.528473
word_count: 77
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

rule\_id

string<uuid>

required

#### Query Parameters

limit

integer

default:150

Required range: `1 <= x <= 1440`

cursor

string | null

backfill

boolean

default:false

start\_time

string<date-time> | null

end\_time

string<date-time> | null

session\_id

string<uuid> | null

#### Response

200

application/json

Successful Response

Paginated response for rule logs with cursor-based pagination.

logs

RuleLogSchema · object[]

required

Show child attributes

cursor

string | null