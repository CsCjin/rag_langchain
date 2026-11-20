---
title: "Query single thread stats - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/threads/query-single-thread-stats
scraped_at: 2026-11-15T03:42:04.622079
word_count: 469
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

#### Path Parameters

thread\_id

string

required

Thread ID

#### Query Parameters

filter

string

`filter` narrows which of the thread's traces are aggregated, using a LangSmith filter expression. For example: lt(start\_time, "2025-01-01T00:00:00Z") or eq(trace\_id, "0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328").
See <https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language> for syntax.

selects

enum<string>[]

required

`selects` lists which aggregate stats to compute and return (repeatable query parameter). At least one value is required. Accepts any value of `SingleThreadStatsSelectField`.

Available options:

`TURNS`,

`FIRST_START_TIME`,

`LAST_START_TIME`,

`LAST_END_TIME`,

`LATENCY_P50`,

`LATENCY_P99`,

`PROMPT_TOKENS`,

`PROMPT_COST`,

`COMPLETION_TOKENS`,

`COMPLETION_COST`,

`TOTAL_TOKENS`,

`TOTAL_COST`,

`PROMPT_TOKEN_DETAILS`,

`COMPLETION_TOKEN_DETAILS`,

`PROMPT_COST_DETAILS`,

`COMPLETION_COST_DETAILS`,

`FEEDBACK_STATS`

session\_id

string<uuid>

required

`session_id` is the tracing project (session) UUID (required).

#### Response

200

application/json

aggregate stats for the thread

completion\_cost

number

`completion_cost` is the sum of per-trace completion costs across the thread, in USD. Populated when `COMPLETION_COST` is selected.

completion\_cost\_details

object

`completion_cost_details` is the per-sub-category sum of completion cost details across the thread. Populated when `COMPLETION_COST_DETAILS` is selected.

Show child attributes

completion\_token\_details

object

`completion_token_details` is the per-sub-category sum of completion token details across the thread. Populated when `COMPLETION_TOKEN_DETAILS` is selected.

Show child attributes

completion\_tokens

integer

`completion_tokens` is the sum of per-trace completion token counts across the thread. Populated when `COMPLETION_TOKENS` is selected.

feedback\_stats

object

`feedback_stats` aggregates run-level feedback across the thread's traces, keyed by feedback key. Populated when `FEEDBACK_STATS` is selected.

Show child attributes

first\_start\_time

string<date-time>

`first_start_time` is the earliest trace start time in the thread (RFC3339). Populated when `FIRST_START_TIME` is selected.

last\_end\_time

string<date-time>

`last_end_time` is the latest trace end time in the thread (RFC3339). Populated when `LAST_END_TIME` is selected.

last\_start\_time

string<date-time>

`last_start_time` is the latest trace start time in the thread (RFC3339). Populated when `LAST_START_TIME` is selected.

latency\_p50\_seconds

number

`latency_p50_seconds` is the approximate p50 of trace latency across the thread, in seconds. Populated when `LATENCY_P50` is selected.

latency\_p99\_seconds

number

`latency_p99_seconds` is the approximate p99 of trace latency across the thread, in seconds. Populated when `LATENCY_P99` is selected.

prompt\_cost

number

`prompt_cost` is the sum of per-trace prompt costs across the thread, in USD. Populated when `PROMPT_COST` is selected.

prompt\_cost\_details

object

`prompt_cost_details` is the per-sub-category sum of prompt cost details across the thread. Populated when `PROMPT_COST_DETAILS` is selected.

Show child attributes

prompt\_token\_details

object

`prompt_token_details` is the per-sub-category sum of prompt token details across the thread. Populated when `PROMPT_TOKEN_DETAILS` is selected.

Show child attributes

prompt\_tokens

integer

`prompt_tokens` is the sum of per-trace prompt token counts across the thread. Populated when `PROMPT_TOKENS` is selected.

total\_cost

number

`total_cost` is the sum of per-trace total costs across the thread, in USD. Populated when `TOTAL_COST` is selected.

total\_tokens

integer

`total_tokens` is the sum of per-trace total token counts across the thread. Populated when `TOTAL_TOKENS` is selected.

turns

integer

`turns` is the number of distinct traces (turns) in the thread. Populated when `TURNS` is selected.