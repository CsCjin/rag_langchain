---
title: "Get insights jobs (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/get-insights-jobs-beta
scraped_at: 2026-11-15T03:42:10.413209
word_count: 67
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

limit

integer

default:100

Required range: `1 <= x <= 100`

offset

integer

default:0

Required range: `x >= 0`

config\_id

string<uuid> | null

legacy

boolean | null

#### Response

200

application/json

Successful Response

A collection of Insights jobs.

clustering\_jobs

RunClusteringJobPydantic · object[]

required

Show child attributes