---
title: "List registries - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/list-registries
scraped_at: 2026-11-15T03:41:52.028417
word_count: 109
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

Number of results per cursor page

Required range: `1 <= x <= 100`

cursor

string

Opaque cursor from a prior response's next\_cursor

limit

integer

Deprecated: use page\_size. Maximum number of registries to return

offset

integer

Deprecated: use cursor. Number of registries to skip

name\_contains

string

Filter to registries whose name contains this substring

#### Response

200

application/json

OK

items

object[]

Show child attributes

next\_cursor

string | null

offset

integer

Deprecated: only applies to limit/offset requests. Use next\_cursor when paging with a cursor.

registries

object[]

Deprecated: use items.

Show child attributes