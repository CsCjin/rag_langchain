---
title: "Delete an example - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/examples/delete-an-example
scraped_at: 2026-11-15T03:40:54.575562
word_count: 48
---

#### Authorizations

API Key & Tenant IDBearer Auth & Tenant IDAPI Key & Tenant IDBearer Auth & Tenant ID

X-API-Key

string

header

required

X-Tenant-Id

string

header

required

#### Path Parameters

dataset\_id

string<uuid>

required

Dataset ID

example\_id

string<uuid>

required

Example ID

#### Response

204

Example deleted or already deleted