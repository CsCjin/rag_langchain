---
title: "Get annotation queue item placement - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation_queues/get-annotation-queue-item-placement
scraped_at: 2026-11-15T03:40:32.787631
word_count: 51
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

item\_id

string

required

Annotation queue item ID

#### Response

200

application/json

OK

cursor

string

item\_type

enum<string>

Available options:

`RUN`,

`THREAD`

position

integer

section

enum<string>

Available options:

`needs_my_review`,

`needs_others_review`,

`archived`