---
title: "Create feedback formula ep - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/feedback/create-feedback-formula-ep
scraped_at: 2026-11-15T03:41:00.160691
word_count: 97
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

dataset\_id

string<uuid> | null

session\_id

string<uuid> | null

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