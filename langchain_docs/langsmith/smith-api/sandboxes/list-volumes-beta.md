---
title: "List volumes (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/list-volumes-beta
scraped_at: 2026-11-15T03:41:52.578747
word_count: 65
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

page\_size

integer

default:20

Number of results per page

cursor

string

Opaque pagination cursor from a prior response's next\_cursor

name\_contains

string

Filter by name substring

#### Response

200

application/json

OK

items

object[]

Show child attributes

next\_cursor

string | null

Cursor for the next page, or null on the last page.