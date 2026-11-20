---
title: "Count examples - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/examples/count-examples
scraped_at: 2026-11-15T03:40:54.261636
word_count: 125
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

id

string<uuid>[] | null

Only count examples with these IDs.

as\_of

string<date-time>stringstring<date-time>string

default:latest

Only modifications made on or before this time are included. If None, the latest version of the dataset is used.

metadata

string | null

JSON object. Only count examples whose metadata contains it.

full\_text\_contains

string[] | null

Only count examples whose inputs or outputs contain every one of these terms, ignoring case.

splits

string[] | null

Only count examples in any of these splits.

dataset

string<uuid> | null

Only count examples in this dataset.

filter

string | null

Filter expression the examples must match.

#### Response

200

application/json

Successful Response

The response is of type `integer`.