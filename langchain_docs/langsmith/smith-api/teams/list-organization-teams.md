---
title: "List organization teams - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/teams/list-organization-teams
scraped_at: 2026-11-15T03:42:01.989706
word_count: 106
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

#### Query Parameters

workspace\_id

string<uuid>

Only return teams that belong to or are granted into this workspace

parent\_team\_id

string<uuid>

Only return workspace teams under this organization-wide team

identity\_id

string<uuid>

Only return teams this organization identity is a direct member of

page\_size

integer

default:20

Teams per page

Required range: `1 <= x <= 100`

cursor

string

Where to resume, taken from the previous page

#### Response

200

application/json

OK

items

object[]

required

Show child attributes

next\_cursor

string | null

required