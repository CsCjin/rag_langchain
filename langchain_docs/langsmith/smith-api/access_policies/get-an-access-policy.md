---
title: "Get an access policy - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/access_policies/get-an-access-policy
scraped_at: 2026-11-15T03:40:24.509377
word_count: 48
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

#### Response

200

application/json

Access policy details

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