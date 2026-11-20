---
title: "Create example - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/examples/create-example
scraped_at: 2026-11-15T03:40:54.368325
word_count: 160
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Create class for Example.

dataset\_id

string<uuid>

required

outputs

Outputs · object | null

deprecated

Deprecated: use reference\_outputs instead.

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

inputs

Inputs · object | null

split

string[]stringstring[]string

id

string<uuid> | null

use\_source\_run\_io

boolean

default:false

use\_source\_run\_attachments

string[]

use\_legacy\_message\_format

boolean

default:false

Use Legacy Message Format for LLM runs

created\_at

string

reference\_outputs

Reference Outputs · object | null

#### Response

200 - application/json

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