---
title: "Remove repo owner - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/ownerships/remove-repo-owner
scraped_at: 2026-11-15T03:41:30.099827
word_count: 40
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

Request to remove a repo owner.

identity\_id

string<uuid>

required

#### Response

200

application/json

Successful Response