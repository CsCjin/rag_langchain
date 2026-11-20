---
title: "Approve OAuth2 authorization request - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/oauth/approve-oauth2-authorization-request
scraped_at: 2026-11-15T03:41:11.867829
word_count: 94
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

multipart/form-data

organization\_id

string

required

Organization ID; must match the authenticated org

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

workspace\_id

string

Default workspace ID; must belong to organization and be accessible to user

state

string

Opaque state value to prevent CSRF

#### Response

200

application/json

JSON body with redirect\_uri the frontend should navigate the browser to

{key}

string