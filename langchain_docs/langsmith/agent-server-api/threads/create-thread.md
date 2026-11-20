---
title: "Create Thread - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/threads/create-thread
scraped_at: 2026-11-15T03:38:17.546708
word_count: 284
---

#### Body

application/json

Payload for creating a thread.

thread\_id

string<uuid>

The ID of the thread. If not provided, a random UUID will be generated.

metadata

Metadata · object

Metadata to add to thread.

if\_exists

enum<string>

default:raise

How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do\_nothing' (return existing thread).

Available options:

`raise`,

`do_nothing`

ttl

TTL · object

The time-to-live for the thread.

Show child attributes

supersteps

object[]

Show child attributes

#### Response

200

application/json

Success

thread\_id

string<uuid>

required

The ID of the thread.

created\_at

string<date-time>

required

The time the thread was created.

updated\_at

string<date-time>

required

The last time the thread was updated.

metadata

Metadata · object

required

The thread metadata.

status

enum<string>

required

The status of the thread.

Available options:

`idle`,

`busy`,

`interrupted`,

`error`

state\_updated\_at

string<date-time>

The last time the thread state was updated.

config

Config · object

The thread config.

values

Values · object

The current state of the thread.

interrupts

Interrupts · object

The current interrupts of the thread.

run\_priority

integer | null

The queue priority level of the thread's runs, from -5 (highest priority) to 5 (lowest priority). Set at the thread's first run; null until then.

Required range: `-5 <= x <= 5`

fairness\_group

string | null

A label for the thread's runs, such as a tenant or customer ID, kept for sharing workers fairly between tenants; scheduling doesn't use it yet. Set at the thread's first run with a default of "default"; null until then.

ttl

TTL Info · object

TTL information if set for this thread. Only present when ?include=ttl is passed.

Show child attributes

extracted

Extracted · object

Extracted values from thread JSONB columns, populated when extract is specified in search request.