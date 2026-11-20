---
title: "Count shared examples - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/public/count-shared-examples
scraped_at: 2026-11-15T03:41:33.061090
word_count: 56
---

#### Path Parameters

share\_token

string<uuid>

required

#### Query Parameters

id

string<uuid>[] | null

as\_of

string<date-time>stringstring<date-time>string

default:latest

Only modifications made on or before this time are included. If None, the latest version of the dataset is used.

metadata

string | null

filter

string | null

#### Response

200

application/json

Successful Response

The response is of type `integer`.