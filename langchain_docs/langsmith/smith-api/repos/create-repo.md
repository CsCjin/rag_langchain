---
title: "Create repo - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/repos/create-repo
scraped_at: 2026-11-15T03:41:36.357659
word_count: 91
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Fields to create a repo

repo\_handle

string

required

is\_public

boolean

required

tag\_value\_ids

string<uuid>[] | null

Maximum array length: `100`

description

string | null

readme

string | null

tags

string[] | null

repo\_type

enum<string>

default:prompt

Available options:

`prompt`,

`file`,

`agent`,

`skill`

source

enum<string> | null

Available options:

`internal`,

`external`

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