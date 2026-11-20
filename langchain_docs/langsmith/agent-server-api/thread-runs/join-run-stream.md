---
title: "Join Run Stream - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/join-run-stream
scraped_at: 2026-11-15T03:38:16.668445
word_count: 466
---

#### Headers

Last-Event-ID

string

The ID of the last event received. Set to -1 if you want to stream all events. In the in-memory runtime (`langgraph dev`), requires `stream_resumable=true` when creating the run.

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

checkpoint\_id

string<uuid>

Resume after this checkpoint of the run, such as the one the thread's state was just loaded at: events up to the checkpoint are skipped. Used when `Last-Event-ID` is absent, `-` or `-1`; a real `Last-Event-ID` takes precedence. If the run's stream has no record of the checkpoint, the stream starts from the beginning of the run, as with -1. Send it with `Last-Event-ID: -1`, so a server that ignores it replays the whole run instead of streaming only new events. The in-memory runtime (`langgraph dev`) ignores it and replays the whole run, which needs `stream_resumable=true` when creating the run.

stream\_mode

enum<string>enum<string>[]enum<string>enum<string>[]

Stream modes to control which of the run's events are returned. Only modes the run was created with have events. Events about the whole run, such as `metadata` (which starts each attempt of the run), `error` and `feedback`, always pass, except on the `langgraph dev` server, which passes only `error`. If not provided, all of the run's events are returned.

Available options:

`values`,

`messages`,

`messages-tuple`,

`tasks`,

`checkpoints`,

`updates`,

`events`,

`debug`,

`custom`,

`tools`,

`lifecycle`

namespace

string[]

A conversation to stream: a `|`-joined namespace, empty for the main agent (the root graph) or a subagent's, such as `tools:<task_id>`. The stream keeps that conversation's events without those of the subagents it starts (subgraphs that the `tools` node runs), but with the `lifecycle` events of every subagent below it. Repeat it to stream several conversations. Events about the whole run, such as `metadata` and `error`, always pass. Events of the `events` and `messages` modes (not `messages-tuple`) carry no namespace, so they stream with the main agent's conversation. Subagent events exist only on runs created with `stream_subgraphs`, except `lifecycle` events, which come either way. If not provided, all of the run's events are returned.

Maximum array length: `32`

cancel\_on\_disconnect

boolean

default:false

If true, the run will be cancelled if the client disconnects.

#### Response

200

text/event-stream

Success

The server will send a stream of events in SSE format. The last event is `end`, with data `{"run_id": ..., "status": ...}` giving the run's final status: `success` (also when the run stops at an interrupt), `error`, `timeout`, `interrupted` (the run was cancelled) or, for a stateless run, `rollback`. A run that was deleted, or rolled back on a thread, has no status left, so its stream ends with its `error` event instead. If a stream closes with neither, get the run to see how it ended.

Example event:

id: 1

event: message

data: {}