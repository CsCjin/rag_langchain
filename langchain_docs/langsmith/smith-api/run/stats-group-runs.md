---
title: "Stats group runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/stats-group-runs
scraped_at: 2026-11-15T03:41:40.710712
word_count: 198
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

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

group\_count

integer

required

run\_count

integer | null

latency\_p50

number | null

latency\_p99

number | null

first\_token\_p50

number | null

first\_token\_p99

number | null

total\_tokens

integer | null

prompt\_tokens

integer | null

completion\_tokens

integer | null

median\_tokens

integer | null

completion\_tokens\_p50

integer | null

prompt\_tokens\_p50

integer | null

tokens\_p99

integer | null

completion\_tokens\_p99

integer | null

prompt\_tokens\_p99

integer | null

last\_run\_start\_time

string<date-time> | null

feedback\_stats

Feedback Stats · object | null

run\_facets

Run Facets · object[] | null

error\_rate

number | null

streaming\_rate

number | null

total\_cost

number | null

prompt\_cost

number | null

completion\_cost

number | null

cost\_p50

number | null

cost\_p99

number | null

prompt\_token\_details

Prompt Token Details · object | null

completion\_token\_details

Completion Token Details · object | null

prompt\_cost\_details

Prompt Cost Details · object | null

completion\_cost\_details

Completion Cost Details · object | null