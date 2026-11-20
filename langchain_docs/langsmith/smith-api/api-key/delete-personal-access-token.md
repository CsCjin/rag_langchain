---
title: "Delete personal access token - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/api-key/delete-personal-access-token
scraped_at: 2026-11-15T03:40:34.085725
word_count: 137
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

pat\_id

string<uuid>

required

#### Response

200

application/json

Successful Response

API key GET schema.

role\_id, org\_role\_id, and access\_scope let clients render the key's
current role state without a second round trip. For workspace-scoped
service keys, org\_role\_id comes from the parent organization identity.

id

string<uuid>

required

short\_key

string

required

description

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