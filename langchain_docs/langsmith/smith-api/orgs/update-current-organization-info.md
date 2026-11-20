---
title: "Update current organization info - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/update-current-organization-info
scraped_at: 2026-11-15T03:41:28.426290
word_count: 405
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Update organization schema.

display\_name

string

Minimum string length: `1`

Pattern: `^[a-zA-Z0-9\-_ ]+$`

public\_sharing\_disabled

boolean | null

pat\_creation\_disabled

boolean | null

api\_key\_creation\_from\_api\_keys\_enabled

boolean

unshare\_all

boolean | null

jit\_provisioning\_enabled

boolean | null

workspace\_admin\_can\_invite\_to\_org

boolean | null

invites\_enabled

boolean | null

max\_api\_key\_expiry\_days

integer | null

security\_contact

string<email> | null

max\_pat\_expiry\_days

integer | null

max\_service\_key\_expiry\_days

integer | null

max\_tracing\_key\_expiry\_days

integer | null

scim\_group\_name\_separator

string

Required string length: `1`

llm\_auth\_proxy\_enabled

boolean | null

llm\_auth\_proxy\_jwt\_audience

string | null

ip\_allowlist

string[] | null

disabled\_model\_providers

string[] | null

restrict\_browser\_secrets

boolean | null

byoc\_create\_saas\_workspace\_enabled

boolean | null

llm\_auth\_proxy\_allowed\_urls

string[] | null

topic\_search\_enabled

boolean

default:false

engine\_enabled

boolean | null

engine\_lcu\_spend\_limit\_monthly

numberstringnumberstring

#### Response

200

application/json

Successful Response

Information about an organization.

IMPORTANT: Keep in sync with Go OrganizationInfo in smith-go/orgs/handler.go
while both implementations are in use (weighted routing rollout).

config

OrganizationConfig · object

required

Organization level configuration. May include any field that exists in tenant config and additional fields.

Each field's type annotation drives how Metronome custom-field values are validated
when resolving config (see smith-backend's `_parse_metronome_value` and smith-go's
`rejectInvalidMetronomeValue`): a value that doesn't fit the annotated type is
dropped and the field keeps whatever value was already resolved for it, rather than
raising. Changing a field's type here changes what Metronome values are accepted for it.

Show child attributes

is\_personal

boolean

required

id

string<uuid> | null

display\_name

string | null

avatar\_url

string | null

topic\_search\_enabled

boolean

default:false

engine\_enabled

boolean | null

engine\_lcu\_spend\_limit\_monthly

string | null

Pattern: `^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$`

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

reached\_max\_workspaces

boolean

default:false

permissions

string[]

org\_role\_name

enum<string> | null

Available options:

`ORGANIZATION_ADMIN`,

`ORGANIZATION_OPERATOR`,

`ORGANIZATION_USER`,

`ORGANIZATION_VIEWER`,

`ORGANIZATION_RESTRICTED`,

`CUSTOM`

org\_role\_id

string<uuid> | null

disabled

boolean

default:false

member\_disabled

boolean

default:false

is\_sso\_user

boolean

default:false

sso\_only

boolean

default:false

jit\_provisioning\_enabled

boolean

default:true

invites\_enabled

boolean

default:true

sso\_login\_slug

string | null

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

boolean

default:true

marketplace\_payouts\_enabled

boolean

default:false

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

can\_export\_usage\_backfill

boolean

default:false

llm\_auth\_proxy\_enabled

boolean

default:false

oidc\_login\_enabled

boolean

default:false

llm\_auth\_proxy\_jwt\_audience

string | null

ip\_allowlist

string[]

ip\_allowlist\_enabled

boolean

default:false

disabled\_model\_providers

string[]

restrict\_browser\_secrets

boolean

default:false

llm\_auth\_proxy\_allowed\_urls

string[] | null

oidc\_sso\_available

boolean

default:false

managed\_evals\_enabled

boolean | null

managed\_eval\_terms\_accepted\_at

string | null