---
title: "Create an oauth client - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/oauth/create-an-oauth-client
scraped_at: 2026-11-15T03:41:12.193935
word_count: 49
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

allowed\_scopes

string[]

client\_name

string

client\_type

string

"public" or "confidential"

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

tos\_uri

string

#### Response

201

application/json

Created

client

object

Show child attributes

client\_secret

string