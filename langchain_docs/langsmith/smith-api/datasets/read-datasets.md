---
title: "Read datasets - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/read-datasets
scraped_at: 2026-11-15T03:40:50.222304
word_count: 188
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

id

string<uuid>[] | null

data\_type

enum<string>[]enum<string>enum<string>[]enum<string>

Enum for dataset data types.

Available options:

`kv`,

`llm`,

`chat`

name

string | null

name\_contains

string | null

metadata

string | null

offset

integer

default:0

Required range: `x >= 0`

limit

integer

default:100

Required range: `1 <= x <= 100`

sort\_by

enum<string>

default:last\_session\_start\_time

Enum for available dataset columns to sort by.

Available options:

`name`,

`created_at`,

`last_session_start_time`,

`example_count`,

`session_count`,

`modified_at`

sort\_by\_desc

boolean

default:true

tag\_value\_id

string<uuid>[] | null

exclude\_corrections\_datasets

boolean

default:false

exclude

enum<string>[] | null

Available options:

`example_count`

#### Response

200

application/json

Successful Response

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