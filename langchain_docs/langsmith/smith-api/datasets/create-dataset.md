---
title: "Create dataset - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/create-dataset
scraped_at: 2026-11-15T03:40:47.269637
word_count: 182
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Create class for Dataset.

name

string

required

tag\_value\_ids

string<uuid>[] | null

Maximum array length: `100`

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

id

string<uuid> | null

extra

Extra · object | null

data\_type

enum<string>

default:kv

Enum for dataset data types.

Available options:

`kv`,

`llm`,

`chat`

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