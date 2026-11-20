---
title: "Create workspace - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/create-workspace
scraped_at: 2026-11-15T03:42:17.755627
word_count: 80
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Creation model for the workspace.

display\_name

string

required

Minimum string length: `1`

Pattern: `^[a-zA-Z0-9\-_ '@()]+$`

id

string<uuid>

tenant\_handle

string | null

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