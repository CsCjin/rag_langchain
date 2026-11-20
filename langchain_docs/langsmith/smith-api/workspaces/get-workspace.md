---
title: "Get workspace - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/get-workspace
scraped_at: 2026-11-15T03:42:21.608405
word_count: 106
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

workspace\_id

string<uuid>

required

#### Query Parameters

include\_deleted

boolean

default:false

Also return the workspace if it has been deleted.

data\_plane\_id

string<uuid> | null

Accepted only from a data plane service; other callers get 403.

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