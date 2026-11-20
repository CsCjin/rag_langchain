---
title: "Get current workspace encrypted secrets - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/get-current-workspace-encrypted-secrets
scraped_at: 2026-11-15T03:42:20.173616
word_count: 64
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

service

enum<string>

required

Service requesting encrypted secrets

Available options:

`agent_builder`,

`polly`

key\_names

string[] | null

Optional list of workspace secret keys to return

expand\_iam\_role

boolean

default:false

If true, expand AWS\_IAM\_ROLE\_ARN into temporary credentials via STS

#### Response

200

application/json

Successful Response

encrypted\_secrets

string

required

tenant\_id

string<uuid> | null