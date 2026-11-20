---
title: "Delete runs from annotation queue - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/delete-runs-from-annotation-queue
scraped_at: 2026-11-15T03:40:28.677524
word_count: 39
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

#### Body

application/json

delete\_all

boolean

default:false

run\_ids

string<uuid>[] | null

exclude\_run\_ids

string<uuid>[] | null

#### Response

200

application/json

Successful Response