---
title: "Remove a member from a team - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/teams/remove-a-member-from-a-team
scraped_at: 2026-11-15T03:42:02.292504
word_count: 49
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

identity\_id

string<uuid>

required

Organization identity ID of the member

#### Response

204

No Content