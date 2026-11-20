---
title: "List rule logs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/list-rule-logs
scraped_at: 2026-11-15T03:41:39.383896
word_count: 148
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

offset

integer

default:0

Required range: `x >= 0`

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