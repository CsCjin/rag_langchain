---
title: "List evaluators - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/evaluators/list-evaluators
scraped_at: 2026-11-15T03:40:53.832969
word_count: 108
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

type

string

Filter by evaluator type

name\_contains

string

Filter by name substring (also searches creator names)

tag\_value\_id

string[]

Filter by tag value IDs

feedback\_key

string

Filter by feedback key

resource\_id

string[]

Filter by resource IDs

agent\_id

string

Filter to evaluators attached to the agent's environments or tagged datasets; run\_rules then lists only those attachments

sort\_by

string

Field to sort by

sort\_by\_desc

boolean

Sort in descending order

limit

integer

default:100

Maximum number of results (1-100)

offset

integer

default:0

Offset for pagination

#### Response

200

application/json

OK

evaluators

object[]

Show child attributes

total

integer