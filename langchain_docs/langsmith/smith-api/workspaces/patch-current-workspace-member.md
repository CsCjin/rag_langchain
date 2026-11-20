---
title: "Patch current workspace member - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/patch-current-workspace-member
scraped_at: 2026-11-15T03:42:23.652484
word_count: 36
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

identity\_id

string<uuid>

required

#### Body

application/json

role\_id

string<uuid>

required

read\_only

boolean | null

deprecated

#### Response

200

application/json

Successful Response