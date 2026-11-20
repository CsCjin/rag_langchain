---
title: "Delete directory repository - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/directories/delete-directory-repository
scraped_at: 2026-11-15T03:40:52.418222
word_count: 58
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

repo\_type

enum<string>

Repository type to delete; a different type is treated as not found

Available options:

`agent`,

`skill`

#### Response

204

No Content