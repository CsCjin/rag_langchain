---
title: "List Runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/list-runs
scraped_at: 2026-11-15T03:38:16.909521
word_count: 242
---

#### Path Parameters

thread\_id

string<uuid>

required

The ID of the thread.

#### Query Parameters

limit

integer

default:10

offset

integer

default:0

status

enum<string>

Available options:

`pending`,

`running`,

`error`,

`success`,

`timeout`,

`interrupted`

select

enum<string>[]

Specify which fields to return. If not provided, all fields are returned.

Available options:

`run_id`,

`thread_id`,

`assistant_id`,

`created_at`,

`updated_at`,

`status`,

`metadata`,

`kwargs`,

`multitask_strategy`,

`langsmith_session_name`,

`cancel_reason`,

`priority`

#### Response

200

application/json

Success

run\_id

string<uuid>

required

The ID of the run.

thread\_id

string<uuid>

required

The ID of the thread.

assistant\_id

string<uuid>

required

The assistant that was used for this run.

created\_at

string<date-time>

required

The time the run was created.

updated\_at

string<date-time>

required

The last time the run was updated.

status

enum<string>

required

The status of the run. One of 'pending', 'running', 'error', 'success', 'timeout', 'interrupted'.

Available options:

`pending`,

`running`,

`error`,

`success`,

`timeout`,

`interrupted`

metadata

Metadata · object

required

The run metadata.

kwargs

Kwargs · object

required

multitask\_strategy

enum<string>

required

Strategy to handle concurrent runs on the same thread.

Available options:

`reject`,

`rollback`,

`interrupt`,

`enqueue`

langsmith\_session\_name

string | null

LangSmith tracing session (project) name for this run, when tracing is enabled at creation time.

cancel\_reason

string | null

Why the run was cancelled, if it was: for example an explicit cancel request, a client disconnecting, or a newer run superseding it. Server-generated.

priority

integer

Queue priority level of the run, from -5 to 5. When all workers are busy, runs at a lower level start first.

Required range: `-5 <= x <= 5`