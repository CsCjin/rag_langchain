---
title: "Auto-generate insights job config (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/auto-generate-insights-job-config-beta
scraped_at: 2026-11-15T03:42:07.604117
word_count: 85
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

Request to generate an Insights job configuration.

user\_context

User Context · object

required

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

#### Response

200

application/json

Successful Response

Generated Insights job configuration. This configuration is not saved.

summary\_prompt

string

required

name

string | null

attribute\_schemas

Attribute Schemas · object | null

Show child attributes