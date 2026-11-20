---
title: "On payment method created - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/on-payment-method-created
scraped_at: 2026-11-15T03:41:26.072571
word_count: 40
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Stripe payment information.

billing\_info

StripeCustomerBillingInfo · object

required

Stripe customer billing information.

Show child attributes

setup\_intent

string

required

#### Response

200

application/json

Successful Response