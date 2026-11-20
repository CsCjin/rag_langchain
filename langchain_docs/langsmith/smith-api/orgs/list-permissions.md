---
title: "List permissions - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/list-permissions
scraped_at: 2026-11-15T03:41:25.329013
word_count: 45
---

#### Authorizations

Authorization

string

header

required

Bearer tokens are used to authenticate from the UI. Must also specify x-tenant-id or x-organization-id (for org scoped apis).

#### Response

200 - application/json

Successful Response

name

string

required

description

string

required

access\_scope

enum<string>

required

Available options:

`organization`,

`workspace`