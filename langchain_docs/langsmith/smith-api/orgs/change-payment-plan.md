---
title: "Change payment plan - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/change-payment-plan
scraped_at: 2026-11-15T03:41:17.561342
word_count: 74
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Change payment plan schema.

tier

enum<string>

required

Enum for payment plans that the user can change to. Developer plans are permanent and enterprise plans will be changed manually.

Available options:

`disabled`,

`developer`,

`developer_01_2026`,

`developer_07_2026`,

`developer_10_2026`,

`plus`,

`plus_01_2026`,

`plus_07_2026`,

`plus_10_2026`,

`startup`,

`startup_v0`,

`startup_07_2026`,

`startup_10_2026`,

`partner`,

`premier`,

`free`,

`free_07_2026`,

`free_10_2026`

display\_name

string | null

#### Response

200

application/json

Successful Response