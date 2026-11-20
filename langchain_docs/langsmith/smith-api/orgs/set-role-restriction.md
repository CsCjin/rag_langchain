---
title: "Set role restriction - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/set-role-restriction
scraped_at: 2026-11-15T03:41:27.416504
word_count: 61
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

role\_id

string<uuid>

required

#### Body

application/json

is\_restricted

boolean

required

#### Response

200

application/json

Successful Response

id

string<uuid>

required

name

string

required

display\_name

string

required

description

string

required

permissions

string[]

required

organization\_id

string<uuid> | null

access\_scope

enum<string> | null

Available options:

`organization`,

`workspace`

is\_restricted

boolean

default:false