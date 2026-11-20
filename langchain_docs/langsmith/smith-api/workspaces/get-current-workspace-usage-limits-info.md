---
title: "Get current workspace usage limits info - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/get-current-workspace-usage-limits-info
scraped_at: 2026-11-15T03:42:20.650063
word_count: 41
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Response

200 - application/json

Successful Response

in\_reject\_set

boolean

required

usage\_limit\_type

enum<string> | null

Available options:

`payload_size`,

`events_ingested_per_hour`,

`total_unique_traces`,

`events_ingested_per_minute`,

`traces_deleted_per_hour`,

`user_defined_monthly_traces`,

`user_defined_monthly_longlived_traces`,

`user_defined_unknown`

tenant\_limit

integer | null