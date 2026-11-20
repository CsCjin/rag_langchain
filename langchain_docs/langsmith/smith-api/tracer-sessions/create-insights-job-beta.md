---
title: "Create insights job (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/create-insights-job-beta
scraped_at: 2026-11-15T03:42:08.399183
word_count: 133
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

session\_id

string<uuid>

required

#### Body

application/json

Configuration for an Insights job.

config\_id

string<uuid> | null

start\_time

string<date-time> | null

end\_time

string<date-time> | null

last\_n\_hours

integer | null

hierarchy

integer[] | null

partitions

Partitions · object | null

Show child attributes

sample

numberintegernumberinteger

summary\_prompt

string | null

filter

string | null

name

string | null

attribute\_schemas

Attribute Schemas · object | null

user\_context

User Context · object | null

Show child attributes

model

enum<string>

default:openai

Available options:

`openai`,

`anthropic`

cluster\_model

string | null

summary\_model

string | null

is\_scheduled

boolean

default:false

validate\_model\_secrets

boolean

default:true

#### Response

200

application/json

Successful Response

An Insights job queued for execution.

id

string<uuid>

required

name

string

required

status

string

required

error

string | null