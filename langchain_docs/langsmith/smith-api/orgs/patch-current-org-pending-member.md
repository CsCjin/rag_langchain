---
title: "Patch current org pending member - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/patch-current-org-pending-member
scraped_at: 2026-11-15T03:41:26.320815
word_count: 106
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

identity\_id

string<uuid>

required

#### Body

application/json

role\_id

string<uuid> | null

role\_name

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

tenant\_ids

string<uuid>[]