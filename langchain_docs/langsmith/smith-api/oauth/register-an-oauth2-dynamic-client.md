---
title: "Register an OAuth2 dynamic client - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/oauth/register-an-oauth2-dynamic-client
scraped_at: 2026-11-15T03:41:14.166699
word_count: 63
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

client\_name

string

client\_uri

string

grant\_types

string[]

logo\_uri

string

policy\_uri

string

redirect\_uris

string[]

response\_types

string[]

scope

string

token\_endpoint\_auth\_method

string

tos\_uri

string

#### Response

201

application/json

Created

client\_id

string

client\_id\_issued\_at

integer

client\_name

string

client\_uri

string

grant\_types

string[]

logo\_uri

string

policy\_uri

string

redirect\_uris

string[]

response\_types

string[]

token\_endpoint\_auth\_method

string

tos\_uri

string