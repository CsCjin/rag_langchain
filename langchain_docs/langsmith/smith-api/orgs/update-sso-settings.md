---
title: "Update SSO settings - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/update-sso-settings
scraped_at: 2026-11-15T03:41:29.333953
word_count: 203
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

id

string<uuid>

required

#### Body

application/json

default\_workspace\_role\_id

string<uuid> | null

default\_workspace\_ids

string<uuid>[] | null

metadata\_url

string | null

metadata\_xml

string | null

sso\_groups\_enabled

boolean | null

sso\_groups\_claim\_field

string | null

sso\_groups\_required

boolean | null

sso\_groups\_role\_sync\_enabled

boolean | null

attribute\_mapping

SupabaseAttributeMapping · object | null

Supabase SAML provider attribute\_mapping. Empty keys is a valid value
(clears the mapping). Map key is the claim key written into identity\_data;
value points at the SAML assertion attribute name.

Show child attributes

#### Response

200

application/json

Successful Response

id

string<uuid>

required

organization\_id

string<uuid>

required

provider\_id

string<uuid>

required

default\_workspace\_role\_id

string<uuid>

required

default\_workspace\_ids

string<uuid>[]

required

provider\_type

enum<string>

default:saml

Available options:

`saml`,

`oidc`

metadata\_url

string | null

metadata\_xml

string | null

oidc\_issuer\_url

string | null

oidc\_client\_id

string | null

oidc\_scopes

string[]

oidc\_claim\_mapping

Oidc Claim Mapping · object

Show child attributes

sso\_groups\_enabled

boolean

default:false

sso\_groups\_claim\_field

string

default:groups

sso\_groups\_required

boolean

default:false

sso\_groups\_role\_sync\_enabled

boolean

default:true

attribute\_mapping

SupabaseAttributeMapping · object | null

Supabase SAML provider attribute\_mapping. Empty keys is a valid value
(clears the mapping). Map key is the claim key written into identity\_data;
value points at the SAML assertion attribute name.

Show child attributes

attribute\_mapping\_load\_error

string | null