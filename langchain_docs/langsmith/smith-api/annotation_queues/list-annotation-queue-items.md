---
title: "List annotation queue items - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation_queues/list-annotation-queue-items
scraped_at: 2026-11-15T03:40:33.261941
word_count: 134
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

queue\_id

string

required

Annotation queue ID

#### Query Parameters

status

enum<string>

required

Review section: needs\_my\_review, needs\_others\_review, or archived

Available options:

`needs_my_review`,

`needs_others_review`,

`archived`

page\_size

integer

default:20

Page size (max 100)

cursor

string

Opaque pagination cursor

item\_type

enum<string>

Filter to RUN or THREAD

Available options:

`RUN`,

`THREAD`

min\_start\_time

string<date-time>

Only items whose trace start time is at or after this timestamp. Omit or send the zero time for no bound

max\_start\_time

string<date-time>

Only items whose trace start time is at or before this timestamp. Omit or send the zero time for no bound

direction

enum<string>

default:forward

Pagination direction. backward requires cursor

Available options:

`forward`,

`backward`

#### Response

200

application/json

OK

items

object[]

Show child attributes

next\_cursor

string

previous\_cursor

string