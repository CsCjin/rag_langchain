---
title: "Export annotation queue archived runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/export-annotation-queue-archived-runs
scraped_at: 2026-11-15T03:40:28.922020
word_count: 45
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

Export annotation queue runs request schema.

start\_time

string<date-time> | null

end\_time

string<date-time> | null

include\_annotator\_detail

boolean

default:false

#### Response

200

application/json

Successful Response