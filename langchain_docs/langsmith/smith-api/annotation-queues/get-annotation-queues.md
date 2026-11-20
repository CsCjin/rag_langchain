---
title: "Get annotation queues - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-annotation-queues
scraped_at: 2026-11-15T03:40:29.545102
word_count: 148
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

ids

string<uuid>[] | null

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

tag\_value\_id

string<uuid>[] | null

dataset\_id

string<uuid> | null

queue\_type

enum<string> | null

Available options:

`single`,

`pairwise`

assigned\_to\_me

boolean

default:false

sort\_by

string | null

sort\_by\_desc

boolean

default:true

#### Response

200

application/json

Successful Response

name

string

required

id

string<uuid>

required

tenant\_id

string<uuid>

required

queue\_type

enum<string>

required

Available options:

`single`,

`pairwise`

total\_runs

integer

required

description

string | null

created\_at

string<date-time>

updated\_at

string<date-time>

num\_reviewers\_per\_item

integer | null

default:1

enable\_reservations

boolean | null

default:true

reservation\_minutes

integer | null

default:1

reviewer\_access\_mode

string

default:any

source\_rule\_id

string<uuid> | null

run\_rule\_id

string<uuid> | null

default\_dataset

string<uuid> | null

metadata

Metadata · object | null

assigned\_reviewers

AssignedReviewerSchema · object[]

Show child attributes