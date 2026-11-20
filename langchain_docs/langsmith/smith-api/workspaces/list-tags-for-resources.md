---
title: "List tags for resources - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/list-tags-for-resources
scraped_at: 2026-11-15T03:42:23.298406
word_count: 52
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

resource\_id

string<uuid>

required

resource\_type

enum<string>

required

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

{key}

TagKeyWithValuesAndTaggings · object[]

Show child attributes