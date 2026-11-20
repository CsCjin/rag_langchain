---
title: "Populate annotation queue - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/populate-annotation-queue
scraped_at: 2026-11-15T03:40:30.907116
word_count: 65
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

queue\_id

string<uuid>

required

ID of the annotation queue to add runs to.

session\_ids

string<uuid>[]

required

Experiments whose runs are added to the queue. Each must be an experiment on a dataset.

extend\_trace\_retention

boolean

default:false

Upgrade the added traces from short-lived to extended retention.

#### Response

200

application/json

Successful Response