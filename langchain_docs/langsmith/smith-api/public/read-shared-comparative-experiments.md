---
title: "Read shared comparative experiments - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/public/read-shared-comparative-experiments
scraped_at: 2026-11-15T03:41:34.651414
word_count: 98
---

#### Path Parameters

share\_token

string<uuid>

required

#### Query Parameters

name

string | null

name\_contains

string | null

offset

integer

default:0

Required range: `x >= 0`

limit

integer

default:100

Required range: `1 <= x <= 100`

sort\_by

enum<string>

default:created\_at

Enum for available comparative experiment columns to sort by.

Available options:

`name`,

`created_at`

sort\_by\_desc

boolean

default:true

#### Response

200

application/json

Successful Response

id

string<uuid>

required

created\_at

string<date-time>

required

modified\_at

string<date-time>

required

experiments\_info

SimpleExperimentInfo · object[]

required

Show child attributes

name

string | null

description

string | null

extra

Extra · object | null

feedback\_stats

Feedback Stats · object | null