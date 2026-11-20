---
title: "Add members to current org batch - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/add-members-to-current-org-batch
scraped_at: 2026-11-15T03:41:17.239727
word_count: 125
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

email

string

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