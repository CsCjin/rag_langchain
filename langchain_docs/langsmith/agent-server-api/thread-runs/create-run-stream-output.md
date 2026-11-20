---
title: "Create Run, Stream Output - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/create-run-stream-output
scraped_at: 2026-11-15T03:38:15.768820
word_count: 726
---

#### Path Parameters

thread\_id

string<uuid>

required

The ID of the thread.

#### Query Parameters

namespace

string[]

A conversation to stream: a `|`-joined namespace, empty for the main agent (the root graph) or a subagent's, such as `tools:<task_id>`. The stream keeps that conversation's events without those of the subagents it starts (subgraphs that the `tools` node runs), but with the `lifecycle` events of every subagent below it. Repeat it to stream several conversations. Events about the whole run, such as `metadata` and `error`, always pass. Events of the `events` and `messages` modes (not `messages-tuple`) carry no namespace, so they stream with the main agent's conversation. Subagent events exist only on runs created with `stream_subgraphs`, except `lifecycle` events, which come either way. If not provided, all of the run's events are returned.

Maximum array length: `32`

#### Body

application/json

Payload for creating a run.

assistant\_id

string<uuid>stringstring<uuid>string

required

The assistant ID or graph name to run. If using graph name, will default to first assistant created from that graph.

checkpoint

Checkpoint · object

The checkpoint to resume from.

Show child attributes

input

Input · objectany[]stringnumberbooleanInput · objectany[]stringnumberboolean

The input to the graph.

command

Command · object | null

The command to run.

Show child attributes

metadata

Metadata · object

Metadata to assign to the run.

config

Config · object

The configuration for the assistant.

Show child attributes

context

Context · object

Static context added to the assistant.

webhook

string<uri-reference>

Webhook to call after LangGraph API call is done.

Required string length: `1 - 65536`

interrupt\_before

enum<string>string[]enum<string>string[]

Nodes to interrupt immediately before they get executed.

Available options:

`*`

interrupt\_after

enum<string>string[]enum<string>string[]

Nodes to interrupt immediately after they get executed.

Available options:

`*`

stream\_mode

enum<string>[]enum<string>enum<string>[]enum<string>

The stream mode(s) to use. `lifecycle` sends `lifecycle|<namespace>` events when a subagent (a subgraph) starts and ends: `{"event": "started" | "completed" | "failed" | "interrupted", "namespace", "tool_call_id"?, "error"?}`, with the id of the tool call that started it, with or without `stream_subgraphs`. `tools` sends `on_tool_start`, `on_tool_event`, `on_tool_end` and `on_tool_error` events with `toolCallId` and `name` (from langgraph 1.2.19 and @langchain/langgraph 1.6.0; a tool error's text is never sent).

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

stream\_subgraphs

boolean

default:false

Whether to stream output from subgraphs.

stream\_resumable

boolean

default:false

Whether to keep the run's stream events so a client can rejoin the run. Deployments keep every run's events for `RESUMABLE_STREAM_TTL_SECONDS` (2 minutes by default) regardless of this field. The in-memory runtime (`langgraph dev`) keeps them only when it is true.

strict\_resume

boolean

default:false

Refuse a `command.resume` that names an interrupt that isn't pending, before the graph runs: the run ends with `UnknownInterruptError` and the thread keeps its state. Needs a langgraph version with strict resume; `/info` reports `strict_resume` when it is available.

feedback\_keys

string[]

Generate pre-signed URLs for assigning feedback keys to the run.

For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

multitask\_strategy

enum<string>

default:enqueue

Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.

Available options:

`reject`,

`rollback`,

`interrupt`,

`enqueue`

if\_not\_exists

enum<string>

default:reject

How to handle missing thread. Must be either 'reject' (raise error if missing), or 'create' (create new thread).

Available options:

`create`,

`reject`

after\_seconds

number

The number of seconds to wait before starting the run. Use to schedule future runs.

checkpoint\_during

boolean

default:false

deprecated

Whether to checkpoint during the run.

Deprecated. Use `durability` instead to control checkpoint persistence behavior during the run.

durability

enum<string>

default:async

Durability level for the run. Must be one of `sync`, `async`, or `exit`. See [durability modes](https://docs.langchain.com/oss/python/langgraph/checkpointers#durability-modes) for more details.

Available options:

`sync`,

`async`,

`exit`

on\_disconnect

enum<string>

default:continue

The disconnect mode to use. Must be one of 'cancel' or 'continue'.

Available options:

`cancel`,

`continue`

#### Response

200

text/event-stream

Success

The server will send a stream of events in SSE format. The last event is `end`, with data `{"run_id": ..., "status": ...}` giving the run's final status: `success` (also when the run stops at an interrupt), `error`, `timeout`, `interrupted` (the run was cancelled) or, for a stateless run, `rollback`. A run that was deleted, or rolled back on a thread, has no status left, so its stream ends with its `error` event instead. If a stream closes with neither, get the run to see how it ended.

Example event:

id: 1

event: message

data: {}