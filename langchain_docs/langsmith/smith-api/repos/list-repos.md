---
title: "List repos - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/repos/list-repos
scraped_at: 2026-11-15T03:41:37.426351
word_count: 227
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

limit

integer

default:20

deprecated

Deprecated: use page\_size and cursor.

Required range: `1 <= x <= 100`

offset

integer

default:0

deprecated

Deprecated: use page\_size and cursor.

Required range: `x >= 0`

page\_size

integer

default:20

Number of repos per page. Max 100.

Required range: `1 <= x <= 100`

cursor

string | null

Opaque cursor from the previous response's next\_cursor. Omit for the first page. Cannot be combined with offset.

with\_latest\_manifest

boolean

default:false

include\_owners

boolean

default:false

tenant\_handle

string | null

tenant\_id

string<uuid> | null

query

string | null

has\_commits

boolean | null

tags

string[] | null

is\_archived

enum<string> | null

Available options:

`true`,

`allow`,

`false`

is\_public

enum<string> | null

Available options:

`true`,

`false`

upstream\_repo\_owner

string | null

upstream\_repo\_handle

string | null

tag\_value\_id

string<uuid>[] | null

repo\_type

enum<string> | null

Available options:

`prompt`,

`file`,

`agent`,

`skill`

repo\_types

enum<string>[] | null

Available options:

`prompt`,

`file`,

`agent`,

`skill`

source

enum<string> | null

Available options:

`internal`,

`external`

sort\_field

enum<string> | null

Available options:

`num_likes`,

`num_downloads`,

`num_views`,

`updated_at`,

`relevance`

sort\_direction

Sort Direction · stringSort Direction · stringSort Direction · stringSort Direction · string

Allowed value: `"asc"`

#### Response

200

application/json

Successful Response

repos

RepoWithLookups · object[]

required

Show child attributes

total

integer

required

next\_cursor

string | null

Cursor for the next page, or null when no pages remain.