---
title: "Get last applied rule - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/get-last-applied-rule
scraped_at: 2026-11-15T03:41:39.293365
word_count: 125
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

backfill

boolean

default:false

#### Response

200

application/json

Successful Response

Run rules log schema.

rule\_id

string<uuid>

required

run\_id

string<uuid>

required

start\_time

string<date-time>

required

end\_time

string<date-time>

required

run\_name

string | null

run\_type

string | null

run\_session\_id

string<uuid> | null

run\_trace\_id

string<uuid> | null

application\_time

string<date-time> | null

add\_to\_annotation\_queue

RuleLogActionResponse · object | null

Show child attributes

add\_to\_dataset

RuleLogActionResponse · object | null

Show child attributes

evaluators

RuleLogActionResponse · object | null

Show child attributes

alerts

RuleLogActionResponse · object | null

Show child attributes

webhooks

RuleLogActionResponse · object | null

Show child attributes

extend\_only

RuleLogActionResponse · object | null

Show child attributes

thread\_id

string | null