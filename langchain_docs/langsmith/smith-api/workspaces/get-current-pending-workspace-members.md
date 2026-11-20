---
title: "Get current pending workspace members - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/get-current-pending-workspace-members
scraped_at: 2026-11-15T03:42:19.933549
word_count: 140
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

limit

integer

default:50

Required range: `1 <= x <= 500`

offset

integer

default:0

Required range: `x >= 0`

emails

string[]

q

string | null

Search query for email or name

sort\_by\_desc

boolean

default:true

Sort in descending order

sort\_by

enum<string>

default:created\_at

Field to sort by

Available options:

`name`,

`email`,

`role`,

`created_at`

#### Response

200

application/json

Successful Response

email

string

required

id

string<uuid>

required

created\_at

string<date-time>

required

read\_only

boolean

default:false

deprecated

role\_id

string<uuid> | null

role\_name

string | null

workspace\_ids

string<uuid>[] | null

workspace\_role\_id

string<uuid> | null

workspace\_role\_name

string | null

password

string | null

full\_name

string | null

access\_scope

enum<string>

default:workspace

Available options:

`organization`,

`workspace`

user\_id

string<uuid> | null

tenant\_id

string<uuid> | null

organization\_id

string<uuid> | null

org\_role\_id

string<uuid> | null

org\_role\_name

string | null