---
title: "Get repo - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/repos/get-repo
scraped_at: 2026-11-15T03:41:36.984891
word_count: 45
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

#### Response

200

application/json

Successful Response

repo

RepoWithLookups · object

required

All database fields for repos, plus helpful computed fields.

Show child attributes