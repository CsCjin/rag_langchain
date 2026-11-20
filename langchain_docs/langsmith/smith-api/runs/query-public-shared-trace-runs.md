---
title: "Query public shared trace runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/runs/query-public-shared-trace-runs
scraped_at: 2026-11-15T03:41:44.172110
word_count: 112
---

#### Headers

Accept

string

application/json or text/event-stream

Content-Type

string

application/json

#### Path Parameters

share\_token

string<uuid>

required

Share token UUID

#### Body

application/json

selects

enum<string>[]

`selects` lists which public run properties to include on each returned run.

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

`INPUTS_PREVIEW`,

`OUTPUTS_PREVIEW`,

`PARENT_RUN_ID`,

`PARENT_RUN_IDS`,

`PROJECT_ID`,

`TRACE_ID`,

`THREAD_ID`,

`DOTTED_ORDER`,

`IS_ROOT`,

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

`THREAD_EVALUATION_TIME`,

`FEEDBACK_STATS`

Example:

```
[
  "ID",
  "NAME",
  "PROJECT_ID",
  "START_TIME",
  "RUN_TYPE",
  "STATUS",
  "INPUTS_PREVIEW",
  "OUTPUTS_PREVIEW",
  "METADATA"
]
```

#### Response

200

application/json

OK

items

object[]

`items` lists runs in the trace for the requested time window, in `start_time` order.

Show child attributes