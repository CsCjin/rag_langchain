---
title: "Exchange grant for OAuth2 tokens - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/oauth/exchange-grant-for-oauth2-tokens
scraped_at: 2026-11-15T03:41:12.579628
word_count: 79
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

multipart/form-data

grant\_type

string

required

Grant type: authorization\_code, urn:ietf:params:oauth:grant-type:device\_code, or refresh\_token

client\_id

string

required

OAuth2 client ID

code

string

Authorization code (authorization\_code grant)

code\_verifier

string

PKCE code verifier (authorization\_code grant)

redirect\_uri

string

Redirect URI (authorization\_code grant)

device\_code

string

Device code (device\_code grant)

refresh\_token

string

Refresh token (refresh\_token grant)

#### Response

200

application/json

OK

access\_token

string

expires\_in

integer

id\_token

string

refresh\_token

string

token\_type

string

workspace\_id

string