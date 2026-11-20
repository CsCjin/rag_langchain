---
title: "Claim pending workspace invite - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/claim-pending-workspace-invite
scraped_at: 2026-11-15T03:42:16.960953
word_count: 37
---

#### Authorizations

Authorization

string

header

required

Bearer tokens are used to authenticate from the UI. Must also specify x-tenant-id or x-organization-id (for org scoped apis).

#### Path Parameters

workspace\_id

string<uuid>

required

#### Response

200

application/json

Successful Response