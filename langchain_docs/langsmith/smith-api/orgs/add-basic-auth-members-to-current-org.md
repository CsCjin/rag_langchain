---
title: "Add basic auth members to current org - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/add-basic-auth-members-to-current-org
scraped_at: 2026-11-15T03:41:17.050450
word_count: 85
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

user\_id

string<uuid> | null

ls\_user\_id

string<uuid> | null

read\_only

boolean | null

deprecated

role\_id

string<uuid> | null

password

string | null

full\_name

string | null

workspace\_role\_id

string<uuid> | null

workspace\_ids

string<uuid>[] | null

#### Response

200

application/json

Successful Response

id

string<uuid>

required

ls\_user\_id

string<uuid>

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

email

string

required

full\_name

string | null

avatar\_url

string | null

password

string | null