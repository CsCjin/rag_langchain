---
title: "Create section - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/charts/create-section
scraped_at: 2026-11-15T03:40:40.863703
word_count: 59
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

title

string

required

description

string | null

index

integer | null

#### Response

200

application/json

Successful Response

title

string

required

id

string<uuid>

required

description

string | null

index

integer | null

chart\_count

integer | null

created\_at

string<date-time> | null

modified\_at

string<date-time> | null