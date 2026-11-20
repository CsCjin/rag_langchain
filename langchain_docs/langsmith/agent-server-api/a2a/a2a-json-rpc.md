---
title: "A2A JSON-RPC - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/a2a/a2a-json-rpc
scraped_at: 2026-11-15T03:38:07.952590
word_count: 136
---

#### Headers

Accept

string

required

For `message/stream`, must include `text/event-stream`. For all other methods, use `application/json`.

#### Path Parameters

assistant\_id

string<uuid>

required

The ID of the assistant to communicate with

#### Body

application/json

jsonrpc

enum<string>

required

JSON-RPC version

Available options:

`2.0`

id

string

required

Request identifier

method

enum<string>

required

The method to invoke

Available options:

`message/send`,

`message/stream`,

`tasks/get`,

`tasks/cancel`

params

Message Send/Stream Parameters · object

Method parameters; shape depends on the method.

* Message Send/Stream Parameters
* Task Get Parameters
* Task Cancel Parameters

Show child attributes

#### Response

200

application/json

JSON-RPC response for non-streaming methods. For `message/stream`, the response is an SSE stream of JSON-RPC envelopes.

jsonrpc

enum<string>

required

Available options:

`2.0`

id

string

required

result

object

Success result containing task information or task details

error

object

Error information if request failed

Show child attributes