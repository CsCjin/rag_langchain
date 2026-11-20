---
title: "Update an alert rule - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/alert_rules/update-an-alert-rule
scraped_at: 2026-11-15T03:40:26.544299
word_count: 55
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

session\_id

string

required

Session ID

alert\_rule\_id

string

required

Alert rule ID

#### Body

application/json

actions

object[]

required

Minimum array length: `1`

Show child attributes

rule

object

required

Show child attributes

#### Response

200

application/json

Alert rule updated

{key}

any