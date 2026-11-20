---
title: "Fork repo - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/repos/fork-repo
scraped_at: 2026-11-15T03:41:36.797908
word_count: 80
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

repo

string

required

#### Body

application/json

Fields to fork a repo

repo\_handle

string

required

tag\_value\_ids

string<uuid>[] | null

Maximum array length: `100`

readme

string | null

description

string | null

tags

string[] | null

is\_public

boolean | null

#### Response

200

application/json

Successful Response

repo

RepoWithLookups · object

required

All database fields for repos, plus helpful computed fields.

Show child attributes