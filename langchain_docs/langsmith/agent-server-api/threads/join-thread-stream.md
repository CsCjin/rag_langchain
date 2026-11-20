---
title: "Join Thread Stream - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/threads/join-thread-stream
scraped_at: 2026-11-15T03:38:19.274303
word_count: 231
---

#### Headers

Last-Event-ID

string

The ID of the last event received. Used to resume streaming from a specific point. Pass '-' to resume from the beginning. A `gap` event is sent, first on a resume or mid-stream, when events the client should receive may be missing. Its `reason` is `expired` when they may have aged out of the stream's history; `unknown_id` when the ID is later than any event the thread streamed, and the stream starts over from the beginning; or `too_large` when an event was over the size limit, with that event's stream mode in `mode`. `expired` errs on the safe side: once the stream's history has expired, a resume gets it unless its ID is the thread's last streamed event, which is kept for an hour after that.

#### Path Parameters

thread\_id

string<uuid>

required

The ID of the thread.

#### Query Parameters

stream\_modes

enum<string>enum<string>[]enum<string>enum<string>[]

default:["run\_modes"]

Stream modes to control which events are returned. 'lifecycle' returns only run start/end events and `interrupts` events (the interrupts a run answers), 'run\_modes' returns all run events (default behavior), 'state\_update' returns only state update events.

Available options:

`lifecycle`,

`run_modes`,

`state_update`

stream\_mode

enum<string>enum<string>[]enum<string>enum<string>[]

Alias of `stream_modes`, the name the SDKs send. Ignored when `stream_modes` is set.

Available options:

`lifecycle`,

`run_modes`,

`state_update`

#### Response

200

text/event-stream

Success

The server will send a stream of events in SSE format.

Example event:

id: 1

event: message

data: {}