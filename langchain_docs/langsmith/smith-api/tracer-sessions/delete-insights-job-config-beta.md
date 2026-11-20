---
title: "Delete insights job config (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/delete-insights-job-config-beta
scraped_at: 2026-11-15T03:42:09.385460
word_count: 42
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

config\_id

string<uuid>

required

#### Response

200

application/json

Successful Response

Confirmation that an Insights job configuration was deleted.

id

string<uuid>

required

message

string

required