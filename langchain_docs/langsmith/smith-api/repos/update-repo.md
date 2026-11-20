---
title: "Update repo - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/repos/update-repo
scraped_at: 2026-11-15T03:41:37.651670
word_count: 77
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

Fields to update a repo

description

string | null

readme

string | null

tags

string[] | null

is\_public

boolean | null

is\_archived

boolean | null

restricted\_mode

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