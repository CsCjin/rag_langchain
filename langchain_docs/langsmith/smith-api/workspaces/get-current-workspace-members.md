---
title: "Get current workspace members - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/get-current-workspace-members
scraped_at: 2026-11-15T03:42:20.398249
word_count: 42
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Response

200 - application/json

Successful Response

Tenant members schema.

tenant\_id

string<uuid>

required

members

MemberIdentity · object[]

required

Show child attributes

pending

PendingIdentity · object[]

required

Show child attributes