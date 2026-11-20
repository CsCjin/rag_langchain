---
title: "Get the LangSmith UI URL for a run - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/runs/get-the-langsmith-ui-url-for-a-run
scraped_at: 2026-11-15T03:41:43.385179
word_count: 67
---

#### Authorizations

API Key & Tenant IDBearer Auth & Tenant IDAPI Key & Tenant IDBearer Auth & Tenant ID

X-API-Key

string

header

required

X-Tenant-Id

string

header

required

#### Path Parameters

run\_id

string<uuid>

required

Run UUID

#### Query Parameters

project\_id

string

required

Project (session) UUID

trace\_id

string

required

Trace UUID

start\_time

string

Run start time in RFC3339 format; omit if unknown

#### Response

200

application/json

OK

url

string