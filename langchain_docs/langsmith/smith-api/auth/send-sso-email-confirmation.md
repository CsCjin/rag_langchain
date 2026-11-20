---
title: "Send SSO email confirmation - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/auth/send-sso-email-confirmation
scraped_at: 2026-11-15T03:40:37.893147
word_count: 59
---

#### Authorizations

Authorization

string

header

required

Bearer tokens are used to authenticate from the UI. Must also specify x-tenant-id or x-organization-id (for org scoped apis).

#### Body

application/json

email

string

required

saml\_provider\_id

string<uuid>

required

#### Response

202

application/json

Successful Response

The response is of type `Response Send Sso Email Confirmation Api V1 Sso Email Verification Send Post · object`.