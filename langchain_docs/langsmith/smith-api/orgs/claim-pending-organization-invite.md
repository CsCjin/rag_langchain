---
title: "Claim pending organization invite - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/claim-pending-organization-invite
scraped_at: 2026-11-15T03:41:17.744571
word_count: 75
---

#### Authorizations

Authorization

string

header

required

Bearer tokens are used to authenticate from the UI. Must also specify x-tenant-id or x-organization-id (for org scoped apis).

#### Path Parameters

organization\_id

string<uuid>

required

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