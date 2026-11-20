---
title: "Get directory contents - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/directories/get-directory-contents
scraped_at: 2026-11-15T03:40:52.836446
word_count: 61
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

Repository owner handle or '-' for current tenant

repo

string

required

Repository handle

#### Query Parameters

commit

string

Commit hash/tag to resolve (defaults to latest)

#### Response

200

application/json

OK

commit\_hash

string

required

commit\_id

string<uuid>

required

files

object

required

Show child attributes