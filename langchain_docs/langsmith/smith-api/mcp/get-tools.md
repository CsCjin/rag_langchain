---
title: "Get tools - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/mcp/get-tools
scraped_at: 2026-11-15T03:41:07.844278
word_count: 57
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

url

string

required

oauth\_provider\_id

string | null

ls\_user\_id

string | null

agent\_id

string | null

force\_refresh

boolean

default:false

#### Response

200

application/json

Successful Response

tools

Tools · object[]

required

cached

boolean

required

fetched\_at

string<date-time> | null

required

server\_icon\_url

string | null