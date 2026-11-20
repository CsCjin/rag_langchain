---
title: "Update a team - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/teams/update-a-team
scraped_at: 2026-11-15T03:42:03.001455
word_count: 151
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

description

string | null

Description is cleared by null.

idp\_group\_name

string | null

IdpGroupName is cleared by null. Workspace scoped teams cannot have one.

Required string length: `1 - 255`

idp\_sync\_enabled

boolean

IdpSyncEnabled can be true only while the team has an IdpGroupName.

name

string

Required string length: `1 - 255`

#### Response

200

application/json

OK

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