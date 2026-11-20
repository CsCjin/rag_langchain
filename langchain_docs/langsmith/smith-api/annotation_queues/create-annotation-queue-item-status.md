---
title: "Create annotation queue item status - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation_queues/create-annotation-queue-item-status
scraped_at: 2026-11-15T03:40:32.066159
word_count: 51
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

queue\_item\_id

string

required

Annotation queue item ID

#### Body

application/json

override\_added\_at

string

status

enum<string>

Available options:

`viewed`,

`completed`

#### Response

200

application/json

OK

is\_archived

boolean

override\_added\_at

string

queue\_item\_id

string

status

enum<string>

Available options:

`viewed`,

`completed`