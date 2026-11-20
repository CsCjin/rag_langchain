---
title: "Query thread traces - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/threads/query-thread-traces
scraped_at: 2026-11-15T03:42:05.064358
word_count: 296
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

cursor

string

`cursor` is the opaque string from a previous response's `next_cursor`. Omit on the first request; pass the returned cursor to fetch the next page.

filter

string

`filter` narrows which traces are returned for this thread, using a LangSmith filter expression evaluated against each root trace run.
For example: eq(status, "success") or has(tags, "production").
See <https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language> for syntax.

page\_size

integer

default:20

`page_size` is the maximum number of traces to return in this response. Defaults to 20 when omitted; must be between 1 and 100 inclusive when set.

Required range: `1 <= x <= 100`

project\_id

string<uuid>

required

`project_id` is the tracing project UUID (required).

selects

enum<string>[]

`selects` lists which properties to include on each returned trace (repeatable query parameter). Accepts any value of the `ThreadTraceSelectField` enum. Properties not listed are omitted from each trace object; `trace_id` is always returned.

Available options:

`THREAD_ID`,

`TRACE_ID`,

`OP`,

`PROMPT_TOKENS`,

`COMPLETION_TOKENS`,

`TOTAL_TOKENS`,

`START_TIME`,

`END_TIME`,

`LATENCY`,

`FIRST_TOKEN_TIME`,

`INPUTS_PREVIEW`,

`OUTPUTS_PREVIEW`,

`INPUTS`,

`OUTPUTS`,

`ERROR`,

`PROMPT_COST`,

`COMPLETION_COST`,

`TOTAL_COST`,

`PROMPT_TOKEN_DETAILS`,

`COMPLETION_TOKEN_DETAILS`,

`PROMPT_COST_DETAILS`,

`COMPLETION_COST_DETAILS`,

`NAME`,

`ERROR_PREVIEW`,

`TURN_NUMBER`

trace\_filter

string

`trace_filter` narrows traces by applying a LangSmith filter expression to each trace's root run.

tree\_filter

string

`tree_filter` narrows traces to those containing at least one run that matches the LangSmith filter expression.

#### Response

200

application/json

items and pagination

items

object[]

`items` is the page of root traces in this thread. Which properties are populated on each trace depends on the `selects` query parameter.

Show child attributes

next\_cursor

string

`next_cursor` is the opaque cursor to pass as `cursor` on the next request. Null on the final page.

Example:

`"eyJydW5zX2N1cnNvciI6Imx0KGN1cnNvciwiLi4uIikifQ=="`