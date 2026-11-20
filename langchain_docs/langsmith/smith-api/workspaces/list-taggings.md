---
title: "List taggings - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/list-taggings
scraped_at: 2026-11-15T03:42:22.660837
word_count: 46
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

tag\_value\_id

string<uuid> | null

#### Response

200

application/json

Successful Response

tag\_key

string

required

tag\_key\_id

string<uuid>

required

tag\_value

string

required

tag\_value\_id

string<uuid>

required

resources

TaggingsByResourceType · object

required

Show child attributes