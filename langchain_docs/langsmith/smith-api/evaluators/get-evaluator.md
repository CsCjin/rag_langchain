---
title: "Get evaluator - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/evaluators/get-evaluator
scraped_at: 2026-11-15T03:40:53.500387
word_count: 93
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

#### Response

200

application/json

OK

code\_evaluator

object

Show child attributes

created\_at

string

created\_by

string

feedback\_keys

string[]

id

string

is\_managed

boolean

IsManaged marks a LangChain Tuned Evaluator (currently the tuned
Perceived Error judge). NULL in the DB is read as false via COALESCE.

llm\_evaluator

object

Embedded child evaluator (populated based on type)

Show child attributes

name

string

run\_rules

object[]

Show child attributes

tenant\_id

string

type

enum<string>

Available options:

`llm`,

`code`,

`decision_model`

updated\_at

string