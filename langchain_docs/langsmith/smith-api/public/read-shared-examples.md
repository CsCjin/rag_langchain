---
title: "Read shared examples - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/public/read-shared-examples
scraped_at: 2026-11-15T03:41:35.552481
word_count: 145
---

#### Path Parameters

share\_token

string<uuid>

required

#### Query Parameters

id

string<uuid>[] | null

as\_of

string<date-time>stringstring<date-time>string

default:latest

Only modifications made on or before this time are included. If None, the latest version of the dataset is used.

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

select

enum<string>[]

Available options:

`id`,

`created_at`,

`modified_at`,

`name`,

`dataset_id`,

`source_run_id`,

`source_session_id`,

`source_run_start_time`,

`source_trace_id`,

`source_thread_id`,

`metadata`,

`inputs`,

`outputs`,

`attachment_urls`

filter

string | null

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