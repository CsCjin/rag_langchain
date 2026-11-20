---
title: "Update an access policy - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/access_policies/update-an-access-policy
scraped_at: 2026-11-15T03:40:25.300482
word_count: 64
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

access\_policy\_id

string

required

Access Policy ID

#### Body

application/json

condition\_groups

object[]

Show child attributes

description

string | null

effect

string

name

string

#### Response

200

application/json

Updated access policy

condition\_groups

object[]

Show child attributes

created\_at

string

description

string

effect

string

id

string

name

string

role\_ids

string[]

updated\_at

string