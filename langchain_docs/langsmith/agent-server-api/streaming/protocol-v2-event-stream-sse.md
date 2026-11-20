---
title: "Protocol v2 Event Stream (SSE) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/streaming/protocol-v2-event-stream-sse
scraped_at: 2026-11-15T03:38:14.207454
word_count: 269
---

#### Path Parameters

thread\_id

string<uuid>

required

The ID of the thread to observe.

#### Body

application/json

Body of `POST /threads/{thread_id}/stream/events`. Filters the connection-scoped SSE stream.

channels

(enum<string> | string)[]

required

Channels to subscribe to for the lifetime of this connection.

Minimum array length: `1`

Subscribable event channel. One of the eight fixed channels or a user-defined `custom:<name>` namespaced custom channel emitted by a stream transformer. `debug` and `checkpoints` were removed from the protocol in `@langchain/protocol@0.0.10` — task-level debug info now flows on the `tasks` channel, and checkpoint pointers ride on `values` events as an attached `checkpoint` envelope.

Available options:

`values`,

`updates`,

`messages`,

`tools`,

`lifecycle`,

`input`,

`tasks`,

`custom`

namespaces

string[][]

Prefix-match filter. An event matches if its namespace starts with any of these prefixes. Omit for all namespaces.

Hierarchical path identifying a position in the agent tree. Empty array denotes the root agent; each segment names a nested subgraph.

depth

integer

Max depth below the namespace prefix. Omit for unbounded depth.

Required range: `x >= 0`

since

integer

Replay events with `seq` greater than this value before streaming live events.

Required range: `x >= 0`

#### Response

200

text/event-stream

SSE event stream

Stream of `ProtocolEvent` frames. Each SSE frame uses the event's `method` as the `event:` field and a JSON-encoded `ProtocolEvent` as the `data:` field; `id:` is set to the event's `seq`.

If reading the thread's event stream fails, the server ends the stream with a final frame whose `event:` field is `error` and whose `data:` field is a `ProtocolError` with `id: null` and `error: "unknown_error"`. That frame has no `id:` field.

Example frame:

id: 42

event: messages

data: {"type":"event","event\_id":"42","seq":42,"method":"messages","params":{"namespace":[],"timestamp":1700000000000,"data":{...}}}