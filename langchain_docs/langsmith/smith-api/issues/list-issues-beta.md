---
title: "List issues (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/issues/list-issues-beta
scraped_at: 2026-11-15T03:41:07.229768
word_count: 338
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

session\_id

string

Filter by session ID (UUID)

session\_name

string

Filter by session name (exact match)

status

enum<string>

Filter by status

Available options:

`open`,

`fixing`,

`watching`,

`completed`,

`ignored`

severity

enum<integer>

Filter by severity

Available options:

`0`,

`1`,

`2`,

`3`

severity\_exact

enum<integer>[]

Filter by exact severity (repeatable; OR semantics)

Available options:

`0`,

`1`,

`2`,

`3`

activity

enum<string>[]

Filter by Engine activity (repeatable; OR semantics)

Available options:

`fixing`,

`watching`,

`recurred`

tag

string

Filter by tag (exact match)

trace\_id

string<uuid>

Return only issues with a linked run in this trace

updated\_at

string

Return only issues updated at or after this RFC3339 timestamp

sort\_by

enum<string>

Sort field

Available options:

`default`,

`created_at`,

`updated_at`,

`last_seen`,

`last_updated`,

`trace_count`,

`severity`

status\_first

boolean

Group results by issue lifecycle status before applying sort\_by

limit

integer

Page size (positive integer; defaults to 50, capped at 500)

offset

integer

Page offset (non-negative integer; at most 100000)

#### Response

200

application/json

OK

actions

object

auto\_resolution\_evidence

object

auto\_resolution\_state

string

Nil unless eligible: "auto\_close" or "prompt". Evidence carries the deciding gate.

created\_at

string

description

string

evidence

object | null

Nil for the trace-list issues that are the norm.

Show child attributes

first\_seen\_at

string

fix\_branch

string

Legacy: branch of the oldest fix in the board's oldest connected repository.

fix\_dispatched\_at

string

fix\_pr\_number

integer

fix\_prompt

string

Issue-level: the problem every fix shares, and the last time a fix run
was dispatched for this issue — one run works several fixes.

fix\_verification

object

Show child attributes

fixes

object[]

Newest first.

Show child attributes

id

string

last\_seen\_at

string

linear\_context

object

Show child attributes

linear\_sync

object

Show child attributes

name

string

proposed\_context\_fixes

object[]

proposed\_examples

object[]

proposed\_fix

string

proposed\_prompt\_fixes

object[]

recurrences\_since\_watching

integer

RecurrencesSinceWatching counts linked traces whose run start\_time is after
watching\_since — i.e. recurrences observed during the current watch period.

session\_id

string

severity

enum<integer>

Available options:

`0`,

`1`,

`2`,

`3`

status

enum<string>

Available options:

`open`,

`fixing`,

`watching`,

`completed`,

`ignored`

tags

string[]

tenant\_id

string

traces

object

updated\_at

string

validation\_result

object

Show child attributes

watching\_since

string