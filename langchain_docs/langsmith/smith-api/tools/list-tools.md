---
title: "List tools - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tools/list-tools
scraped_at: 2026-11-15T03:42:07.044731
word_count: 56
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

Maximum number of tools to return

offset

integer

Number of tools to skip

query

string

Search query to filter tools by name or description

#### Response

200

application/json

OK

next\_offset

integer

tools

object[]

Show child attributes

total

integer