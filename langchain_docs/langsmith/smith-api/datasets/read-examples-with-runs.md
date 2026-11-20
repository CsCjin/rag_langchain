---
title: "Read examples with runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/read-examples-with-runs
scraped_at: 2026-11-15T03:40:50.489109
word_count: 213
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

dataset\_id

string<uuid>

required

#### Query Parameters

format

string | null

Response format, e.g., 'csv'

Allowed value: `"csv"`

#### Body

application/json

Request DTO for querying examples with runs - used for API input.

This is separate from the internal schema to cleanly handle optional limit values.
When limit is None, the internal schema will apply appropriate defaults based on
format.

session\_ids

string<uuid>[]

required

Minimum array length: `1`

offset

integer

default:0

Required range: `x >= 0`

limit

integer | null

Required range: `x >= 1`

preview

boolean

default:false

comparative\_experiment\_id

string<uuid> | null

sort\_params

SortParamsForRunsComparisonView · object | null

Show child attributes

filters

Filters · object | null

Show child attributes

example\_ids

string<uuid>[] | null

Maximum array length: `1000`

include\_annotator\_detail

boolean

default:false

#### Response

200

application/json

ExampleWithRunsCH · object[] | null

Successful Response

dataset\_id

string<uuid>

required

inputs

Inputs · object

required

id

string<uuid>

required

name

string

required

runs

RunSchemaComparisonView · object[]

required

Show child attributes

outputs

Outputs · object | null

source\_run\_id

string<uuid> | null

source\_session\_id

string<uuid> | null

source\_run\_start\_time

string<date-time> | null

source\_trace\_id

string<uuid> | null

metadata

Metadata · object | null

created\_at

string<date-time>

modified\_at

string<date-time> | null

source\_thread\_id

string | null

attachment\_urls

Attachment Urls · object | null