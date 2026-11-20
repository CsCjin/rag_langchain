---
title: "Create tenant - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tenant/create-tenant
scraped_at: 2026-11-15T03:42:03.298107
word_count: 99
---

#### Authorizations

Authorization

string

header

required

Bearer tokens are used to authenticate from the UI. Must also specify x-tenant-id or x-organization-id (for org scoped apis).

#### Body

application/json

Creation model for the tenant.

display\_name

string

required

Minimum string length: `1`

Pattern: `^[a-zA-Z0-9\-_ ']+$`

id

string<uuid>

organization\_id

string<uuid> | null

tenant\_handle

string | null

is\_personal

boolean

default:false

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