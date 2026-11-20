---
title: "Update insights job (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/update-insights-job-beta
scraped_at: 2026-11-15T03:42:12.912923
word_count: 52
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

#### Body

application/json

Request to update an Insights job.

name

string

required

#### Response

200

application/json

Successful Response

Response to updating an Insights job.

name

string

required

status

string

required