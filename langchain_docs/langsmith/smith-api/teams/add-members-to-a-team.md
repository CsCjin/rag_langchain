---
title: "Add members to a team - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/teams/add-members-to-a-team
scraped_at: 2026-11-15T03:42:00.101085
word_count: 69
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

#### Body

application/json

identity\_ids

string<uuid>[]

required

IdentityIDs are the organization identities of the users to add.

Required array length: `1 - 100` elements

#### Response

207

application/json

Multi-Status

statuses

object[]

required

Show child attributes