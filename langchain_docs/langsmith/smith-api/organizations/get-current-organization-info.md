---
title: "Get current organization info - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/organizations/get-current-organization-info
scraped_at: 2026-11-15T03:41:16.739614
word_count: 223
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Response

200

application/json

Organization info

api\_key\_creation\_from\_api\_keys\_enabled

boolean

avatar\_url

string | null

byoc\_create\_saas\_workspace\_enabled

boolean

can\_export\_usage\_backfill

boolean

config

object

Show child attributes

default\_sso\_provision

boolean

disabled

boolean

disabled\_model\_providers

string[]

display\_name

string

engine\_enabled

boolean

engine\_lcu\_spend\_limit\_monthly

string

EngineLCUSpendLimitMonthly is the org admin (Layer 3) monthly Engine LCU spend
limit; null means the admin set no limit. The effective enforced limit is the
minimum of this and the finance/plan limits carried on Config.

id

string

invites\_enabled

boolean

ip\_allowlist

string[]

ip\_allowlist\_enabled

boolean

is\_personal

boolean

is\_sso\_user

boolean

jit\_provisioning\_enabled

boolean

llm\_auth\_proxy\_allowed\_urls

string[]

llm\_auth\_proxy\_enabled

boolean

llm\_auth\_proxy\_jwt\_audience

string

managed\_eval\_terms\_accepted\_at

string

ManagedEvalTermsAcceptedAt is the raw ISO 8601 timestamp string from the
config JSONB of when an org admin accepted the tuned evaluator terms;
null if never accepted. Returned verbatim so the value is byte-identical
to the smith-backend implementation under weighted routing.

managed\_evals\_enabled

boolean

ManagedEvalsEnabled is the org-level consent flag for tuned evaluators
(evaluators that spend a LangChain-held provider key).

marketplace\_payouts\_enabled

boolean

max\_api\_key\_expiry\_days

integer

max\_pat\_expiry\_days

integer

max\_service\_key\_expiry\_days

integer

max\_tracing\_key\_expiry\_days

integer | null

member\_disabled

boolean

oidc\_login\_enabled

boolean

default:false

oidc\_sso\_available

boolean

default:false

org\_role\_id

string<uuid> | null

org\_role\_name

enum<string> | null

Available options:

`ORGANIZATION_ADMIN`,

`ORGANIZATION_OPERATOR`,

`ORGANIZATION_USER`,

`ORGANIZATION_VIEWER`,

`ORGANIZATION_RESTRICTED`,

`CUSTOM`

pat\_creation\_disabled

boolean

permissions

string[]

public\_sharing\_disabled

boolean

reached\_max\_workspaces

boolean

restrict\_browser\_secrets

boolean

default:false

scim\_group\_name\_separator

string

security\_contact

string

sso\_login\_slug

string

sso\_only

boolean

tier

string

topic\_search\_enabled

boolean

default:false

workspace\_admin\_can\_invite\_to\_org

boolean