---
title: "List data planes for the current organization - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/data_planes/list-data-planes-for-the-current-organization
scraped_at: 2026-11-16T08:49:04.012226
word_count: 43
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

view

enum<string>

default:FULL

Response view. Specify once; omit for the full resource.

Available options:

`FULL`,

`SUMMARY`

#### Response

200

application/json

Data planes

data\_planes

object[]

Show child attributes