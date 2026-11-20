---
title: "List a team's workspace grants - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/teams/list-a-teams-workspace-grants
scraped_at: 2026-11-15T03:42:01.784048
word_count: 77
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

#### Query Parameters

page\_size

integer

default:20

Grants per page

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