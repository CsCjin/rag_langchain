---
title: "Patch workspace - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/patch-workspace
scraped_at: 2026-11-15T03:42:24.069877
word_count: 94
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

workspace\_id

string<uuid>

required

#### Body

application/json

Patch model for the workspace.

display\_name

string

required

New workspace name. Letters, digits, spaces and - \_ ' @ ( ) only.

Minimum string length: `1`

Pattern: `^[a-zA-Z0-9\-_ '@()]+$`

#### Response

200

application/json

Successful Response

Tenant schema.

id

string<uuid>

required

created\_at

string<date-time>

required

display\_name

string

required

is\_personal

boolean

required

is\_deleted

boolean

required

organization\_id

string<uuid> | null

tenant\_handle

string | null

data\_plane\_url

string | null

data\_plane\_name

string | null

data\_plane\_region

string | null