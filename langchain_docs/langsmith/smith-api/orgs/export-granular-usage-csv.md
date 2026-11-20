---
title: "Export granular usage csv - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/export-granular-usage-csv
scraped_at: 2026-11-15T03:41:20.857211
word_count: 111
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

start\_time

string<date-time>

required

end\_time

string<date-time>

required

workspace\_ids

string<uuid>[] | null

group\_by

enum<string>

default:workspace

Dimensions for grouping granular usage data.

Available options:

`user`,

`api_key`,

`project`,

`workspace`,

`trace_tier`

kind

enum<string>

default:traces

Which billable usage domain a granular-usage query targets.

* `traces`: trace counts.
* `langsmith_deployments`: LangSmith Deployment metrics (nodes executed,
  agent runs, agent uptime).

Default is `traces` for backward compatibility — existing callers of
`GET /granular-usage` without a `kind` query param get the same
response shape they always did.

Available options:

`traces`,

`langsmith_deployments`

trace\_tier

enum<string> | null

Available options:

`longlived`,

`shortlived`

#### Response

200

application/json

Successful Response