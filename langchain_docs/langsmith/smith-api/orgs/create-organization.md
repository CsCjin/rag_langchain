---
title: "Create organization - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/create-organization
scraped_at: 2026-11-15T03:41:18.639439
word_count: 222
---

#### Authorizations

Authorization

string

header

required

Bearer tokens are used to authenticate from the UI. Must also specify x-tenant-id or x-organization-id (for org scoped apis).

#### Body

application/json

Create organization schema.

display\_name

string

required

Minimum string length: `1`

Pattern: `^[a-zA-Z0-9\-_ ]+$`

is\_personal

boolean

required

security\_contact

string<email> | null

#### Response

200

application/json

Successful Response

Schema for an organization in postgres for list views.

id

string<uuid>

required

display\_name

string

required

is\_personal

boolean

required

disabled

boolean

required

avatar\_url

string | null

tier

enum<string> | null

Available options:

`no_plan`,

`developer`,

`developer_01_2026`,

`developer_07_2026`,

`developer_10_2026`,

`plus`,

`plus_01_2026`,

`plus_07_2026`,

`plus_10_2026`,

`enterprise`,

`developer_legacy`,

`plus_legacy`,

`free`,

`free_07_2026`,

`free_10_2026`,

`enterprise_legacy`,

`startup`,

`startup_v0`,

`startup_07_2026`,

`startup_10_2026`,

`partner`,

`premier`

created\_at

string<date-time> | null

created\_by\_user\_id

string<uuid> | null

created\_by\_ls\_user\_id

string<uuid> | null

modified\_at

string<date-time> | null

sso\_login\_slug

string | null

sso\_only

boolean

default:false

jit\_provisioning\_enabled

boolean

default:true

invites\_enabled

boolean

default:true

public\_sharing\_disabled

boolean

default:false

pat\_creation\_disabled

boolean

default:false

api\_key\_creation\_from\_api\_keys\_enabled

boolean

workspace\_admin\_can\_invite\_to\_org

boolean

default:false

byoc\_create\_saas\_workspace\_enabled

boolean | null

default\_sso\_provision

boolean

default:false

max\_api\_key\_expiry\_days

integer | null

security\_contact

string | null

max\_pat\_expiry\_days

integer | null

max\_service\_key\_expiry\_days

integer | null

max\_tracing\_key\_expiry\_days

integer | null

scim\_group\_name\_separator

string

default::

llm\_auth\_proxy\_enabled

boolean | null

oidc\_login\_enabled

boolean | null

llm\_auth\_proxy\_jwt\_audience

string | null

ip\_allowlist

string[] | null

disabled\_model\_providers

string[] | null

restrict\_browser\_secrets

boolean | null

llm\_auth\_proxy\_allowed\_urls

string[] | null

topic\_search\_enabled

boolean

default:false

engine\_enabled

boolean | null

engine\_lcu\_spend\_limit\_monthly

string | null

Pattern: `^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$`

managed\_evals\_enabled

boolean | null