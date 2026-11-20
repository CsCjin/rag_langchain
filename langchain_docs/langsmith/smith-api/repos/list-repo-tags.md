---
title: "List repo tags - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/repos/list-repo-tags
scraped_at: 2026-11-15T03:41:37.266267
word_count: 125
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

Required range: `1 <= x <= 100`

offset

integer

default:0

Required range: `x >= 0`

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

#### Response

200

application/json

Successful Response

tags

TagCount · object[]

required

Show child attributes