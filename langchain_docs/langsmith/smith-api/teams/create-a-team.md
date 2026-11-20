---
title: "Create a team - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/teams/create-a-team
scraped_at: 2026-11-15T03:42:00.213333
word_count: 132
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

#### Body

application/json

name

string

required

Required string length: `1 - 255`

description

string

parent\_team\_id

string<uuid>

workspace\_id

string<uuid>

Rejected with 400, so a request for a workspace team does not create an
organization-wide team. Granting a team a workspace creates its workspace team.

#### Response

201

application/json

Created

created\_at

string

required

description

string

required

id

string<uuid>

required

idp\_sync\_enabled

boolean

required

name

string

required

organization\_id

string<uuid>

required

updated\_at

string

required

idp\_group\_name

string

parent\_team\_id

string<uuid>

ParentTeamID is the organization-wide team a workspace team belongs to.
It is omitted for organization-wide teams.

workspace\_id

string<uuid>

WorkspaceID is the workspace the team belongs to. It is omitted for
organization-wide teams.