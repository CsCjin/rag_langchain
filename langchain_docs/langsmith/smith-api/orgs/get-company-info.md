---
title: "Get company info - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/get-company-info
scraped_at: 2026-11-15T03:41:21.444184
word_count: 52
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Response

200 - application/json

Successful Response

company\_info

StripeBusinessBillingInfo · object | null

Stripe customer billing information.

Show child attributes

tax\_id

StripeTaxId · object | null

Stripe tax ID.

Show child attributes

invoice\_email

string | null

is\_business

boolean

default:false