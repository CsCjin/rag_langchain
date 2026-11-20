---
title: "Get run cluster from insights job (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/get-run-cluster-from-insights-job-beta
scraped_at: 2026-11-15T03:42:10.254644
word_count: 56
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

cluster\_id

string<uuid>

required

#### Response

200

application/json

Successful Response

A cluster in an Insights report.

id

string<uuid>

required

num\_children

integer

required

level

integer

required

name

string

required

description

string

required

parent\_id

string<uuid> | null