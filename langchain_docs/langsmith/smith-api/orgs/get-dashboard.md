---
title: "Get dashboard - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/get-dashboard
scraped_at: 2026-11-15T03:41:22.806050
word_count: 61
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

type

enum<string>

required

Enum for acceptable types of dashboards.

Available options:

`invoices`,

`usage`,

`credits`

color\_scheme

enum<string> | null

required

Enum for acceptable color schemes of dashboards.

Available options:

`light`,

`dark`

#### Response

200

application/json

Successful Response

Organization dashboard for usage or invoices.

embeddable\_url

string

required