---
title: "Get shared tokens - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/get-shared-tokens
scraped_at: 2026-11-15T03:42:21.739313
word_count: 62
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

limit

integer

default:50

Required range: `1 <= x <= 100`

offset

integer

default:0

Required range: `x >= 0`

#### Response

200

application/json

Successful Response

entities

(TenantShareRunToken · object | TenantShareDatasetToken · object | TenantShareThreadToken · object)[]

required

* TenantShareRunToken
* TenantShareDatasetToken
* TenantShareThreadToken

Show child attributes