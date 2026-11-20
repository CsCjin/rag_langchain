---
title: "Get the annotation queue item count - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation_queues/get-the-annotation-queue-item-count
scraped_at: 2026-11-15T03:40:33.129997
word_count: 81
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

Queue ID

#### Query Parameters

status

string

required

Count bucket: all, needs\_my\_review, needs\_others\_review, or archived.

start\_time

string

Archived strictly after this time. Only used when status=archived

end\_time

string

Archived strictly before this time. Only used when status=archived

min\_start\_time

string<date-time>

Trace started at or after this time

max\_start\_time

string<date-time>

Trace started at or before this time

#### Response

200

application/json

OK

count

integer