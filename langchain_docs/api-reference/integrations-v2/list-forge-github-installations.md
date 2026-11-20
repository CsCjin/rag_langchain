---
title: "List Forge Github Installations - Docs by LangChain"
url: https://docs.langchain.com/api-reference/integrations-v2/list-forge-github-installations
scraped_at: 2026-11-15T03:38:03.147258
word_count: 72
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

A page of Forge GitHub App installations.

items

ForgeGithubIntegration · object[]

required

Forge GitHub App installations available to the workspace.

Show child attributes

next\_cursor

string | null

Opaque cursor for the next page, if one exists.