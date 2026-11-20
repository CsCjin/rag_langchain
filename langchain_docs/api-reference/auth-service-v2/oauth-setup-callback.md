---
title: "Oauth Setup Callback - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/oauth-setup-callback
scraped_at: 2026-11-15T03:37:56.036894
word_count: 55
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

setup\_action

string

Setup action from GitHub App

installation\_id

integer

GitHub App installation ID

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