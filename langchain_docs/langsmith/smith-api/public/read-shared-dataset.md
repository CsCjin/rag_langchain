---
title: "Read shared dataset - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/public/read-shared-dataset
scraped_at: 2026-11-15T03:41:34.744322
word_count: 133
---

#### Path Parameters

share\_token

string<uuid>

required

#### Query Parameters

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

#### Response

200

application/json

Successful Response

Public schema for datasets.

Doesn't currently include session counts/stats
since public test project sharing is not yet shipped

name

string

required

id

string<uuid>

required

example\_count

integer

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