---
title: "List repo owners - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/ownerships/list-repo-owners
scraped_at: 2026-11-15T03:41:29.967761
word_count: 41
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

Response for listing repo owners.

owners

RepoOwner · object[]

required

Show child attributes