---
title: "Query thread stats - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/threads/query-thread-stats
scraped_at: 2026-11-15T03:42:04.932043
word_count: 533
---

#### Authorizations

API Key & Tenant IDBearer Auth & Tenant IDAPI Key & Tenant IDBearer Auth & Tenant ID

X-API-Key

string

header

required

X-Tenant-Id

string

header

required

#### Body

application/json

project\_id

string<uuid>

required

`project_id` is the tracing project UUID.

Example:

`"0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328"`

select

enum<string>[]

required

`select` lists the aggregate statistics to compute and return. At least one value is required.

Minimum array length: `1`

Available options:

`THREAD_COUNT`,

`TRACE_COUNT`,

`TOTAL_TOKENS`,

`TOTAL_COST`,

`ERROR_RATE`,

`STREAMING_RATE`,

`LATENCY_P50`,

`LATENCY_P99`,

`MEDIAN_TOKENS`,

`FIRST_TOKEN_P50`,

`FIRST_TOKEN_P99`,

`PROMPT_TOKENS`,

`COMPLETION_TOKENS`,

`PROMPT_COST`,

`COMPLETION_COST`,

`PROMPT_TOKEN_DETAILS`,

`COMPLETION_TOKEN_DETAILS`,

`PROMPT_COST_DETAILS`,

`COMPLETION_COST_DETAILS`,

`THREAD_FEEDBACK_STATS`

Example:

```
[
  "THREAD_COUNT",
  "TRACE_COUNT",
  "TOTAL_TOKENS",
  "TOTAL_COST"
]
```

filter

string

`filter` is a deprecated, unscoped LangSmith filter expression evaluated
against trace root runs. Kept for compatibility with deployments that
serve this endpoint via the legacy ClickHouse backend (no SmithDB query
service configured); prefer `trace_filter`, `tree_filter`, or
`thread_filter` otherwise, since those require SmithDB.

Example:

`"eq(status, \"error\")"`

max\_start\_time

string<date-time>

`max_start_time` is the exclusive upper bound on thread activity (RFC3339 date-time). Defaults to now (UTC) when omitted.

min\_start\_time

string<date-time>

`min_start_time` is the inclusive lower bound on thread activity (RFC3339 date-time). Defaults to 1 day before now (UTC) when omitted.

thread\_filter

string

`thread_filter` narrows eligible threads using a LangSmith filter expression evaluated against the complete thread summary.

Example:

`"gte(turn_count, 3)"`

trace\_filter

string

`trace_filter` narrows eligible threads to those containing a trace whose root run matches this LangSmith filter expression.

Example:

`"eq(status, \"error\")"`

tree\_filter

string

`tree_filter` narrows eligible threads to those containing a matching run anywhere in a trace tree.

Example:

`"has(tags, \"production\")"`

#### Response

200

application/json

aggregate thread statistics

completion\_cost

number

`completion_cost` is the completion cost across matching traces in USD.

completion\_cost\_details

object

`completion_cost_details` contains completion-cost totals by category.

Show child attributes

completion\_token\_details

object

`completion_token_details` contains completion-token totals by category.

Show child attributes

completion\_tokens

integer

`completion_tokens` is the sum of completion tokens across matching traces.

error\_rate

number

`error_rate` is the fraction of matching traces that contain an error.

first\_token\_p50\_seconds

number

`first_token_p50_seconds` is the approximate median time to first token in seconds. Populated when `FIRST_TOKEN_P50` is selected.

first\_token\_p99\_seconds

number

`first_token_p99_seconds` is the approximate p99 time to first token in seconds. Populated when `FIRST_TOKEN_P99` is selected.

latency\_p50\_seconds

number

`latency_p50_seconds` is the approximate median trace latency in seconds. Populated when `LATENCY_P50` is selected.

latency\_p99\_seconds

number

`latency_p99_seconds` is the approximate p99 trace latency in seconds. Populated when `LATENCY_P99` is selected.

median\_tokens

integer

`median_tokens` is the approximate median of total tokens across matching traces. Populated when `MEDIAN_TOKENS` is selected.

prompt\_cost

number

`prompt_cost` is the prompt cost across matching traces in USD.

prompt\_cost\_details

object

`prompt_cost_details` contains prompt-cost totals by category.

Show child attributes

prompt\_token\_details

object

`prompt_token_details` contains prompt-token totals by category.

Show child attributes

prompt\_tokens

integer

`prompt_tokens` is the sum of prompt tokens across matching traces.

streaming\_rate

number

`streaming_rate` is the fraction of completed matching traces that streamed tokens.

thread\_count

integer

`thread_count` is the number of distinct threads matching the query. Populated when `THREAD_COUNT` is selected.

thread\_feedback\_stats

object

`thread_feedback_stats` contains aggregate thread-level feedback statistics keyed by feedback key. Populated when `THREAD_FEEDBACK_STATS` is selected.

Show child attributes

total\_cost

number

`total_cost` is the total cost across matching traces in USD.

total\_tokens

integer

`total_tokens` is the sum of all tokens across matching traces.

trace\_count

integer

`trace_count` is the number of traces in the matching threads. Populated when `TRACE_COUNT` is selected.