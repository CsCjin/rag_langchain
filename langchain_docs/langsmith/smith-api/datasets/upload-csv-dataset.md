---
title: "Upload csv dataset - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/upload-csv-dataset
scraped_at: 2026-11-15T03:40:51.987195
word_count: 167
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

multipart/form-data

file

file

required

input\_keys

string[]

required

name

string | null

data\_type

enum<string>

default:kv

Enum for dataset data types.

Available options:

`kv`,

`llm`,

`chat`

output\_keys

string[]

metadata\_keys

string[]

description

string | null

inputs\_schema\_definition

string | null

outputs\_schema\_definition

string | null

transformations

string | null

input\_key\_mappings

string | null

output\_key\_mappings

string | null

metadata\_key\_mappings

string | null

tag\_value\_ids

string | null

#### Response

200

application/json

Successful Response

Dataset schema.

name

string

required

id

string<uuid>

required

tenant\_id

string<uuid>

required

session\_count

integer

required

modified\_at

string<date-time>

required

description

string | null

created\_at

string<date-time>

inputs\_schema\_definition

Inputs Schema Definition · object | null

outputs\_schema\_definition

Outputs Schema Definition · object | null

externally\_managed

boolean | null

default:false

transformations

DatasetTransformation · object[] | null

Show child attributes

data\_type

enum<string> | null

default:kv

Enum for dataset data types.

Available options:

`kv`,

`llm`,

`chat`

example\_count

integer | null

last\_session\_start\_time

string<date-time> | null

metadata

Metadata · object | null

baseline\_experiment\_id

string<uuid> | null