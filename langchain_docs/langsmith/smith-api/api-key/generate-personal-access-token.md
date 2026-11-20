---
title: "Generate personal access token - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/api-key/generate-personal-access-token
scraped_at: 2026-11-15T03:40:34.431911
word_count: 242
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

API key POST schema.

expires\_at: Optional datetime when the API key will expire.
workspaces: List of workspace UUIDs this key can access (feature-flagged).
role\_id: Optional UUID of the role to assign to API key.
If not provided, uses default role based on read\_only flag:
- WORKSPACE\_ADMIN if read\_only is False
- WORKSPACE\_READER if read\_only is True
org\_role\_id: UUID of an org role for service keys.
Workspace-scoped keys accept only the built-in ORGANIZATION\_VIEWER
or ORGANIZATION\_RESTRICTED role.
Defaults to ORGANIZATION\_VIEWER for workspace-scoped keys,
or ORGANIZATION\_USER for org-scoped keys.
default\_workspace\_id: UUID of the default workspace for PATs.
If not provided, uses the current logic (first available workspace).

description

string

default:Default API key

read\_only

boolean

default:false

deprecated

expires\_at

string<date-time> | null

workspaces

string<uuid>[] | null

role\_id

string<uuid> | null

org\_role\_id

string<uuid> | null

default\_workspace\_id

string<uuid> | null

#### Response

200

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