---
title: "Update org service key - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/update-org-service-key
scraped_at: 2026-11-15T03:41:28.942558
word_count: 202
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

api\_key\_id

string<uuid>

required

#### Body

application/json

API key PATCH schema.

role\_id: New workspace-level role to apply to every workspace identity
attached to the key. Optional; omit to leave workspace roles unchanged.
org\_role\_id: New org-level role to apply to the key's org identity.
Workspace-scoped keys accept only the built-in ORGANIZATION\_VIEWER
or ORGANIZATION\_RESTRICTED role.
Optional; omit to leave the organization role unchanged.

role\_id

string<uuid> | null

org\_role\_id

string<uuid> | null

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