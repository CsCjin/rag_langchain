---
title: "Create service account - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/service-accounts/create-service-account
scraped_at: 2026-11-15T03:41:57.087562
word_count: 55
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

name

string

required

workspaces

ServiceAccountWorkspaceAssignment · object[]

Show child attributes

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

updated\_at

string<date-time>

required

name

string

required

organization\_id

string<uuid>

required

default\_workspace\_id

string<uuid> | null

required

organization\_identity\_id

string<uuid>

required