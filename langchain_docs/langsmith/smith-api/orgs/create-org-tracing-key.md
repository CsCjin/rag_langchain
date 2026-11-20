---
title: "Create org tracing key - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/create-org-tracing-key
scraped_at: 2026-11-15T03:41:18.509054
word_count: 124
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

workspaces

string<uuid>[]

required

Minimum array length: `1`

description

string

default:Tracing key

expires\_at

string<date-time> | null

#### Response

201

application/json

Successful Response

API key POST schema.

id

string<uuid>

required

short\_key

string

required

description

string

required

key

string

required

created\_at

string<date-time> | null

read\_only

boolean

default:false

deprecated

last\_used\_at

string<date-time> | null

expires\_at

string<date-time> | null

revoked\_at

string<date-time> | null

workspace\_names

string[] | null

default\_workspace\_name

string | null

role\_id

string<uuid> | null

org\_role\_id

string<uuid> | null

access\_scope

enum<string> | null

Available options:

`organization`,

`workspace`

created\_by

string | null

is\_tracing\_key

boolean

default:false

workspace\_ids

string<uuid>[]

can\_delete

boolean

default:false

Whether tracing-key deletion authority has been confirmed. Legacy key responses do not evaluate this capability.