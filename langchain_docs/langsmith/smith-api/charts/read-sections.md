---
title: "Read sections - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/charts/read-sections
scraped_at: 2026-11-15T03:40:43.473154
word_count: 88
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

default:100

Required range: `1 <= x <= 100`

offset

integer

default:0

Required range: `x >= 0`

title\_contains

string | null

ids

string<uuid>[] | null

sort\_by

string | null

default:created\_at

sort\_by\_desc

boolean | null

default:true

tag\_value\_id

string<uuid>[] | null

#### Response

200

application/json

Successful Response

title

string

required

id

string<uuid>

required

description

string | null

index

integer | null

chart\_count

integer | null

created\_at

string<date-time> | null

modified\_at

string<date-time> | null