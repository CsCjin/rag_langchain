---
title: "Update Token Label - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/update-token-label
scraped_at: 2026-11-15T03:37:56.684240
word_count: 69
---

#### Path Parameters

token\_id

string

required

#### Body

application/json

Request model for updating a token's metadata.

provider\_account\_label

string | null

is\_default

boolean | null

#### Response

200

application/json

Successful Response

Public-facing token summary — no sensitive data.

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