---
title: "Create a gateway policy - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/gateway-policies/create-a-gateway-policy
scraped_at: 2026-11-15T03:41:03.011533
word_count: 226
---

#### Authorizations

API KeyBearer AuthAPI KeyBearer Auth

X-API-Key

string

header

required

#### Body

application/json

action

string

config

object

description

string

enabled

boolean

name

string

policy\_type

string

priority

integer

subject\_matchers

object[]

Show child attributes

#### Response

201

application/json

Created

action

string

config

object

created\_at

string

created\_by

string

current\_spend

object[]

CurrentSpend is the list of spends recorded for each of the
tracked spend limit windows, used in v2 of spend\_cap policy type.

Show child attributes

current\_spend\_usd

number

CurrentSpendUSD is the spend in the policy's current window. Set for
any spend\_cap policy regardless of enabled state — disabled policies
still surface usage so users can see what would have been counted.
Nil for non-spend\_cap policies or when the spend lookup failed.

current\_usage

object[]

CurrentUsage is the consumed units in each configured limit's current
window. Set for any rate\_limit policy regardless of enabled state, one
entry per limit in the config. Nil for non-rate\_limit policies or when
the usage lookup failed.

Show child attributes

description

string

enabled

boolean

id

string

is\_system\_generated

boolean

name

string

organization\_id

string

parent\_policy\_id

string

ParentPolicyID is set on materialized children of a default\_spend\_cap
to the default's id. An explicit Update or a Create with the same
matchers clears the link and takes ownership of the materialized row.
Delete on the parent cascade-soft-deletes children still attached.

policy\_type

string

priority

integer

subject\_matchers

object[]

Show child attributes

updated\_at

string