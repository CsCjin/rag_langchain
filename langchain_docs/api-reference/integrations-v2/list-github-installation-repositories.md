---
title: "List Github Installation Repositories - Docs by LangChain"
url: https://docs.langchain.com/api-reference/integrations-v2/list-github-installation-repositories
scraped_at: 2026-11-15T03:38:03.894996
word_count: 77
---

#### Path Parameters

integration\_id

string<uuid>

required

GitHub integration ID.

#### Query Parameters

page\_size

integer

default:20

Maximum number of resources to return.

Required range: `1 <= x <= 100`

cursor

string | null

Opaque cursor returned by the previous page.

#### Response

200

application/json

Successful Response

A page of GitHub repositories.

items

GithubRepository · object[]

required

GitHub repositories available through the installation.

Show child attributes

next\_cursor

string | null

Opaque cursor for the next page, if one exists.