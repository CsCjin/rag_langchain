---
title: "Add annotation queue items - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation_queues/add-annotation-queue-items
scraped_at: 2026-11-15T03:40:32.198291
word_count: 56
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

extend\_trace\_retention

boolean

Extend trace retention for added run items

#### Body

application/json

items

object[]

Maximum array length: `100`

Show child attributes

#### Response

201

application/json

Created

items

object[]

Show child attributes