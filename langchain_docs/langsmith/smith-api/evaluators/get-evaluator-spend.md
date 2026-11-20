---
title: "Get evaluator spend - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/evaluators/get-evaluator-spend
scraped_at: 2026-11-15T03:40:53.696477
word_count: 178
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

group\_by

string

Aggregation mode: 'evaluator', 'resource', or 'run\_rule'. Mutually exclusive with entity filters.

evaluator\_id

string

Filter to a specific evaluator (UUID). Mutually exclusive with group\_by.

session\_id

string

Filter to a specific project (UUID). Mutually exclusive with group\_by.

dataset\_id

string

Filter to a specific dataset (UUID). Mutually exclusive with group\_by.

resource\_id

string[]

Filter grouped results to evaluators attached to all supplied project or dataset IDs. Only valid with group\_by.

type

string

Filter grouped results by evaluator type: 'llm', 'code' or 'decision\_model'. Only valid with group\_by.

feedback\_key

string

Filter grouped results by evaluator feedback key. Only valid with group\_by.

tag\_value\_id

string[]

Filter grouped results to evaluators, projects, or datasets tagged with all supplied tag value IDs. Only valid with group\_by.

agent\_id

string

Filter grouped results to spend from evaluator attachments on the agent's environments or tagged datasets. Only valid with group\_by.

period\_start

string

required

Start of the 7-day window (YYYY-MM-DD).

#### Response

200

application/json

OK

groups

object[]

Show child attributes

period\_end

string

period\_start

string