---
title: "Create Background Run - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/stateless-runs/create-background-run
scraped_at: 2026-11-15T03:38:12.255485
word_count: 377
---

#### Body

application/json

Payload for creating a run.

assistant\_id

string<uuid>stringstring<uuid>string

required

The assistant ID or graph name to run. If using graph name, will default to first assistant created from that graph.

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

feedback\_keys

string[]

Generate pre-signed URLs for assigning feedback keys to the run.

For each key specified, a unique URL will be generated that can be called to assign the feedback key to the run. See [LangSmith Feedback](https://docs.langchain.com/langsmith/observability-concepts#feedback) for more details.

stream\_subgraphs

boolean

default:false

Whether to stream output from subgraphs.

stream\_resumable

boolean

default:false

Whether to keep the run's stream events so a client can rejoin the run. Deployments keep every run's events for `RESUMABLE_STREAM_TTL_SECONDS` (2 minutes by default) regardless of this field. The in-memory runtime (`langgraph dev`) keeps them only when it is true.

on\_completion

enum<string>

default:delete

Whether to delete or keep the thread created for a stateless run. Must be one of 'delete' or 'keep'.

Available options:

`delete`,

`keep`

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

#### Response

200

application/json

Success