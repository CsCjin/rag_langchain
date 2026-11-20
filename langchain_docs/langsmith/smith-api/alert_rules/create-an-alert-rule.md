---
title: "Create an alert rule - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/alert_rules/create-an-alert-rule
scraped_at: 2026-11-15T03:40:25.566586
word_count: 57
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

201

application/json

Alert rule created

actions

object[]

Show child attributes

rule

object

Show child attributes