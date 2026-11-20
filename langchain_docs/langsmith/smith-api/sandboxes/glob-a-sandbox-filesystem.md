---
title: "Glob a sandbox filesystem - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/glob-a-sandbox-filesystem
scraped_at: 2026-11-15T03:41:51.188146
word_count: 44
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

sandbox\_id

string

required

Sandbox ID or name

#### Body

application/json

limit

integer

path

string

pattern

string

#### Response

200

application/json

OK

matches

object[]

Show child attributes

truncated

boolean