---
title: "Create tagging - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/create-tagging
scraped_at: 2026-11-15T03:42:17.370462
word_count: 80
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

tag\_value\_id

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

resource\_id

string<uuid>

required

#### Response

200

application/json

Successful Response

tag\_value\_id

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

resource\_id

string<uuid>

required

id

string<uuid>

required

created\_at

string<date-time>

required