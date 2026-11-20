---
title: "List Token Events For User - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/list-token-events-for-user
scraped_at: 2026-11-15T03:37:55.436252
word_count: 72
---

#### Query Parameters

provider\_id

string | null

Filter to one OAuth provider

limit

integer

default:50

Max events to return

Required range: `1 <= x <= 200`

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

event\_type

string

required

created\_at

string<date-time>

required

agent\_id

string | null

reason

string | null

source

string | null

provider\_account\_label

string | null

scopes

string[]

detail

Detail · object | null

acknowledged\_at

string<date-time> | null