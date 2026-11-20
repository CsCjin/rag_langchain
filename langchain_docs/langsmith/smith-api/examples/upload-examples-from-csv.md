---
title: "Upload examples from csv - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/examples/upload-examples-from-csv
scraped_at: 2026-11-15T03:40:56.482707
word_count: 97
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

#### Body

multipart/form-data

file

file

required

input\_keys

string[]

required

output\_keys

string[]

metadata\_keys

string[]

#### Response

200

application/json

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