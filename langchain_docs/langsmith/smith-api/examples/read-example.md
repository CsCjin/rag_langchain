---
title: "Read example - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/examples/read-example
scraped_at: 2026-11-15T03:40:55.613563
word_count: 116
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

example\_id

string<uuid>

required

#### Query Parameters

as\_of

string<date-time>stringstring<date-time>string

default:latest

Only modifications made on or before this time are included. If None, the latest version of the dataset is used.

dataset

string<uuid> | null

#### Response

200

application/json

Successful Response

Example schema.

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