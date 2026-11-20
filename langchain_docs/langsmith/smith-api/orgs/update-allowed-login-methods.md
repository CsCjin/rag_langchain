---
title: "Update allowed login methods - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/update-allowed-login-methods
scraped_at: 2026-11-15T03:41:27.870000
word_count: 49
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

sso\_only

boolean | null

oidc\_login\_enabled

boolean | null

#### Response

200

application/json

Successful Response

The response is of type `Response Update Allowed Login Methods Api V1 Orgs Current Login Methods Patch · object`.