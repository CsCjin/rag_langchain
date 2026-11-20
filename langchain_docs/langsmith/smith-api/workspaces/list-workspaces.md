---
title: "List workspaces - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/list-workspaces
scraped_at: 2026-11-15T03:42:23.488281
word_count: 80
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

include\_deleted

boolean

default:false

data\_plane\_id

string<uuid> | null

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