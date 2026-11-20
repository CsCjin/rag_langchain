---
title: "Detach an access policy from a team - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/teams/detach-an-access-policy-from-a-team
scraped_at: 2026-11-15T03:42:00.581569
word_count: 57
---

#### Authorizations

API Key & Organization IDBearer Auth & Organization IDAPI Key & Organization IDBearer Auth & Organization ID

X-API-Key

string

header

required

X-Organization-Id

string

header

required

#### Path Parameters

team\_id

string<uuid>

required

Team ID

access\_policy\_id

string<uuid>

required

Access policy ID

#### Query Parameters

workspace\_id

string<uuid>

Workspace the policy was attached in

#### Response

204

No Content