---
title: "Validate examples - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/examples/validate-examples
scraped_at: 2026-11-15T03:40:56.780808
word_count: 62
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Response

200 - application/json

Successful Response

dataset\_id

string<uuid> | null

inputs

Inputs · object | null

outputs

Outputs · object | null

created\_at

string<date-time> | null

metadata

Metadata · object | null

source\_run\_id

string<uuid> | null

split

string[]stringstring[]string

id

string<uuid> | null

use\_source\_run\_io

boolean

default:false

overwrite

boolean

default:false