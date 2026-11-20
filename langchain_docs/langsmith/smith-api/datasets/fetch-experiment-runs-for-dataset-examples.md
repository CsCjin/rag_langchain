---
title: "Fetch experiment runs for dataset examples - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/fetch-experiment-runs-for-dataset-examples
scraped_at: 2026-11-15T03:40:49.516878
word_count: 212
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

dataset\_id

string

required

Dataset ID

#### Body

application/json

comparative\_experiment\_id

string

`comparative_experiment_id` scopes pairwise-annotation feedback (optional).

cursor

string

`cursor` is the opaque string from a previous response's `next_cursor`. Absent for the first page.

example\_ids

string[]

`example_ids` optionally restricts the page to these dataset example UUIDs (max 1000).

experiment\_ids

string[]

`experiment_ids` lists the experiment (tracing session) UUIDs to query. Required, non-empty.

filters

object

`filters` maps a project (session) UUID string to a list of filter expressions (optional).

Show child attributes

page\_size

integer

`page_size` is the maximum number of examples to return. Defaults to 20, max 100.

selects

enum<string>[]

`selects` lists which run properties to include. Omitted => only `id`. Tokens mirror /v2/runs/query.

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

sort

object

`sort` controls feedback-score sorting (single project only).

Show child attributes

#### Response

200

application/json

OK

items

object[]

Show child attributes

next\_cursor

string