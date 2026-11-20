---
title: "Create directory commit - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/directories/create-directory-commit
scraped_at: 2026-11-15T03:40:52.202655
word_count: 80
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

#### Body

application/json

files

object

Paths to create, update, link, delete, or unlink. Use null to delete or unlink an existing path.

Show child attributes

parent\_commit

string

skip\_webhooks

boolean

SkipWebhooks suppresses Context Hub commit webhooks for this commit.

#### Response

200

application/json

OK

commit

object

Show child attributes