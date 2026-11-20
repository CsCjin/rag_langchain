---
title: "Detach access policies from a role - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/access_policies/detach-access-policies-from-a-role
scraped_at: 2026-11-15T03:40:24.344257
word_count: 39
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

role\_id

string

required

Role ID

#### Query Parameters

access\_policy\_ids

string[]

required

Access policy IDs to detach

#### Response

204

Access policies detached successfully