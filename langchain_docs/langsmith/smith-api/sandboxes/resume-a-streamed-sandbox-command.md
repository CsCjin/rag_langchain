---
title: "Resume a streamed sandbox command - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/resume-a-streamed-sandbox-command
scraped_at: 2026-11-15T03:41:53.569813
word_count: 90
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

command\_id

string

CommandID names the command to attach to.

stderr\_offset

integer

stdout\_offset

integer

StdoutOffset and StderrOffset are where to continue from, and are also the
ack for every buffered byte below them. Zero replays from the beginning,
which is what a retry sends when the stream broke before any output arrived.

#### Response

200

text/event-stream

SSE event stream

The response is of type `string`.