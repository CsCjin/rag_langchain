---
title: "List tools for a vendor - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/list-tools-for-a-vendor
scraped_at: 2026-11-15T03:41:09.503376
word_count: 59
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

#### Query Parameters

limit

integer

Max tools to return (default 50)

offset

integer

Number of tools to skip (default 0)

#### Response

200

application/json

OK

limit

integer

offset

integer

tools

object[]

Show child attributes

total

integer