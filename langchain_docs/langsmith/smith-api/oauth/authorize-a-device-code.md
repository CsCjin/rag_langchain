---
title: "Authorize a device code - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/oauth/authorize-a-device-code
scraped_at: 2026-11-15T03:41:11.964748
word_count: 56
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

user\_code

string

required

User code displayed on the device

workspace\_id

string

Default workspace ID; must belong to organization and be accessible to user

#### Response

200

application/json

OK

{key}

string