---
title: "Add repo owner - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/ownerships/add-repo-owner
scraped_at: 2026-11-15T03:41:29.870948
word_count: 84
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

owner

string

required

repo

string

required

#### Body

application/json

Request to add a repo owner.

email

string

required

#### Response

200

application/json

Successful Response

A repo owner with user details.

Note: identity\_id and email may be None when returned to users
outside the repo's tenant (PII protection).

identity\_id

string<uuid> | null

required

ls\_user\_id

string<uuid>

required

email

string | null

required

full\_name

string | null

required

created\_at

string<date-time>

required