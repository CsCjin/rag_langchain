---
title: "List tenants - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tenant/list-tenants
scraped_at: 2026-11-15T03:42:03.549361
word_count: 91
---

#### Authorizations

Authorization

string

header

required

Bearer tokens are used to authenticate from the UI. Must also specify x-tenant-id or x-organization-id (for org scoped apis).

#### Query Parameters

skip\_create

boolean

default:false

include\_deleted

boolean

default:false

#### Response

200

application/json

Successful Response

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

read\_only

boolean

default:false

deprecated

role\_id

string<uuid> | null

role\_name

string | null

permissions

string[] | null