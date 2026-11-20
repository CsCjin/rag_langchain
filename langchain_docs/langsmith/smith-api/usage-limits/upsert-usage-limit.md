---
title: "Upsert usage limit - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/usage-limits/upsert-usage-limit
scraped_at: 2026-11-15T03:42:15.555864
word_count: 123
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Request body for creating or updating a usage limit.

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

#### Response

200

application/json

Successful Response

Usage limit model.

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