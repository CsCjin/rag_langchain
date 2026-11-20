---
title: "Generate query for runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/generate-query-for-runs
scraped_at: 2026-11-15T03:41:38.842302
word_count: 48
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

query

string

required

feedback\_keys

enum<string>[]

Available options:

`user_score`,

`user_edited`,

`user_removed`,

`user_opened_run`,

`user_selected_run`,

`results_size`,

`valid_filter`

#### Response

200

application/json

Successful Response

filter

string

required

feedback\_urls

Feedback Urls · object

required

Show child attributes