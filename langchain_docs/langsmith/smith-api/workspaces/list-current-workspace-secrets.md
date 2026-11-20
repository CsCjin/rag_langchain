---
title: "List current workspace secrets - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/list-current-workspace-secrets
scraped_at: 2026-11-15T03:42:21.848631
word_count: 66
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

include\_configs

boolean

default:false

If true, include the hosts each secret may be sent to.

#### Response

200

application/json

Successful Response

key

string

required

configs

SecretConfig · object[]

Hosts the secret may be sent to, with built-in defaults applied. Listed secrets include it only when include\_configs is true.

Show child attributes