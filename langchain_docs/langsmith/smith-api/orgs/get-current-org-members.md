---
title: "Get current org members - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/get-current-org-members
scraped_at: 2026-11-15T03:41:21.756811
word_count: 42
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Response

200 - application/json

Successful Response

Organization members schema.

organization\_id

string<uuid>

required

members

OrgMemberIdentity · object[]

required

Show child attributes

pending

OrgPendingIdentity · object[]

required

Show child attributes