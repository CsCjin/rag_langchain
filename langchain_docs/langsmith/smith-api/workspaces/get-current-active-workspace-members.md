---
title: "Get current active workspace members - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/get-current-active-workspace-members
scraped_at: 2026-11-15T03:42:19.698830
word_count: 157
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

ls\_user\_ids

string<uuid>[]

user\_ids

string<uuid>[]

deprecated

is\_disabled

boolean | null

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

email

string | null

full\_name

string | null

avatar\_url

string | null

linked\_login\_methods

ProviderUserSlim · object[]

Show child attributes

display\_name

string | null

is\_disabled

boolean

default:false

org\_identity\_id

string<uuid> | null

org\_role\_id

string<uuid> | null

org\_role\_name

string | null