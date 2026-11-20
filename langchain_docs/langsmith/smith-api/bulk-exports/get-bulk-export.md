---
title: "Get bulk export - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/bulk-exports/get-bulk-export
scraped_at: 2026-11-15T03:40:38.984693
word_count: 155
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

bulk\_export\_id

string<uuid>

required

#### Response

200

application/json

Successful Response

bulk\_export\_destination\_id

string<uuid>

required

start\_time

string<date-time>

required

id

string<uuid>

required

tenant\_id

string<uuid>

required

status

enum<string>

required

Available options:

`Cancelled`,

`Completed`,

`Created`,

`IntervalScheduled`,

`Failed`,

`TimedOut`,

`Running`

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

finished\_at

string<date-time> | null

required

session\_id

string<uuid> | null

all\_experiments

boolean

default:false

end\_time

string<date-time> | null

filter

string | null

LangSmith filter expression that selects the runs to export. Accepts the function-style syntax, for example eq(run\_type, "llm"), and, on LangSmith Cloud and self-hosted versions that support it, the v2 syntax, for example run\_type:llm.
See <https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language> for syntax.

format

enum<string>

default:Parquet

Available options:

`Parquet`

format\_version

enum<string>

default:v1

Enum for bulk export format versions.

Available options:

`v1`,

`v2_beta`

compression

enum<string>

default:zstandard

Available options:

`none`,

`gzip`,

`snappy`,

`zstandard`

is\_rollup\_disabled

boolean

default:false

interval\_hours

integer | null

export\_fields

string[] | null

source\_bulk\_export\_id

string<uuid> | null