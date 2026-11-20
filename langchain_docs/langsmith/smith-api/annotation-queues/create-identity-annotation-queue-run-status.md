---
title: "Create identity annotation queue run status - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/create-identity-annotation-queue-run-status
scraped_at: 2026-11-15T03:40:29.687158
word_count: 43
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

annotation\_queue\_run\_id

string<uuid>

required

#### Body

application/json

Identity annotation queue run status create schema.

status

string | null

override\_added\_at

string<date-time> | null

#### Response

200

application/json

Successful Response