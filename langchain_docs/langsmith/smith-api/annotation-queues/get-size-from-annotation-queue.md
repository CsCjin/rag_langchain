---
title: "Get size from annotation queue - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-size-from-annotation-queue
scraped_at: 2026-11-15T03:40:30.560907
word_count: 45
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

queue\_id

string<uuid>

required

#### Query Parameters

status

enum<string> | null

Available options:

`needs_my_review`,

`needs_others_review`,

`completed`

#### Response

200

application/json

Successful Response

Size of an Annotation Queue

size

integer

required