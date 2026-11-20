---
title: "Studio experiment - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/studio-experiment
scraped_at: 2026-11-15T03:40:51.047185
word_count: 38
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

project\_name

string

required

dataset\_id

string<uuid>

required

evaluator\_rules

string<uuid>[] | null

metadata

Metadata · object | null

#### Response

200

application/json

Successful Response