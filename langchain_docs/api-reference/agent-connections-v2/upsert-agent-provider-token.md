---
title: "Upsert Agent Provider Token - Docs by LangChain"
url: https://docs.langchain.com/api-reference/agent-connections-v2/upsert-agent-provider-token
scraped_at: 2026-11-15T03:37:51.253984
word_count: 124
---

#### Path Parameters

agent\_id

string

required

Agent ID

provider\_id

string

required

OAuth provider ID

#### Body

application/json

Import an OAuth token and bind it to an agent for a provider.

Used by Managed Deep Agents Connect flows that obtain tokens out-of-band
(e.g. Google OAuth for Gmail) and need them stored under a synthetic
agent\_id for toolserver resolution.

access\_token

string

required

refresh\_token

string | null

expires\_in\_seconds

integer | null

scopes

string[]

provider\_account\_label

string | null

metadata

Metadata · object | null

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