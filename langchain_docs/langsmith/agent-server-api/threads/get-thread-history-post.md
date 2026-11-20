---
title: "Get Thread History Post - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-history-post
scraped_at: 2026-11-15T03:38:18.405819
word_count: 164
---

#### Path Parameters

thread\_id

string<uuid>

required

The ID of the thread.

#### Body

application/json

limit

integer

default:1

The maximum number of states to return.

Required range: `1 <= x <= 1000`

before

Before · object

Return states before this checkpoint.

Show child attributes

metadata

Metadata · object

Filter states by metadata key-value pairs.

checkpoint

Checkpoint · object

Return states for this subgraph.

Show child attributes

select

(enum<string> | string)[]

Specify which fields of each state to return. Use `values.<key>` to return only that key of the state values, for example `values.messages`. If not provided, all fields are returned.

Available options:

`values`,

`next`,

`tasks`,

`checkpoint`,

`metadata`,

`created_at`,

`parent_checkpoint`,

`interrupts`

#### Response

200

application/json

Success

values

object

required

* Values · object[]
* Values · object

next

string[]

required

checkpoint

Checkpoint · object

required

Checkpoint config.

Show child attributes

metadata

Metadata · object

required

created\_at

string

required

tasks

Tasks · object[]

Show child attributes

parent\_checkpoint

Parent Checkpoint · object

interrupts

Interrupt · object[]

Show child attributes