---
title: "Get org usage - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/get-org-usage
scraped_at: 2026-11-15T03:41:23.209687
word_count: 61
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

starting\_on

string<date-time>

required

ending\_before

string<date-time>

required

on\_current\_plan

boolean

default:true

#### Response

200

application/json

Successful Response

customer\_id

string

required

billable\_metric\_id

string

required

billable\_metric\_name

string

required

start\_timestamp

string

required

end\_timestamp

string

required

value

number | null

required

groups

Groups · object | null

required

Show child attributes