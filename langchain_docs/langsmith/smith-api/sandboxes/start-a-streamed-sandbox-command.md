---
title: "Start a streamed sandbox command - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/start-a-streamed-sandbox-command
scraped_at: 2026-11-15T03:41:54.225740
word_count: 187
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

sandbox\_id

string

required

Sandbox ID or name

#### Body

application/json

command

string[]

Command accepts either a shell command string or an argv string array.

command\_id

string

CommandID makes the request idempotent: a known ID attaches to that
running command instead of starting a second one.

cwd

string

deprecated

Deprecated: use run\_config.work\_dir. Rejected when run\_config is also set.

env

object

deprecated

Deprecated: use run\_config.env\_vars. Rejected when run\_config is also set.

Show child attributes

idle\_timeout\_seconds

integer

0 = default, -1 = never idle-kill

run\_config

object

RunConfig overrides, for this command only, the user, working directory and env the sandbox's commands run with.

Show child attributes

shell

string

stdin

string<byte>

Stdin is the process's entire standard input, base64 on the wire. It is
written once when the command is spawned and then closed, so the process
reads EOF; there is no stdin streaming on this endpoint.

timeout\_seconds

integer

0 = no timeout

ttl\_seconds

integer

0 = default, -1 = keep forever

#### Response

200

text/event-stream

SSE event stream

The response is of type `string`.