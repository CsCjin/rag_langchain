---
title: "Request OAuth2 device authorization - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/oauth/request-oauth2-device-authorization
scraped_at: 2026-11-15T03:41:14.365159
word_count: 60
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

multipart/form-data

client\_id

string

required

OAuth2 client ID

#### Response

200

application/json

OK

device\_code

string

expires\_in

integer

interval

integer

user\_code

string

verification\_uri

string

verification\_uri\_complete

string

The verification URI with the user code included, so the user confirms
the code instead of typing it (RFC 8628 §3.3.1).