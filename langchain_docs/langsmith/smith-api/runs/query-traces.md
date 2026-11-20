---
title: "Query traces - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/runs/query-traces
scraped_at: 2026-11-15T03:41:44.511002
word_count: 531
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

`ai_search` is a plain-language criterion evaluated against the messages from the agent trajectory scoped to the trace.
AND-ed with the ordinary filters. Requires semantic filtering enabled for the deployment.
Must contain nonempty text of at most 2000 UTF-8 bytes.

Required string length: `1 - 2000`

Example:

`"A run that contains a billing dispute"`

cursor

string

`cursor` is the opaque string returned in a previous response's `next_cursor`.

max\_feedback\_modified\_at

string<date-time>

`max_feedback_modified_at` is the exclusive upper bound (RFC3339) on feedback `modified_at`, applied to the feedback conditions in `trace_filter` or `tree_filter` (for example eq(feedback\_key, "correctness")).
Requires at least one feedback condition. Root runs must still fall within the `start_time` window.

Example:

`"2024-12-31T23:59:59Z"`

max\_start\_time

string<date-time>

`max_start_time` is the exclusive upper bound for the root-run start time scan (RFC3339). Defaults to the request time when omitted.

Example:

`"2024-12-31T23:59:59Z"`

min\_feedback\_modified\_at

string<date-time>

`min_feedback_modified_at` is the inclusive lower bound (RFC3339) on feedback `modified_at`, applied to the feedback conditions in `trace_filter` or `tree_filter` (for example eq(feedback\_key, "correctness")).
Requires at least one feedback condition. Root runs must still fall within the `start_time` window.

Example:

`"2024-01-01T00:00:00Z"`

min\_start\_time

string<date-time>

`min_start_time` is the inclusive lower bound for the root-run start time scan (RFC3339). Defaults to 24 hours before the request when omitted.

Example:

`"2024-01-01T00:00:00Z"`

page\_size

integer

default:20

`page_size` is the maximum number of traces to return per page. Defaults to 20; must be between 1 and 100 when set.

Required range: `1 <= x <= 100`

Example:

`20`

project\_id

string<uuid>

`project_id` is the UUID of the tracing project that owns the traces. Required.

Example:

`"018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"`

selects

enum<string>[]

`selects` lists which properties to include on each returned trace. Properties listed here are routed to the appropriate sub-object on each item: `total_tokens`, `total_cost`, and `first_token_time` appear under `trace_aggregates`; everything else appears under `root_run`. If omitted, only `id` is returned on `root_run`.

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
  "START_TIME",
  "STATUS",
  "TOTAL_TOKENS",
  "TOTAL_COST",
  "FIRST_TOKEN_TIME"
]
```

trace\_filter

string

`trace_filter` narrows results to traces whose root run matches this LangSmith filter expression. This filter targets root runs only — `is_root = true` is implied.
See <https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language> for syntax.

Example:

`"eq(status, \"error\")"`

trace\_ids

string<uuid>[]

`trace_ids` is an optional fast-path restriction to a known set of trace UUIDs. Equivalent in result to including each UUID in a `trace_filter`, but more efficient at scale.

tree\_filter

string

`tree_filter` narrows results to traces containing at least one run anywhere in the run tree (root or descendant) that matches this LangSmith filter expression.

Example:

`"has(tags, \"production\")"`

#### Response

200

application/json

OK

items

object[]

`items` is the page of traces.

Show child attributes

next\_cursor

string

`next_cursor` is the opaque cursor for the next page. Null on the final page.