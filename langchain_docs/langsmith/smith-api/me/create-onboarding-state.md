---
title: "Create onboarding state - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/me/create-onboarding-state
scraped_at: 2026-11-15T03:41:09.980875
word_count: 88
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

id

string<uuid>

required

ls\_user\_id

string<uuid>

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

tracing\_completed\_at

string<date-time> | null

lgstudio\_completed\_at

string<date-time> | null

playground\_completed\_at

string<date-time> | null

evaluation\_completed\_at

string<date-time> | null

success\_viewed\_at

string<date-time> | null

agent\_platform\_welcome\_viewed\_at

string<date-time> | null

get\_started\_checklist\_dismissed\_at

string<date-time> | null

agent\_trace\_viewed\_at

string<date-time> | null

agent\_monitoring\_viewed\_at

string<date-time> | null

get\_started\_path

enum<string> | null

Available options:

`BUILD`,

`CONNECT`