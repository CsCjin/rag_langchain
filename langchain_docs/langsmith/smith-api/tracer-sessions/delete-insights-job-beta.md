---
title: "Delete insights job (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/delete-insights-job-beta
scraped_at: 2026-11-15T03:42:09.224111
word_count: 41
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

Confirmation that an Insights job was deleted.

id

string<uuid>

required

message

string

required