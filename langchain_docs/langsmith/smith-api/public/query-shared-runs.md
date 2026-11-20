---
title: "Query shared runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/public/query-shared-runs
scraped_at: 2026-11-15T03:41:34.551473
word_count: 45
---

#### Path Parameters

share\_token

string<uuid>

required

#### Body

application/json

Query params for public run endpoints.

id

string<uuid>[] | null

#### Response

200

application/json

Successful Response

runs

RunPublicSchema · object[]

required

Show child attributes

cursors

Cursors · object

required

Show child attributes

parsed\_query

string | null