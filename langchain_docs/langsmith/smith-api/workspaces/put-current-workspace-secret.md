---
title: "Put current workspace secret - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/put-current-workspace-secret
scraped_at: 2026-11-15T03:42:24.369516
word_count: 122
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

key

string

required

#### Body

application/json

value

string | null

Secret value. Required to create a secret; omit to keep the current value.

Minimum string length: `1`

configs

SecretConfigInput · object[] | null

Full replacement of the allowed hosts. Omitted or empty removes custom hosts so the built-in defaults, if any, apply.

Show child attributes

#### Response

200

application/json

Successful Response

A workspace secret's key and the hosts it may be sent to. Never the value.

key

string

required

configs

SecretConfig · object[]

Hosts the secret may be sent to, with built-in defaults applied. Listed secrets include it only when include\_configs is true.

Show child attributes