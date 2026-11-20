---
title: "Create evaluator - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/evaluators/create-evaluator
scraped_at: 2026-11-15T03:40:53.059988
word_count: 45
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

code\_evaluator

object

Show child attributes

llm\_evaluator

object

Show child attributes

name

string

type

enum<string>

Available options:

`llm`,

`code`,

`decision_model`

#### Response

201

application/json

Created

evaluator

object

Show child attributes