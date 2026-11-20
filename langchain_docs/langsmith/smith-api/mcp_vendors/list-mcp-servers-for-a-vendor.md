---
title: "List MCP servers for a vendor - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/list-mcp-servers-for-a-vendor
scraped_at: 2026-11-15T03:41:09.770974
word_count: 61
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

Max items to return (default 100)

offset

integer

Number of items to skip (default 0)

#### Response

200

application/json

OK

items

object[]

Show child attributes

limit

integer

offset

integer

page\_count

integer

total\_count

integer