---
title: "Search Assistants - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/assistants/search-assistants
scraped_at: 2026-11-15T03:38:10.115558
word_count: 242
---

#### Body

application/json

Payload for listing assistants.

metadata

Metadata · object

Metadata to filter by. Exact match filter for each KV pair.

graph\_id

string

The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration.

name

string

Name of the assistant to filter by. The filtering logic will match (case insensitive) assistants where 'name' is a substring of the assistant name.

limit

integer

default:10

The maximum number of results to return.

Required range: `1 <= x <= 1000`

offset

integer

default:0

The number of results to skip.

Required range: `x >= 0`

sort\_by

enum<string>

The field to sort by.

Available options:

`assistant_id`,

`created_at`,

`updated_at`,

`name`,

`graph_id`

sort\_order

enum<string>

The order to sort by.

Available options:

`asc`,

`desc`

select

enum<string>[]

Specify which fields to return. If not provided, all fields are returned.

Available options:

`assistant_id`,

`graph_id`,

`name`,

`description`,

`config`,

`context`,

`created_at`,

`updated_at`,

`metadata`,

`version`

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