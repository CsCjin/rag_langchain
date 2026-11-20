---
title: "Patch Assistant - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/assistants/patch-assistant
scraped_at: 2026-11-15T03:38:09.860631
word_count: 220
---

#### Path Parameters

assistant\_id

string<uuid>

required

The ID of the assistant.

#### Body

application/json

Payload for updating an assistant.

graph\_id

string

The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration. If not provided, assistant will keep pointing to same graph.

config

Config · object

Configuration to use for the graph. Useful when graph is configurable and you want to update the assistant's configuration.

context

Context · object

Static context added to the assistant.

metadata

Metadata · object

Metadata to merge with existing assistant metadata.

name

string

The new name for the assistant. If not provided, assistant will keep its current name.

description

string

The new description for the assistant. If not provided, assistant will keep its current description.

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