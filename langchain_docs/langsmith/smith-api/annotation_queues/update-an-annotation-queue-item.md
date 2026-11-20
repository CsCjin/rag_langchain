---
title: "Update an annotation queue item - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation_queues/update-an-annotation-queue-item
scraped_at: 2026-11-15T03:40:33.409293
word_count: 75
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

#### Body

application/json

added\_at

string<date-time>

last\_reviewed\_time

string<date-time>

#### Response

200

application/json

OK

added\_at

string

id

string

item\_type

enum<string>

Available options:

`RUN`,

`THREAD`

last\_reviewed\_time

string

LastReviewedTime is always present on the wire (null until reviewed).

project\_id

string

queue\_id

string

run\_id

string

source\_proposed\_example\_id

string

start\_time

string

thread\_id

string