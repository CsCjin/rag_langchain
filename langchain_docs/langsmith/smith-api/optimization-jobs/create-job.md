---
title: "Create job - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/optimization-jobs/create-job
scraped_at: 2026-11-15T03:41:15.235518
word_count: 97
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

repo

string

required

#### Body

application/json

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