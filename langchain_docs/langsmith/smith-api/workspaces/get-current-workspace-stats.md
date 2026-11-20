---
title: "Get current workspace stats - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/get-current-workspace-stats
scraped_at: 2026-11-15T03:42:20.538406
word_count: 57
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

tag\_value\_id

string<uuid>[] | null

#### Response

200

application/json

Successful Response

Stats for a tenant.

tenant\_id

string<uuid>

required

dataset\_count

integer

required

tracer\_session\_count

integer

required

repo\_count

integer

required

annotation\_queue\_count

integer

required

deployment\_count

integer

required

dashboards\_count

integer

required

evaluator\_count

integer

required

custom\_app\_count

integer

required