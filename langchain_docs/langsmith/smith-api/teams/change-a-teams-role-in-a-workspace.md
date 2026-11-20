---
title: "Change a team's role in a workspace - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/teams/change-a-teams-role-in-a-workspace
scraped_at: 2026-11-15T03:42:00.001448
word_count: 81
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

#### Body

application/json

role\_id

string<uuid>

required

RoleID is a workspace role: a built-in one, or a custom one in this organization.

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