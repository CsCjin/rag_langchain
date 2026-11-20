---
title: "Get feedback formula ep - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/feedback/get-feedback-formula-ep
scraped_at: 2026-11-15T03:41:02.055194
word_count: 67
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

feedback\_formula\_id

string<uuid>

required

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