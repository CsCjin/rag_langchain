---
title: "Bulk delete evaluators - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/evaluators/bulk-delete-evaluators
scraped_at: 2026-11-15T03:40:52.969311
word_count: 50
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

evaluator\_ids

string[]

required

Evaluator IDs to delete

delete\_run\_rules

boolean

When true, delete all run rules for this evaluator before deleting the evaluator

#### Response

200

application/json

OK

failed

object[]

Show child attributes

succeeded

string[]