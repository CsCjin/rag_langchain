---
title: "Create a run - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/runs/create-a-run
scraped_at: 2026-11-15T03:41:42.524234
word_count: 105
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

address

string

Addresses the run to an Agent environment in place of session\_id or
session\_name, as lrn:agents/{id}/environments/{environment}. The environment is
case-insensitive. Self-hosted deployments need LangSmith v0.18 or later.

Example:

`"lrn:agents/support-agent/environments/production"`

dotted\_order

string

end\_time

string

error

string

events

object[]

extra

object

id

string

input\_attachments

object

inputs

object

name

string

output\_attachments

object

outputs

object

parent\_run\_id

string

reference\_example\_id

string

run\_type

enum<string>

Available options:

`tool`,

`chain`,

`llm`,

`retriever`,

`embedding`,

`prompt`,

`parser`

serialized

object

session\_id

string

session\_name

string

start\_time

string

status

string

tags

string[]

trace\_id

string

#### Response

202

application/json

Run created

{key}

any