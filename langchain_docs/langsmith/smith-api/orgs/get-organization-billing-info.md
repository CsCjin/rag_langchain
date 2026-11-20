---
title: "Get organization billing info - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/get-organization-billing-info
scraped_at: 2026-11-15T03:41:23.454255
word_count: 219
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

Information about an organization's billing configuration.

display\_name

string

required

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

connected\_to\_stripe

boolean

required

connected\_to\_metronome

boolean

required

is\_personal

boolean

required

id

string<uuid> | null

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

payment\_method

StripePaymentMethodInfo · object | null

Stripe customer billing info.

Show child attributes

end\_of\_billing\_period

string<date-time> | null

current\_plan

CustomerVisiblePlanInfo · object | null

Customer visible plan information.

Show child attributes

upcoming\_plan

CustomerVisiblePlanInfo · object | null

Customer visible plan information.

Show child attributes

reached\_max\_workspaces

boolean

default:false

disabled

boolean

default:false

default\_sso\_provision

boolean

default:false

plus\_plan\_transition

PlusPlanTransitionInfo · object | null

Info about an org's automated startup-to-Plus plan transition.

Show child attributes