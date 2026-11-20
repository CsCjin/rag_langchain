---
title: "Get MCP vendor - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/mcp_vendors/get-mcp-vendor
scraped_at: 2026-11-15T03:41:08.902890
word_count: 46
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

#### Response

200

application/json

OK

description

string

icon

string

name

string

provider\_id

string

settings

any

status

enum<string>

Available options:

`enabled`,

`disabled`

vendor\_id

string