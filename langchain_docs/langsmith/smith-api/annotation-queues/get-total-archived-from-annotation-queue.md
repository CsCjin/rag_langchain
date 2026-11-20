---
title: "Get total archived from annotation queue - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-total-archived-from-annotation-queue
scraped_at: 2026-11-15T03:40:31.623105
word_count: 44
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

start\_time

string<date-time> | null

end\_time

string<date-time> | null

#### Response

200

application/json

Successful Response

Size of an Annotation Queue

size

integer

required