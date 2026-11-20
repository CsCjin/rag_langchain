---
title: "Create Assistant - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/assistants/create-assistant
scraped_at: 2026-11-15T03:38:08.465815
word_count: 230
---

#### Body

application/json

Payload for creating an assistant.

graph\_id

string

required

The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration.

assistant\_id

string<uuid>

The ID of the assistant. If not provided, a random UUID will be generated.

config

Config · object

Configuration to use for the graph. Useful when graph is configurable and you want to create different assistants based on different configurations.

context

Context · object

Static context added to the assistant.

metadata

Metadata · object

Metadata to add to assistant.

if\_exists

enum<string>

default:raise

How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do\_nothing' (return existing assistant).

Available options:

`raise`,

`do_nothing`

name

string

The name of the assistant. Defaults to 'Untitled'.

description

string | null

The description of the assistant. Defaults to null.

#### Response

200

application/json

Success

assistant\_id

string<uuid>

required

The ID of the assistant.

graph\_id

string

required

The ID of the graph.

config

Config · object

required

The assistant config.

Show child attributes

created\_at

string<date-time>

required

The time the assistant was created.

updated\_at

string<date-time>

required

The last time the assistant was updated.

metadata

Metadata · object

required

The assistant metadata.

context

Context · object

Static context added to the assistant.

version

integer

The version of the assistant

name

string

The name of the assistant

description

string | null

The description of the assistant