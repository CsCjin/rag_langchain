---
title: "Resolve annotation queue run - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/resolve-annotation-queue-run
scraped_at: 2026-11-15T03:40:31.052819
word_count: 47
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

#### Response

200

application/json

Successful Response

Resolved annotation queue run position for deep linking.

section

enum<string>

required

Available options:

`needs_my_review`,

`needs_others_review`,

`completed`

position

integer

required