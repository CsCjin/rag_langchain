---
title: "Get a single run - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/runs/get-a-single-run
scraped_at: 2026-11-15T03:41:43.312072
word_count: 1001
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

run\_id

string<uuid>

required

Run UUID

#### Query Parameters

project\_id

string<uuid>

required

`project_id` is the UUID of the tracing project that owns the run.

selects

enum<string>[]

`selects` lists which properties to include on the returned run (repeatable query parameter). Accepts any value of the `RunSelectField` enum. If omitted, only `id` is returned.

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

start\_time

string<date-time>

`start_time` is the run's `start_time` (RFC3339 date-time). Providing it speeds up retrieval.

#### Response

200

application/json

OK

app\_path

string

`app_path` identifies the application code location that produced this run, if recorded.

Example:

`"/app/chains/chat.py:invoke"`

attachments

object

`attachments` maps each attachment file name to a pre-signed HTTPS download URL.

Show child attributes

Example:

```
{
  "{\"output.png\"": "\"https://storage.example.com/bucket/key?X-Amz-Signature=abc\"}"
}
```

completion\_cost

number

`completion_cost` is estimated USD cost for the completion.

Example:

`0.0003`

completion\_cost\_details

object

`completion_cost_details` is the per-category USD breakdown of `completion_cost`. Categories mirror `completion_token_details`. Returned only when the `COMPLETION_COST_DETAILS` field is requested.

Show child attributes

completion\_token\_details

object

`completion_token_details` is the per-category breakdown of `completion_tokens`. Category names are model-specific (for example `reasoning`, `audio`). Returned only when the `COMPLETION_TOKEN_DETAILS` field is requested.

Show child attributes

completion\_tokens

integer

`completion_tokens` is the completion-side token count.

Example:

`150`

dotted\_order

string

`dotted_order` is the hierarchical ordering key for trace trees.

Example:

`"20240115T103000000000Z018e4c7ea9fb7ef0a5b66ea3a82e9327."`

end\_time

string<date-time>

`end_time` is when the run ended (RFC3339 date-time). JSON null if the run has not finished yet.

Example:

`"2024-01-15T10:30:01.500Z"`

error

string

`error` is the error message when `status` indicates failure.

Example:

`"context deadline exceeded"`

error\_preview

string

`error_preview` is a truncated plain-text error snippet.

events

object[]

`events` is the ordered list of run events (for example streaming tokens).

Show child attributes

extra

object

`extra` is additional runtime JSON attached to the run.

feedback\_stats

object

`feedback_stats` aggregates feedback scores keyed by feedback key.

Show child attributes

first\_token\_time

string<date-time>

`first_token_time` is when the first output token was produced (RFC3339 date-time), when recorded for streamed runs.

Example:

`"2024-01-15T10:30:00.312Z"`

id

string<uuid>

`id` is this run's UUID.

Example:

`"018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"`

inputs

object

`inputs` is the run input payload (arbitrary JSON object).

inputs\_preview

string

`inputs_preview` is a truncated plain-text preview of inputs.

is\_in\_dataset

boolean

`is_in_dataset` is true when this run is linked to a dataset example.

Example:

`true`

is\_root

boolean

`is_root` is true when this run has no parent (it is the trace root).

Example:

`true`

last\_queued\_at

string<date-time>

`last_queued_at` is the most recent time this run was added to an annotation queue.

Example:

`"2024-01-15T10:31:00Z"`

latency\_seconds

number

`latency_seconds` is wall-clock duration from start to end in seconds.

Example:

`1.523`

ls\_user\_id

string<uuid>

`ls_user_id` identifies the LangSmith user whose credential traced the run. It is absent for runs traced with a service-account API key, which has no associated user.

Example:

`"f6a7b8c9-d0e1-4f2a-3b4c-5d6e7f8a9b0c"`

manifest

object

`manifest` is the serialized configuration of the traced component (for example the model parameters, prompt template, or pipeline definition), when recorded.

metadata

object

`metadata` is arbitrary user-defined JSON metadata.

name

string

`name` is a human-readable label for the run (for example the model name, function name, or step name chosen when the run was traced).

Example:

`"ChatOpenAI"`

outputs

object

`outputs` is the run output payload (arbitrary JSON object).

outputs\_preview

string

`outputs_preview` is a truncated plain-text preview of outputs.

parent\_run\_ids

string<uuid>[]

`parent_run_ids` lists ancestor run UUIDs from the trace root down to the direct parent.

Example:

```
[
  "018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327",
  "a1b2c3d4-e5f6-4a5b-8c9d-0e1f2a3b4c5d"
]
```

price\_model\_id

string<uuid>

`price_model_id` identifies the pricing model UUID used for cost estimates, when recorded.

Example:

`"e5f6a7b8-c9d0-4e1f-2a3b-4c5d6e7f8a9b"`

project\_id

string<uuid>

`project_id` is the tracing project UUID this run was logged to.

Example:

`"018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"`

prompt\_cost

number

`prompt_cost` is estimated USD cost for the prompt.

Example:

`0.0002`

prompt\_cost\_details

object

`prompt_cost_details` is the per-category USD breakdown of `prompt_cost`. Categories mirror `prompt_token_details`. Returned only when the `PROMPT_COST_DETAILS` field is requested.

Show child attributes

prompt\_token\_details

object

`prompt_token_details` is the per-category breakdown of `prompt_tokens`. Category names are model-specific (for example `cache_read`, `cache_write`). Returned only when the `PROMPT_TOKEN_DETAILS` field is requested.

Show child attributes

prompt\_tokens

integer

`prompt_tokens` is the prompt-side token count.

Example:

`200`

query\_metadata

object | null

`query_metadata` describes this query result, including `sem_filter_score` when a semantic filter is used. Returned automatically by run queries, or null when unavailable.

reference\_dataset\_id

string<uuid>

`reference_dataset_id` is the dataset UUID for the reference example, if any.

Example:

`"c3d4e5f6-a7b8-4c5d-0e1f-2a3b4c5d6e7f"`

reference\_example\_id

string<uuid>

`reference_example_id` is the dataset example UUID this run was compared against, if any.

Example:

`"b2c3d4e5-f6a7-4b5c-9d0e-1f2a3b4c5d6e"`

run\_type

enum<string>

`run_type` identifies what kind of operation this run represents (for example an LLM call, a tool invocation, or a chain step). See the `RunType` enum for allowed values.

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

share\_url

string

`share_url` is the fully-qualified URL of this run's public view, rooted at the deployment's LangSmith app origin (for example `https://smith.langchain.com/public/4f7a1b2c-8d9e-4a0b-9c1d-2e3f4a5b6c7d/r`). It is returned only when `SHARE_URL` is included in `selects`, and only when the run has been explicitly shared; the URL remains stable until the run is unshared. Anyone with this URL can view the run anonymously, so treat it as a secret and do not log it.

Example:

`"https://smith.langchain.com/public/4f7a1b2c-8d9e-4a0b-9c1d-2e3f4a5b6c7d/r"`

start\_time

string<date-time>

`start_time` is when the run started (RFC3339 date-time).

Example:

`"2024-01-15T10:30:00.000Z"`

status

enum<string>

`status` is the completion status of the run.

Available options:

`SUCCESS`,

`ERROR`,

`PENDING`

Example:

`"SUCCESS"`

tags

string[]

`tags` lists user-defined tags on this run.

Example:

```
["production", "gpt-4"]
```

thread\_evaluation\_time

string<date-time>

`thread_evaluation_time` is thread-level evaluation timing (RFC3339 date-time), when recorded.

thread\_id

string<uuid>

`thread_id` is the conversation thread UUID this run belongs to, if any.

Example:

`"d4e5f6a7-b8c9-4d5e-1f2a-3b4c5d6e7f8a"`

total\_cost

number

`total_cost` is total estimated USD cost (prompt plus completion).

Example:

`0.000525`

total\_tokens

integer

`total_tokens` is prompt plus completion tokens.

Example:

`350`

trace\_id

string<uuid>

`trace_id` is the root trace UUID; for a root run it matches `id`.

Example:

`"018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"`