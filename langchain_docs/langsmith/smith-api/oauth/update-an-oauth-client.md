---
title: "Update an oauth client - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/oauth/update-an-oauth-client
scraped_at: 2026-11-15T03:41:15.019188
word_count: 73
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

id

string

required

Client UUID

#### Body

application/json

allowed\_scopes

string[]

client\_name

string

client\_uri

string

disabled

boolean

logo\_uri

string

policy\_uri

string

redirect\_uris

string[]

tos\_uri

string

#### Response

200

application/json

OK

allowed\_scopes

string[]

client\_id

string

client\_name

string

client\_type

string

client\_uri

string

created\_at

string

disabled

boolean

grant\_types

string[]

id

string

logo\_uri

string

policy\_uri

string

redirect\_uris

string[]

tos\_uri

string

updated\_at

string