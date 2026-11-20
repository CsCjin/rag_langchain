---
title: "Validate runs query - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/validate-runs-query
scraped_at: 2026-11-15T03:41:42.394235
word_count: 286
---

#### Body

application/json

Query params for runs query endpoint.

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

session

string<uuid>[] | null

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

cursor

string | null

limit

integer

default:100

Maximum number of runs to return. Not applied when trace is set — all runs in the trace are returned in a single response.

Required range: `1 <= x <= 100`

select

enum<string>[]

Enum for available run columns.

Available options:

`id`,

`name`,

`run_type`,

`start_time`,

`end_time`,

`status`,

`error`,

`extra`,

`events`,

`inputs`,

`inputs_preview`,

`inputs_s3_urls`,

`inputs_or_signed_url`,

`outputs`,

`outputs_preview`,

`outputs_s3_urls`,

`outputs_or_signed_url`,

`s3_urls`,

`error_or_signed_url`,

`events_or_signed_url`,

`extra_or_signed_url`,

`serialized_or_signed_url`,

`parent_run_id`,

`manifest_id`,

`manifest_s3_id`,

`manifest`,

`session_id`,

`serialized`,

`reference_example_id`,

`reference_dataset_id`,

`total_tokens`,

`prompt_tokens`,

`prompt_token_details`,

`completion_tokens`,

`completion_token_details`,

`total_cost`,

`prompt_cost`,

`prompt_cost_details`,

`completion_cost`,

`completion_cost_details`,

`price_model_id`,

`first_token_time`,

`trace_id`,

`dotted_order`,

`last_queued_at`,

`feedback_stats`,

`child_run_ids`,

`parent_run_ids`,

`tags`,

`in_dataset`,

`app_path`,

`share_token`,

`trace_tier`,

`trace_first_received_at`,

`ttl_seconds`,

`trace_upgrade`,

`thread_id`,

`trace_min_max_start_time`,

`messages`,

`inserted_at`

order

enum<string>

default:desc

Enum for run start date order.

Available options:

`asc`,

`desc`

skip\_prev\_cursor

boolean

default:false

#### Response

200

application/json

Successful Response

Response for POST /runs/query/validate.

valid

boolean

required

errors

RunsQueryValidationError · object[]

Show child attributes