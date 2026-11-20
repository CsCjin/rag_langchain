---
title: "Clone section - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/charts/clone-section
scraped_at: 2026-11-15T03:40:40.550788
word_count: 56
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

section\_id

string<uuid> | null

session\_id

string<uuid> | null

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