---
title: "Read examples - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/examples/read-examples
scraped_at: 2026-11-15T03:40:55.743040
word_count: 204
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

as\_of

string<date-time>stringstring<date-time>string

default:latest

Only modifications made on or before this time are included. If None, the latest version of the dataset is used.

metadata

string | null

full\_text\_contains

string[] | null

splits

string[] | null

dataset

string<uuid> | null

offset

integer

default:0

Required range: `x >= 0`

limit

integer

default:100

Required range: `1 <= x <= 100`

order

enum<string>

default:recent

Available options:

`recent`,

`random`,

`recently_created`,

`id`

random\_seed

number | null

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

exclude\_default\_fields

boolean

default:false

Return only the fields in `select`, plus id. Other default fields (created\_at, modified\_at, inputs, name, dataset\_id) are absent unless selected.

descending

boolean | null

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