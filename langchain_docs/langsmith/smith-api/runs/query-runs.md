---
title: "Query runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/runs/query-runs
scraped_at: 2026-11-15T03:41:44.385022
word_count: 788
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

application/json, or text/event-stream (required when ai\_search is set)

Content-Type

string

application/json (required for JSON body)

#### Body

application/json

ai\_search

string

`ai_search` is a plain-language criterion evaluated against the messages from the agent trajectory scoped to the run.
AND-ed with the ordinary filters. Requires semantic filtering enabled for the deployment.
Must contain nonempty text of at most 2000 UTF-8 bytes. Not supported on public dataset queries.

Required string length: `1 - 2000`

Example:

`"The customer was charged twice"`

cursor

string

`cursor` is the opaque string from a previous response's `next_cursor`. Treat it as opaque and pass it back unmodified.

Example:

`"eyJ2IjoxLCJhIjoicnVucy5xdWVyeSIsImsiOiJwYXNzIiwiYiI6InNkYiIsInQiOiJsdChjdXJzb3IsICcyMDI1LTEyLTEyIDE5OjAzOjI4LjQ4MTI1NTAxOWIxM2YyJykifQ"`

filter

string

`filter` narrows results to runs matching this LangSmith filter expression, evaluated against each individual run.
For example: and(eq(run\_type, "llm"), gt(latency, 5)) or eq(status, "error").
See <https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language> for syntax.

Example:

`"and(eq(run_type, \"llm\"), gt(latency, 5))"`

has\_error

boolean

`has_error` filters to runs that errored (true) or completed without error (false).

Example:

`false`

ids

string<uuid>[]

`ids` optionally limits the request to these run UUIDs.

Example:

```
[
  "018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
  "f47ac10b-58cc-4372-a567-0e02b2c3d479"
]
```

include\_subtree\_usage

boolean

default:false

`include_subtree_usage` enriches selected token and cost fields on root and intermediate runs with subtree totals, and selected `first_token_time` with the earliest observed subtree timestamp.
Descendants contribute regardless of this request's filters or time bounds. Runs without observed descendants retain their original values. Defaults to false.

is\_root

boolean

`is_root` returns only root runs (true) or only non-root runs (false).

Example:

`true`

max\_feedback\_modified\_at

string<date-time>

`max_feedback_modified_at` is the exclusive upper bound (RFC3339) on feedback `modified_at`, applied to the feedback conditions in `filter`, `trace_filter`, or `tree_filter` (for example eq(feedback\_key, "correctness")).
Requires at least one feedback condition. Runs must still fall within the `start_time` window.

Example:

`"2024-12-31T23:59:59Z"`

max\_start\_time

string<date-time>

`max_start_time` is the upper bound for run `start_time` (RFC3339). Defaults to now.

Example:

`"2024-12-31T23:59:59Z"`

min\_feedback\_modified\_at

string<date-time>

`min_feedback_modified_at` is the inclusive lower bound (RFC3339) on feedback `modified_at`, applied to the feedback conditions in `filter`, `trace_filter`, or `tree_filter` (for example eq(feedback\_key, "correctness")).
Requires at least one feedback condition. Runs must still fall within the `start_time` window.

Example:

`"2024-01-01T00:00:00Z"`

min\_start\_time

string<date-time>

`min_start_time` is the lower bound for run `start_time` (RFC3339). Defaults to 1 day ago.

Example:

`"2024-01-01T00:00:00Z"`

page\_size

integer

default:100

`page_size` is the maximum number of runs to return in this response. Defaults to 100 when omitted; must be between 1 and 1000 inclusive when set.

Required range: `1 <= x <= 1000`

Example:

`100`

project\_ids

string<uuid>[]

`project_ids` lists tracing project UUIDs to query.
Required unless `reference_dataset_id` is set. Mutually exclusive with `reference_dataset_id` — set exactly one of them.

Example:

```
[
  "018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
  "0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328"
]
```

reference\_dataset\_id

string<uuid>

`reference_dataset_id` resolves session IDs server-side from the dataset.
Required unless `project_ids` is set. Mutually exclusive with `project_ids` — set exactly one of them.
When provided and `min_start_time` is omitted, the server derives it from the earliest session creation date.

Example:

`"018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"`

reference\_examples

string<uuid>[]

`reference_examples` optionally limits to runs linked to these dataset example UUIDs.

Example:

```
[
  "b2c3d4e5-f6a7-4b5c-9d0e-1f2a3b4c5d6e",
  "c3d4e5f6-a7b8-4c5d-0e1f-2a3b4c5d6e7f"
]
```

run\_type

enum<string>

`run_type`, when set, restricts results to runs whose `run_type` equals this value.

Available options:

`TOOL`,

`CHAIN`,

`LLM`,

`RETRIEVER`,

`EMBEDDING`,

`PROMPT`,

`PARSER`

Example:

`"LLM"`

selects

enum<string>[]

`selects` lists which properties to include on each returned run. If omitted, only `id` is returned. Properties not listed are omitted from each run object.

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

Example:

```
[
  "ID",
  "NAME",
  "PROJECT_ID",
  "START_TIME",
  "RUN_TYPE",
  "STATUS"
]
```

trace\_filter

string

`trace_filter` narrows results to runs whose root trace matches this LangSmith filter expression.
Use this to filter by properties of the trace's root run — for example eq(status, "success") to include only traces that completed without error.
See <https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language> for syntax.

Example:

`"eq(status, \"success\")"`

trace\_id

string<uuid>

`trace_id` optionally limits results to runs belonging to this trace UUID.

Example:

`"f47ac10b-58cc-4372-a567-0e02b2c3d479"`

tree\_filter

string

`tree_filter` narrows results to runs that belong to a trace containing at least one run matching this LangSmith filter expression anywhere in the run tree (not just the root).
Use this to find runs inside traces that involved a specific tool, tag, or model — for example has(tags, "production") or eq(name, "my\_tool").
See <https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language> for syntax.

Example:

`"has(tags, \"production\")"`

#### Response

200

application/json

OK

items

object[]

`items` is the page of runs, sorted by `start_time` descending.

Show child attributes

next\_cursor

string

`next_cursor` is the opaque cursor to pass as `cursor` on the next request. Null on the final page.

Example:

`"eyJ2IjoxLCJhIjoicnVucy5xdWVyeSIsImsiOiJwYXNzIiwiYiI6InNkYiIsInQiOiJsdChjdXJzb3IsICcyMDI1LTEyLTEyIDE5OjAzOjI4LjQ4MTI1NTAxOWIxM2YyJykifQ"`