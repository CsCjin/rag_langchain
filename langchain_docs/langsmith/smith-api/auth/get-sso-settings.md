---
title: "Get SSO settings - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/auth/get-sso-settings
scraped_at: 2026-11-15T03:40:36.416404
word_count: 28
---

#### Path Parameters

sso\_login\_slug

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