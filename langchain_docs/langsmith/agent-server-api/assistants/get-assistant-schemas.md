---
title: "Get Assistant Schemas - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-schemas
scraped_at: 2026-11-15T03:38:09.172328
word_count: 133
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

Defines the structure and properties of a graph.

graph\_id

string

required

The ID of the graph.

state\_schema

State Schema · object

required

The schema for the graph state. Missing if unable to generate JSON schema from graph.

input\_schema

Input Schema · object

The schema for the graph input. Missing if unable to generate JSON schema from graph.

output\_schema

Output Schema · object

The schema for the graph output. Missing if unable to generate JSON schema from graph.

config\_schema

Config Schema · object

The schema for the graph config. Missing if unable to generate JSON schema from graph.

context\_schema

Context Schema · object

The schema for the graph context. Missing if unable to generate JSON schema from graph.