---
title: "List sandboxes - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/list-sandboxes
scraped_at: 2026-11-15T03:41:52.180913
word_count: 208
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

limit

integer

default:50

Deprecated: use page\_size. Maximum number of results

offset

integer

default:0

Deprecated: use cursor. Pagination offset

name\_contains

string

Filter by name substring

status

string

Filter by status (provisioning, ready, failed, stopped, deleting)

tag\_value\_id

string[]

Filter by workspace resource tag value IDs; all must match

created\_by

string

Filter by creator identity. Only 'me' is supported.

label

string[]

Filter by label. Repeatable; all must match. Use 'key' to match on key presence or 'key=value' for equality.

sort\_by

string

default:created\_at

Sort column (name, status, created\_at, stopped\_at, idle\_ttl\_seconds, delete\_after\_stop\_seconds)

sort\_order

string

default:desc

Sort direction (asc, desc)

sort\_direction

string

default:desc

Deprecated: use sort\_order. Sort direction (asc, desc)

#### Response

200

application/json

OK

items

object[]

This page of sandboxes.

Show child attributes

next\_cursor

string

Cursor for the next page, or null on the last page. A non-null value is
the only signal that more pages exist. Treat it as opaque.

offset

integer

Deprecated: use next\_cursor. Offset to request for the next page, or 0
when no pages remain.

sandboxes

object[]

Deprecated: use items. Duplicates items.

Show child attributes