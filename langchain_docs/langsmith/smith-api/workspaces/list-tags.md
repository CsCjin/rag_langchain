---
title: "List tags - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/list-tags
scraped_at: 2026-11-15T03:42:22.855369
word_count: 72
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

resource\_type

enum<string> | null

Available options:

`agent`,

`custom_app`,

`dashboard`,

`dataset`,

`deployment`,

`evaluator`,

`experiment`,

`fleet_integration`,

`mcp_server`,

`project`,

`prompt`,

`queue`,

`sandbox`,

`skill`,

`snapshot_name`

#### Response

200

application/json

Successful Response

key

string

required

Required string length: `1 - 255`

id

string<uuid>

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

description

string | null

values

TagValue · object[]

Show child attributes