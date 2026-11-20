---
title: "Proxy - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/mcp/proxy
scraped_at: 2026-11-15T03:41:08.063551
word_count: 65
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

url

string

required

method

enum<string>

default:GET

Available options:

`GET`,

`POST`,

`PUT`,

`DELETE`,

`PATCH`,

`HEAD`,

`OPTIONS`

headers

Headers · object | null

Show child attributes

timeout

integer | null

default:120

body

unknown

oauth\_provider\_id

string | null

ls\_user\_id

string | null

agent\_id

string | null

#### Response

200

application/json

Successful Response