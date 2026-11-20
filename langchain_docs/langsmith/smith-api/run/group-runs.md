---
title: "Group runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/group-runs
scraped_at: 2026-11-15T03:41:39.184035
word_count: 67
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Headers

accept

string | null

#### Body

application/json

session\_id

string<uuid>

required

group\_by

enum<string>

required

Available options:

`conversation`

filter

string | null

start\_time

string<date-time> | null

end\_time

string<date-time> | null

offset

integer

default:0

Required range: `x >= 0`

limit

integer

default:10

Required range: `1 <= x <= 100`

#### Response

200

application/json

Successful Response