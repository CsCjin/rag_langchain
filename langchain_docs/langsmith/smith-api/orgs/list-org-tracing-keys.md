---
title: "List org tracing keys - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/list-org-tracing-keys
scraped_at: 2026-11-15T03:41:24.717801
word_count: 55
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

workspace\_ids

string<uuid>[]

page\_size

integer

default:50

Required range: `1 <= x <= 100`

cursor

string | null

Maximum string length: `1024`

#### Response

200

application/json

Successful Response

items

APIKeyGetResponse · object[]

required

Show child attributes

next\_cursor

string | null

required