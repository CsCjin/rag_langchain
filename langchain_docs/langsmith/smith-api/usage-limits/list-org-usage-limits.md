---
title: "List org usage limits - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/usage-limits/list-org-usage-limits
scraped_at: 2026-11-15T03:42:15.030275
word_count: 69
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Response

200 - application/json

Successful Response

limit\_type

enum<string>

required

Type of usage limit.

Available options:

`monthly_traces`,

`monthly_longlived_traces`

limit\_value

integer

required

tenant\_id

string<uuid>

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

id

string<uuid>

scope

enum<string>

default:workspace

Granularity a limit applies to within a tenant.

Available options:

`workspace`,

`project`,

`user`

session\_id

string<uuid> | null

identity\_id

string<uuid> | null