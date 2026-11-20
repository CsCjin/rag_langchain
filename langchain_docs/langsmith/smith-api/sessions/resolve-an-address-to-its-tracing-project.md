---
title: "Resolve an address to its tracing project - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sessions/resolve-an-address-to-its-tracing-project
scraped_at: 2026-11-15T03:41:57.996805
word_count: 92
---

#### Authorizations

API Key & Tenant IDBearer Auth & Tenant IDAPI Key & Tenant IDBearer Auth & Tenant ID

X-API-Key

string

header

required

X-Tenant-Id

string

header

required

#### Query Parameters

kind

enum<string>

required

The kind of address.

Available options:

`AGENT`,

`EXPERIMENT`,

`EVALUATOR`

id

string

The Agent's user-assigned id for AGENT, or the experiment's id for EXPERIMENT. Not set for EVALUATOR.

environment

enum<string>

The Agent environment. Only set for AGENT.

Available options:

`LOCAL`,

`DEVELOPMENT`,

`STAGING`,

`PRODUCTION`

#### Response

200

application/json

OK

session\_id

string<uuid>

required

`session_id` is the tracing project (session) the address names.