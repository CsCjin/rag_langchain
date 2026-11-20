---
title: "Read charts - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/charts/read-charts
scraped_at: 2026-11-15T03:40:43.390719
word_count: 61
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

timezone

string

default:UTC

start\_time

string<date-time> | null

end\_time

string<date-time> | null

stride

TimedeltaInput · object

Timedelta input.

Show child attributes

omit\_data

boolean

default:false

after\_index

integer | null

tag\_value\_id

string<uuid>[] | null

#### Response

200

application/json

Successful Response

sections

CustomChartsSection · object[]

required

Show child attributes