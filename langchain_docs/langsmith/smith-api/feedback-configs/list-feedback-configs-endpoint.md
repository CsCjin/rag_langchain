---
title: "List feedback configs endpoint - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/feedback-configs/list-feedback-configs-endpoint
scraped_at: 2026-11-15T03:40:59.456894
word_count: 138
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

key

string[] | null

Maximum array length: `50`

name\_contains

string | null

offset

integer

default:0

Required range: `x >= 0`

limit

integer | null

Required range: `1 <= x <= 100`

sort\_by\_desc

boolean

default:true

read\_after\_write

boolean

default:false

is\_enforced

boolean | null

Only enforced configs when true, only unenforced when false.

include\_all\_configs

boolean

default:false

Return every config of each key, deleted ones included, instead of one config per key. Pages of up to 100 configs unless `limit` is set; `X-Pagination-Total` gives the full count.

#### Response

200

application/json

Successful Response

id

string<uuid>

required

feedback\_key

string

required

feedback\_config

FeedbackConfig · object

required

Show child attributes

tenant\_id

string<uuid>

required

modified\_at

string<date-time>

required

is\_lower\_score\_better

boolean | null

is\_enforced

boolean

default:false

is\_first

boolean

default:false

is\_deleted

boolean

default:false