---
title: "Rename filter view - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/rename-filter-view
scraped_at: 2026-11-15T03:42:12.309044
word_count: 101
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

session\_id

string<uuid>

required

Project ID

view\_id

string<uuid>

required

Saved view ID

#### Body

application/json

display\_name

string

required

description

string | null

#### Response

200

application/json

OK

created\_at

string<date-time>

required

display\_name

string

required

id

string<uuid>

required

updated\_at

string<date-time>

required

description

string | null

duration

string | null

end\_time

string<date-time> | null

filter\_string

string | null

session\_id

string<uuid> | null

start\_time

string<date-time> | null

syntax\_version

integer

default:1

thread\_filter\_string

string | null

trace\_filter\_string

string | null

tree\_filter\_string

string | null

type

enum<string>

default:runs

Available options:

`runs`,

`threads`,

`single_run`