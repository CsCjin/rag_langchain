---
title: "Attach an access policy to a team - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/teams/attach-an-access-policy-to-a-team
scraped_at: 2026-11-15T03:41:59.699421
word_count: 138
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

access\_policy\_id

string<uuid>

required

workspace\_id

string<uuid>

WorkspaceID limits an organization-wide team's policy to one workspace. Omit it to apply
the policy in every workspace the team has access to. A workspace team's policy always
applies in the team's workspace, so this must be omitted or match it.

#### Response

200

application/json

The policy was already attached

attached\_at

string

required

description

string

required

effect

enum<string>

required

Available options:

`allow`,

`deny`

id

string<uuid>

required

name

string

required

workspace\_id

string<uuid>

WorkspaceID is the workspace the policy applies in. It is omitted when the policy applies
in every workspace an organization-wide team has access to.