---
title: "Search Threads - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/threads/search-threads
scraped_at: 2026-11-15T03:38:19.765286
word_count: 487
---

#### Body

application/json

Payload for listing threads.

ids

string<uuid>[]

List of thread IDs to include. Others are excluded.

metadata

Metadata · object

Thread metadata to filter on.

exclude\_metadata

Exclude Metadata · object

Exclude threads whose metadata contains this object, or any object in this list. Uses the same matching as `metadata`; threads missing the keys are not excluded.

* Exclude Metadata · object
* Exclude Metadata · object[]

created\_after

string<date-time>

Only include threads created at or after this time (ISO 8601). Timestamps without a timezone are treated as UTC.

created\_before

string<date-time>

Only include threads created before this time (ISO 8601). Timestamps without a timezone are treated as UTC.

state\_updated\_after

string<date-time>

Only include threads whose state last changed at or after this time (ISO 8601). Timestamps without a timezone are treated as UTC.

state\_updated\_before

string<date-time>

Only include threads whose state last changed before this time (ISO 8601). Timestamps without a timezone are treated as UTC.

values

Values · object

State values to filter on.

status

enum<string>

Thread status to filter on.

Available options:

`idle`,

`busy`,

`interrupted`,

`error`

limit

integer

default:10

Maximum number to return.

Required range: `1 <= x <= 1000`

offset

integer

default:0

Offset to start from.

Required range: `x >= 0`

sort\_by

enum<string>

Sort by field.

Available options:

`thread_id`,

`status`,

`created_at`,

`updated_at`,

`state_updated_at`

sort\_order

enum<string>

Sort order.

Available options:

`asc`,

`desc`

select

enum<string>[]

Specify which fields to return. If not provided, all fields are returned.

Available options:

`thread_id`,

`created_at`,

`updated_at`,

`state_updated_at`,

`metadata`,

`config`,

`status`,

`values`,

`interrupts`,

`run_priority`,

`fairness_group`

extract

Extract · object

Map of alias to JSONB path for extracting specific values. Paths must start with values, metadata, config, or interrupts. Example: {"last\_msg": "values.messages[-1]"}.

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