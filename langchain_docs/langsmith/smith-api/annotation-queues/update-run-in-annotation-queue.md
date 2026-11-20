---
title: "Update run in annotation queue - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/update-run-in-annotation-queue
scraped_at: 2026-11-15T03:40:31.737393
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

queue\_run\_id

string<uuid>

required

#### Body

application/json

last\_reviewed\_time

string<date-time> | null

added\_at

string<date-time> | null

#### Response

200

application/json

Successful Response