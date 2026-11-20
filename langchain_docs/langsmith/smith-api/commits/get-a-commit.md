---
title: "Get a commit - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/commits/get-a-commit
scraped_at: 2026-11-15T03:40:45.352309
word_count: 88
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

owner

string

required

Repository owner (tenant handle) or '-' for private repos

repo

string

required

Repository handle

commit

string

required

Commit hash, tag, or 'latest'

#### Query Parameters

get\_examples

boolean

default:false

include

string

Comma-separated list of optional fields: "model", "is\_draft"

include\_model

boolean

default:false

Deprecated: use Include instead

is\_view

boolean

default:false

#### Response

200

application/json

OK

commit\_hash

string

description

string

examples

object[]

Show child attributes

is\_draft

boolean

manifest

object

model\_config

object

model\_provider

string