---
title: "Update current org member - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/update-current-org-member
scraped_at: 2026-11-15T03:41:27.997723
word_count: 40
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

identity\_id

string<uuid>

required

#### Body

application/json

password

string | null

full\_name

string | null

role\_id

string<uuid> | null

#### Response

200

application/json

Successful Response