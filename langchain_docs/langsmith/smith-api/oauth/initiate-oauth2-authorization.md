---
title: "Initiate OAuth2 authorization - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/oauth/initiate-oauth2-authorization
scraped_at: 2026-11-15T03:41:13.653098
word_count: 63
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

response\_type

string

required

Must be 'code'

client\_id

string

required

OAuth2 client ID

redirect\_uri

string

required

Redirect URI registered with the client

code\_challenge

string

required

PKCE code challenge

code\_challenge\_method

string

required

PKCE method, must be 'S256'

state

string

Opaque state value to prevent CSRF

#### Response

302

Found