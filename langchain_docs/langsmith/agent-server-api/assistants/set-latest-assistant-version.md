---
title: "Set Latest Assistant Version - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/assistants/set-latest-assistant-version
scraped_at: 2026-11-15T03:38:10.300321
word_count: 122
---

#### Path Parameters

assistant\_id

string<uuid>

required

The ID of the assistant.

#### Query Parameters

version

integer

required

The version to change to.
The version of the assistant to change to.

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