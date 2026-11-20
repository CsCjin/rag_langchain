---
title: "Optimize prompt job - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/repos/optimize-prompt-job
scraped_at: 2026-11-15T03:41:37.498144
word_count: 57
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Request to optimize a prompt.

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

prompt\_name

string

required

#### Response

200

application/json

Successful Response

Response from optimizing a prompt.

optimization\_job\_id

string<uuid>

required