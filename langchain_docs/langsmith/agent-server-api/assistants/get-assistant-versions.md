---
title: "Get Assistant Versions - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-versions
scraped_at: 2026-11-15T03:38:09.747366
word_count: 103
---

#### Path Parameters

assistant\_id

string<uuid>

required

The ID of the assistant.

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