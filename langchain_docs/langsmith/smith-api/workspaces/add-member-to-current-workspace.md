---
title: "Add member to current workspace - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/add-member-to-current-workspace
scraped_at: 2026-11-15T03:42:15.907985
word_count: 82
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

user\_id

string<uuid> | null

deprecated

org\_identity\_id

string<uuid> | null

ls\_user\_id

string<uuid> | null

read\_only

boolean | null

deprecated

role\_id

string<uuid> | null

#### Response

200

application/json

Successful Response

id

string<uuid>

required

organization\_id

string<uuid>

required

created\_at

string<date-time>

required

user\_id

string<uuid>

required

ls\_user\_id

string<uuid>

required

read\_only

boolean

required

deprecated

tenant\_id

string<uuid> | null

role\_id

string<uuid> | null

role\_name

string | null

access\_scope

enum<string>

default:workspace

Available options:

`organization`,

`workspace`