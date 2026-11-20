---
title: "List Github Installations - Docs by LangChain"
url: https://docs.langchain.com/api-reference/integrations-v2/list-github-installations
scraped_at: 2026-11-15T03:38:03.998784
word_count: 70
---

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

A page of GitHub App installations.

items

GithubIntegration · object[]

required

GitHub App installations available to the workspace.

Show child attributes

next\_cursor

string | null

Opaque cursor for the next page, if one exists.