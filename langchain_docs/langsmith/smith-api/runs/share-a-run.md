---
title: "Share a run - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/runs/share-a-run
scraped_at: 2026-11-15T03:41:44.601652
word_count: 60
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

run\_id

string<uuid>

required

Run UUID

#### Body

application/json

session\_id

string<uuid>

required

session\_id is the tracing project UUID containing the trace.

Example:

`"018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"`

trace\_id

string<uuid>

required

trace\_id is the root trace UUID to share.

Example:

`"018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"`

#### Response

200

application/json

OK

share\_token

string<uuid>

Example:

`"018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"`