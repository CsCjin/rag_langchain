---
title: "Query threads - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/threads/query-threads
scraped_at: 2026-11-15T03:42:05.357149
word_count: 423
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

#### Body

application/json

ai\_search

string

`ai_search` is a plain-language criterion evaluated against the messages from the agent trajectory scoped to the thread.
AND-ed with the ordinary filters. Requires semantic filtering enabled for the deployment.
Must contain nonempty text of at most 2000 UTF-8 bytes.

Required string length: `1 - 2000`

Example:

`"A conversation about a refund request"`

cursor

string

`cursor` is the opaque string from a previous response's `next_cursor`. Omit on the first request; pass the returned cursor to fetch the next page.

filter

string

`filter` narrows which threads are returned, using a LangSmith filter expression evaluated against each thread's root run.
For example: has(tags, "production") or eq(status, "error").
See <https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language> for syntax.

max\_start\_time

string<date-time>

`max_start_time` is the exclusive upper bound on thread activity (RFC3339 date-time). Defaults to now (UTC) when omitted.

min\_start\_time

string<date-time>

`min_start_time` is the inclusive lower bound on thread activity (RFC3339 date-time). Defaults to 1 day before now (UTC) when omitted.

page\_size

integer

default:20

`page_size` is the maximum number of threads to return in this response. Defaults to 20 when omitted; must be between 1 and 100 inclusive when set. The response may contain fewer threads than `page_size` even when `next_cursor` is non-null.

Required range: `1 <= x <= 100`

Example:

`20`

project\_id

string<uuid>

`project_id` is the tracing project UUID.

Example:

`"0190a1b2-c3d4-7ef0-a5b6-6ea3a82e9328"`

thread\_filter

string

`thread_filter` narrows results using a LangSmith filter expression evaluated against each complete thread summary.
Self-hosted deployments require LangSmith v0.17 or later; unsupported deployments return 501.
See <https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language> for syntax.

Example:

`"gte(turn_count, 3)"`

trace\_filter

string

`trace_filter` narrows results to threads containing at least one trace whose root run matches this LangSmith filter expression.
Trace-level aggregate fields are evaluated using the complete trace summary.
Self-hosted deployments require LangSmith v0.17 or later; unsupported deployments return 501.
See <https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language> for syntax.

Example:

`"eq(status, \"error\")"`

tree\_filter

string

`tree_filter` narrows results to threads containing at least one trace with a matching run anywhere in its run tree.
Self-hosted deployments require LangSmith v0.17 or later; unsupported deployments return 501.
See <https://docs.langchain.com/langsmith/trace-query-syntax#filter-query-language> for syntax.

Example:

`"has(tags, \"production\")"`

#### Response

200

application/json

items and pagination

items

object[]

`items` is the page of thread summaries, sorted by the thread's most recent activity.

Show child attributes

next\_cursor

string

`next_cursor` is the opaque cursor to pass as `cursor` on the next request. Null on the final page.

Example:

`"eyJydW5zX2N1cnNvciI6Imx0KGN1cnNvciwiLi4uIikifQ=="`