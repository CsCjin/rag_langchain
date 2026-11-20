---
title: "Protocol v2 Command - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/streaming/protocol-v2-command
scraped_at: 2026-11-15T03:38:14.032406
word_count: 120
---

#### Path Parameters

thread\_id

string<uuid>

required

The ID of the thread the command applies to.

#### Body

application/json

A client → server command envelope. Known methods: `run.start`, `input.respond`, `subscription.subscribe` (WS only), `subscription.unsubscribe` (WS only), `agent.getTree`.

id

integer

required

Client-assigned command id; echoed in the response.

Required range: `x >= 0`

method

string

required

Command method name (e.g. `run.start`).

params

object

Method-specific parameters. See the CDDL spec for per-method shapes.

#### Response

200

application/json

Protocol response — either `ProtocolSuccess` or `ProtocolError`.

* ProtocolSuccess
* ProtocolError

Successful command response.

type

string

required

Allowed value: `"success"`

id

integer

required

Required range: `x >= 0`

result

object

required

Method-specific result payload.

meta

ProtocolResponseMeta · object

Optional metadata attached to command responses.

Show child attributes