---
title: "Unshare a run - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/runs/unshare-a-run
scraped_at: 2026-11-15T03:41:44.921892
word_count: 44
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

trace\_id

string<uuid>

required

Trace root UUID

#### Body

application/json

session\_id

string<uuid>

required

session\_id is the tracing project UUID containing the trace.

Example:

`"018e4c7e-a9fb-7ef0-a5b6-6ea3a82e9327"`

#### Response

204

No Content