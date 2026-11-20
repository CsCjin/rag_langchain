---
title: "Update feedback config endpoint - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/feedback-configs/update-feedback-config-endpoint
scraped_at: 2026-11-15T03:40:59.818359
word_count: 84
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

feedback\_key

string

required

id

string<uuid> | null

feedback\_config

FeedbackConfig · object | null

Show child attributes

is\_lower\_score\_better

boolean | null

add\_categories

FeedbackCategory · object[]

Show child attributes

remove\_categories

number[]

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