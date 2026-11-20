---
title: "Create an access policy - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/access_policies/create-an-access-policy
scraped_at: 2026-11-15T03:40:23.788547
word_count: 45
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

condition\_groups

object[]

Show child attributes

description

string

effect

string

name

string

role\_ids

string[]

if present, attach to the specified roles

#### Response

201

application/json

Access policy created

id

string