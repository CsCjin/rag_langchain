---
title: "Lookup SSO by email - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/auth/lookup-sso-by-email
scraped_at: 2026-11-15T03:40:37.207520
word_count: 28
---

#### Body

application/json

email

string

required

#### Response

200

application/json

Successful Response

provider\_id

string<uuid>

required

organization\_id

string<uuid>

required

organization\_display\_name

string

required

provider\_type

enum<string>

default:saml

Available options:

`saml`,

`oidc`