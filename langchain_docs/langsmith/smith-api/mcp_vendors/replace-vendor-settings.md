---
title: "Replace vendor settings - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/replace-vendor-settings
scraped_at: 2026-11-15T03:41:09.857745
word_count: 41
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

vendor\_slug

string

required

Vendor slug (e.g. arcade)

#### Body

application/json

organization\_id

string

project\_id

string

#### Response

200

application/json

OK

is\_configured

boolean

organization\_id

string

project\_id

string