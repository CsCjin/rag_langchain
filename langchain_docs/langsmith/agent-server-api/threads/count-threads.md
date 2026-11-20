---
title: "Count Threads - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/threads/count-threads
scraped_at: 2026-11-15T03:38:17.423830
word_count: 176
---

#### Body

application/json

Payload for counting threads.

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

#### Response

200

application/json

Success

The response is of type `integer`.