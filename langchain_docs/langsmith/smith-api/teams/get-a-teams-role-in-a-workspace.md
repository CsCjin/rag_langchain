---
title: "Get a team's role in a workspace - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/teams/get-a-teams-role-in-a-workspace
scraped_at: 2026-11-15T03:42:01.171650
word_count: 60
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

workspace\_id

string<uuid>

required

Workspace ID

#### Response

200

application/json

OK

created\_at

string

required

role\_id

string<uuid>

required

role\_name

string

required

updated\_at

string

required

workspace\_id

string<uuid>

required