---
title: "Add runs to annotation queue - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/add-runs-to-annotation-queue
scraped_at: 2026-11-15T03:40:27.126872
word_count: 53
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

extend\_trace\_retention

boolean

default:false

#### Body

application/json

#### Response

200

application/json

Successful Response

run\_id

string<uuid>

required

queue\_id

string<uuid>

required

id

string<uuid>

required

last\_reviewed\_time

string<date-time> | null

added\_at

string<date-time>

source\_proposed\_example\_id

string<uuid> | null