---
title: "List Oauth Tokens For User - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/list-oauth-tokens-for-user
scraped_at: 2026-11-15T03:37:54.937608
word_count: 48
---

#### Query Parameters

provider\_id

string | null

OAuth provider ID

#### Response

200

application/json

Successful Response

id

string

required

provider\_id

string

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

provider\_account\_label

string | null

scopes

string[]

expires\_at

string<date-time> | null

is\_default

boolean

default:false

status

string

default:active

status\_reason

string | null