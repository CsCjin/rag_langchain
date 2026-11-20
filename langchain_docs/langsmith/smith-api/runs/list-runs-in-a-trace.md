---
title: "List runs in a trace - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/runs/list-runs-in-a-trace
scraped_at: 2026-11-15T03:41:43.946703
word_count: 232
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

#### Headers

Accept

string

application/json

#### Path Parameters

trace\_id

string<uuid>

required

Trace UUID

#### Query Parameters

filter

string

`filter` narrows which runs within this trace are returned, using a LangSmith filter expression evaluated against each run. For example: `eq(run_type, "llm")` for LLM runs only, or `eq(status, "error")` for failed runs.
See <https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language> for syntax.

max\_start\_time

string<date-time>

`max_start_time` is the optional inclusive upper bound for run `start_time` (RFC3339 date-time). Required together with `min_start_time`.

min\_start\_time

string<date-time>

`min_start_time` is the optional inclusive lower bound for run `start_time` (RFC3339 date-time). Required together with `max_start_time`.

project\_id

string<uuid>

required

`project_id` is the UUID of the tracing project that owns the trace.

selects

enum<string>[]

`selects` lists which properties to include on each returned run (repeatable query parameter). Accepts any value of the `RunSelectField` enum. If omitted, only `id` is returned.

Available options:

`ID`,

`NAME`,

`RUN_TYPE`,

`STATUS`,

`START_TIME`,

`END_TIME`,

`LATENCY_SECONDS`,

`FIRST_TOKEN_TIME`,

`ERROR`,

`ERROR_PREVIEW`,

`EXTRA`,

`METADATA`,

`EVENTS`,

`INPUTS`,

`INPUTS_PREVIEW`,

`OUTPUTS`,

`OUTPUTS_PREVIEW`,

`MANIFEST`,

`PARENT_RUN_IDS`,

`PROJECT_ID`,

`TRACE_ID`,

`THREAD_ID`,

`DOTTED_ORDER`,

`IS_ROOT`,

`REFERENCE_EXAMPLE_ID`,

`REFERENCE_DATASET_ID`,

`TOTAL_TOKENS`,

`PROMPT_TOKENS`,

`COMPLETION_TOKENS`,

`TOTAL_COST`,

`PROMPT_COST`,

`COMPLETION_COST`,

`PROMPT_TOKEN_DETAILS`,

`COMPLETION_TOKEN_DETAILS`,

`PROMPT_COST_DETAILS`,

`COMPLETION_COST_DETAILS`,

`PRICE_MODEL_ID`,

`TAGS`,

`APP_PATH`,

`ATTACHMENTS`,

`THREAD_EVALUATION_TIME`,

`IS_IN_DATASET`,

`LAST_QUEUED_AT`,

`SHARE_URL`,

`FEEDBACK_STATS`,

`LS_USER_ID`

#### Response

200

application/json

OK

items

object[]

`items` lists runs in the trace for the requested time window, in `start_time` order.

Show child attributes