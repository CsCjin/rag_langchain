---
title: "Get current user login methods - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/get-current-user-login-methods
scraped_at: 2026-11-15T03:41:22.528510
word_count: 89
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

id

string<uuid>

required

ls\_user\_id

string<uuid>

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

provider

enum<string> | null

Available options:

`email`,

`supabase:non-sso`,

`supabase:sso`,

`oidc`,

`custom-oidc`,

`oidc-sso`

saml\_provider\_id

string<uuid> | null

provider\_user\_id

string<uuid> | null

email

string | null

full\_name

string | null

first\_name

string | null

last\_name

string | null

username

string | null

is\_disabled

boolean | null

provisioning\_method

enum<string> | null

Available options:

`scim`,

`saml:jit`,

`bootstrap`

email\_confirmed\_at

string<date-time> | null