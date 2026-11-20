---
title: "List feedback formula ep - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/feedback/list-feedback-formula-ep
scraped_at: 2026-11-15T03:41:01.326879
word_count: 78
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

dataset\_id

string<uuid> | null

session\_id

string<uuid> | null

limit

integer

default:20

offset

integer

default:0

#### Response

200

application/json

Successful Response

feedback\_key

string

required

aggregation\_type

enum<string>

required

Available options:

`sum`,

`avg`

formula\_parts

FeedbackFormulaWeightedVariable · object[]

required

Required array length: `1 - 50` elements

Show child attributes

id

string<uuid>

required

created\_at

string<date-time>

required

modified\_at

string<date-time>

required

dataset\_id

string<uuid> | null

session\_id

string<uuid> | null