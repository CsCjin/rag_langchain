---
title: "Validate example - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/examples/validate-example
scraped_at: 2026-11-15T03:40:56.601974
word_count: 71
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

Validation result for Example, combining fields from Create/Base/Update schemas.

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