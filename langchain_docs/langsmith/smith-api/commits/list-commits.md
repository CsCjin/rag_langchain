---
title: "List commits - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/commits/list-commits
scraped_at: 2026-11-15T03:40:46.964979
word_count: 193
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

owner

string

required

Repository owner (tenant handle) or '-' for private repos

repo

string

required

Repository handle

#### Query Parameters

cursor

string

Cursor is the next\_cursor value from a previous response. Omit it to request the first page.
Cannot be combined with limit or offset.

include\_stats

boolean

default:true

IncludeStats determines whether to compute num\_downloads and num\_views

limit

integer

default:20

Limit is the pagination limit. Deprecated: use page\_size and cursor.

Required range: `1 <= x <= 100`

offset

integer

default:0

Offset is the pagination offset. Deprecated: use page\_size and cursor.

Required range: `x >= 0`

page\_size

integer

default:20

PageSize is the maximum number of commits to return. Cannot be combined with limit or offset.

Required range: `1 <= x <= 100`

tag

string

Tag filters commits to only those with a specific tag (e.g. "production", "staging")

#### Response

200

application/json

OK

commits

object[]

List of commits with lookup information

Show child attributes

next\_cursor

string | null

NextCursor is the cursor for the next page, or null when there are no more commits.

total

integer

Total number of commits