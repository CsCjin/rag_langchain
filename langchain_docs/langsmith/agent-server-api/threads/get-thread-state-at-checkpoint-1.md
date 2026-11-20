---
title: "Get Thread State At Checkpoint - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-state-at-checkpoint-1
scraped_at: 2026-11-15T03:38:18.817071
word_count: 144
---

#### Path Parameters

thread\_id

string<uuid>

required

The ID of the thread.

#### Body

application/json

Payload for getting the state of a thread at a checkpoint.

checkpoint

Checkpoint · object

required

The checkpoint to get the state for.

Show child attributes

subgraphs

boolean

Include subgraph states.

select

(enum<string> | string)[]

Specify which fields of the state to return. Use `values.<key>` to return only that key of the state values, for example `values.messages`. If not provided, all fields are returned.

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