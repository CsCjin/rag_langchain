---
title: "Create vendor settings - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/create-vendor-settings
scraped_at: 2026-11-15T03:41:08.511314
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

201

application/json

Created

is\_configured

boolean

organization\_id

string

project\_id

string