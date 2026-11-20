---
title: "Create Connection - Docs by LangChain"
url: https://docs.langchain.com/api-reference/agent-connections-v2/create-connection
scraped_at: 2026-11-15T03:37:51.040516
word_count: 58
---

#### Path Parameters

agent\_id

string

required

Agent ID

#### Body

application/json

oauth\_token\_id

string

required

#### Response

201

application/json

Successful Response

id

string

required

agent\_id

string

required

oauth\_token\_id

string

required

provider\_id

string

required

provider\_account\_label

string | null

required

scopes

string[]

required

expires\_at

string<date-time> | null

required

created\_by

string

required

created\_at

string<date-time>

required

status

string

default:active

status\_reason

string | null