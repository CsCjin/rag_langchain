---
title: "Update Cron - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/crons/update-cron
scraped_at: 2026-11-15T03:38:11.728864
word_count: 436
---

#### Path Parameters

cron\_id

string<uuid>

required

#### Body

application/json

Payload for updating a cron job. All fields are optional.

schedule

string

The cron schedule to execute this job on.

timezone

string

IANA timezone for the cron schedule (e.g. 'America/New\_York'). Defaults to null, which is treated as UTC.

end\_time

string<date-time> | null

The end date to stop running the cron. Send null to clear a previously set end time; omit this field to leave the existing value unchanged.

input

object

* Input · object[]
* Input · object

metadata

Metadata · object

Metadata to merge with existing cron job metadata.

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

on\_run\_completed

enum<string>

What to do with the thread after the run completes. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up.

Available options:

`delete`,

`keep`

enabled

boolean

Enable or disable the cron job.

stream\_mode

enum<string>[]enum<string>enum<string>[]enum<string>

The stream mode(s) to use.

Available options:

`values`,

`messages`,

`messages-tuple`,

`tasks`,

`checkpoints`,

`updates`,

`events`,

`debug`,

`custom`

stream\_subgraphs

boolean

default:false

Whether to stream output from subgraphs.

stream\_resumable

boolean

default:false

Whether to keep the run's stream events so a client can rejoin the run. Deployments keep every run's events for `RESUMABLE_STREAM_TTL_SECONDS` (2 minutes by default) regardless of this field. The in-memory runtime (`langgraph dev`) keeps them only when it is true.

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

Represents a scheduled task.

cron\_id

string<uuid>

required

The ID of the cron.

thread\_id

string<uuid>

required

The ID of the thread.

end\_time

string<date-time>

required

The end date to stop running the cron.

schedule

string

required

The schedule to run, cron format.

created\_at

string<date-time>

required

The time the cron was created.

updated\_at

string<date-time>

required

The last time the cron was updated.

payload

Payload · object

required

The run payload to use for creating new run.

enabled

boolean

default:true

required

Whether the cron job should be enabled. Disabled crons are not executed.

assistant\_id

string<uuid> | null

The ID of the assistant.

user\_id

string | null

The ID of the user.

next\_run\_date

string<date-time> | null

The next run date of the cron.

metadata

Metadata · object

The cron metadata.