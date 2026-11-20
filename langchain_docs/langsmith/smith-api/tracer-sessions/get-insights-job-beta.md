---
title: "Get insights job (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/get-insights-job-beta
scraped_at: 2026-11-15T03:42:10.672172
word_count: 107
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

#### Response

200

application/json

Successful Response

An Insights job and the report it produced.

id

string<uuid>

required

name

string

required

status

string

required

created\_at

string<date-time>

required

clusters

RunCluster · object[]

required

Show child attributes

start\_time

string<date-time> | null

end\_time

string<date-time> | null

metadata

Metadata · object | null

shape

Shape · object | null

Show child attributes

error

string | null

config\_id

string<uuid> | null

report

InsightsSummary · object | null

High-level summary of an Insights report with patterns and specific traces.

Show child attributes