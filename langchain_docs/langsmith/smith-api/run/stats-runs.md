---
title: "Stats runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/stats-runs
scraped_at: 2026-11-15T03:41:41.145916
word_count: 385
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Query params for run stats.

session

string<uuid>[]

required

Minimum array length: `1`

id

string<uuid>[] | null

trace

string<uuid> | null

Filter runs by trace ID. When set, limit and cursor-based pagination are not applied — all runs in the trace are returned in a single response.

parent\_run

string<uuid> | null

run\_type

enum<string> | null

Enum for run types.

Available options:

`tool`,

`chain`,

`llm`,

`retriever`,

`embedding`,

`prompt`,

`parser`

reference\_example

string<uuid>[] | null

execution\_order

integer | null

Required range: `1 <= x <= 1`

start\_time

string<date-time> | null

end\_time

string<date-time> | null

error

boolean | null

query

string | null

filter

string | null

trace\_filter

string | null

tree\_filter

string | null

is\_root

boolean | null

data\_source\_type

enum<string> | null

Enum for run data source types.

Available options:

`current`,

`historical`,

`lite`,

`root_lite`,

`runs_feedbacks_rmt_wide`

skip\_pagination

boolean | null

search\_filter

string | null

use\_experimental\_search

boolean

default:false

group\_by

RunStatsGroupBy · object | null

Group by param for run stats.

Show child attributes

groups

(string | null)[] | null

select

enum<string>[] | null

Metrics you can select from run stats endpoint.

Available options:

`run_count`,

`latency_p50`,

`latency_p99`,

`latency_avg`,

`first_token_p50`,

`first_token_p99`,

`total_tokens`,

`prompt_tokens`,

`completion_tokens`,

`median_tokens`,

`completion_tokens_p50`,

`prompt_tokens_p50`,

`tokens_p99`,

`completion_tokens_p99`,

`prompt_tokens_p99`,

`last_run_start_time`,

`feedback_stats`,

`thread_feedback_stats`,

`run_facets`,

`error_rate`,

`streaming_rate`,

`total_cost`,

`prompt_cost`,

`completion_cost`,

`cost_p50`,

`cost_p99`,

`session_feedback_stats`,

`all_run_stats`,

`all_token_stats`,

`group_count`,

`prompt_token_details`,

`completion_token_details`,

`prompt_cost_details`,

`completion_cost_details`

reference\_dataset\_id

string<uuid> | null

include\_details

boolean

default:false

#### Response

200

application/json

Successful Response

* RunStats
* Response Stats Runs Api V1 Runs Stats Post

run\_count

integer | null

latency\_p50

number | null

latency\_p99

number | null

first\_token\_p50

number | null

first\_token\_p99

number | null

total\_tokens

integer | null

prompt\_tokens

integer | null

completion\_tokens

integer | null

median\_tokens

integer | null

completion\_tokens\_p50

integer | null

prompt\_tokens\_p50

integer | null

tokens\_p99

integer | null

completion\_tokens\_p99

integer | null

prompt\_tokens\_p99

integer | null

last\_run\_start\_time

string<date-time> | null

feedback\_stats

Feedback Stats · object | null

run\_facets

Run Facets · object[] | null

error\_rate

number | null

streaming\_rate

number | null

total\_cost

number | null

prompt\_cost

number | null

completion\_cost

number | null

cost\_p50

number | null

cost\_p99

number | null

prompt\_token\_details

Prompt Token Details · object | null

completion\_token\_details

Completion Token Details · object | null

prompt\_cost\_details

Prompt Cost Details · object | null

completion\_cost\_details

Completion Cost Details · object | null