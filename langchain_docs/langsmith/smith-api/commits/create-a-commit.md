---
title: "Create a commit - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/commits/create-a-commit
scraped_at: 2026-11-15T03:40:45.273497
word_count: 76
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

Repository owner (tenant handle) or '-' for private repos

repo

string

required

Repository handle

#### Body

application/json

description

string

manifest

object

parent\_commit

string

skip\_webhooks

any

SkipWebhooks allows skipping webhook notifications. Can be true (boolean) to skip all, or an array of webhook UUIDs to skip specific ones.

#### Response

201

application/json

Created

commit

object

Show child attributes