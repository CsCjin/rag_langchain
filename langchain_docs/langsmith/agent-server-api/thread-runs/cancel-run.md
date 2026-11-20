---
title: "Cancel Run - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/cancel-run
scraped_at: 2026-11-15T03:38:15.135508
word_count: 106
---

#### Path Parameters

thread\_id

string<uuid>

required

The ID of the thread.

run\_id

string<uuid>

required

The ID of the run.

#### Query Parameters

wait

boolean

default:false

action

enum<string>

default:interrupt

Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.

Available options:

`interrupt`,

`rollback`

reason

enum<string>

Use `taken` to mark run input absorbed for steering. Records a `cancel_reason` starting with `taken:`. Only supported with `action=interrupt`; cancellation behavior is unchanged. A 404 response means the run was not cancelled.

Available options:

`taken`

#### Response

200

application/json

Success