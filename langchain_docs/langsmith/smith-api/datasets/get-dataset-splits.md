---
title: "Get dataset splits - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/get-dataset-splits
scraped_at: 2026-11-15T03:40:49.325829
word_count: 51
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

dataset\_id

string<uuid>

required

#### Query Parameters

as\_of

string<date-time>stringstring<date-time>string

default:latest

Only modifications made on or before this time are included. If None, the latest version of the dataset is used.

#### Response

200

application/json

Successful Response