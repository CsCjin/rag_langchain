---
title: "Delete annotation queue items - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation_queues/delete-annotation-queue-items
scraped_at: 2026-11-15T03:40:32.300406
word_count: 34
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

#### Body

application/json

item\_ids

string[]

#### Response

200

application/json

OK

{key}

string