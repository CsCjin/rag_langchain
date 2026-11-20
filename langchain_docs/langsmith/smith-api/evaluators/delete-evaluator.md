---
title: "Delete evaluator - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/evaluators/delete-evaluator
scraped_at: 2026-11-15T03:40:53.316885
word_count: 44
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

evaluator\_id

string

required

Evaluator ID

#### Query Parameters

delete\_run\_rules

boolean

When true, delete all run rules for this evaluator before deleting the evaluator

#### Response

204

No Content