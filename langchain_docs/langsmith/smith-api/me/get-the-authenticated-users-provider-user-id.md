---
title: "Get the authenticated user's provider user ID - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/me/get-the-authenticated-users-provider-user-id
scraped_at: 2026-11-15T03:41:10.622070
word_count: 35
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

providerType

string

required

Provider type (e.g. slack, github)

#### Response

200

application/json

OK

The response is of type `string`.