---
title: "Set company info - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/set-company-info
scraped_at: 2026-11-15T03:41:27.120686
word_count: 54
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

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

#### Response

200

application/json

Successful Response