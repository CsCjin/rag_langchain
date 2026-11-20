---
title: "Cancel Runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/cancel-runs
scraped_at: 2026-11-15T03:38:15.235737
word_count: 101
---

#### Query Parameters

action

enum<string>

default:interrupt

Action to take when cancelling the run. Possible values are `interrupt` or `rollback`. `interrupt` will simply cancel the run. `rollback` will cancel the run and delete the run and associated checkpoints afterwards.

Available options:

`interrupt`,

`rollback`

#### Body

application/json

* RunsCancel
* RunsCancel

Payload for cancelling runs.

status

enum<string>

required

Filter runs by status to cancel. Must be one of 'pending', 'running', or 'all'.

Available options:

`pending`,

`running`,

`all`

thread\_id

string<uuid>

The ID of the thread containing runs to cancel.

run\_ids

string<uuid>[]

List of run IDs to cancel.

#### Response

204

Success - Runs cancelled