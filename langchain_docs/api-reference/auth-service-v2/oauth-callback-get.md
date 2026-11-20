---
title: "Oauth Callback Get - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/oauth-callback-get
scraped_at: 2026-11-15T03:37:55.781856
word_count: 42
---

#### Path Parameters

provider\_id

string

required

#### Query Parameters

code

string

Authorization code from OAuth provider

state

string

State parameter containing auth\_id

error

string

Error code from OAuth provider

error\_description

string

Error description from OAuth provider

#### Response

200

application/json

Successful Response