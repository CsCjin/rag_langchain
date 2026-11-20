---
title: "Update job - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/optimization-jobs/update-job
scraped_at: 2026-11-15T03:41:16.603701
word_count: 97
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

job\_id

string<uuid>

required

#### Body

application/json

status

enum<string> | null

Available options:

`created`,

`running`,

`successful`,

`failed`

result

PromptOptimizationResult · object | null

Show child attributes

#### Response

200

application/json

Successful Response

id

string<uuid>

required

repo\_id

string<uuid>

required

status

enum<string>

required

Available options:

`created`,

`running`,

`successful`,

`failed`

tenant\_id

string<uuid>

required

algorithm

enum<string>

required

Available options:

`promptim`,

`demo`

config

PromptimConfig · object

required

* PromptimConfig
* DemoConfig

Show child attributes

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

results

PromptOptimizationResult · object[]

Show child attributes