---
title: "Delete tracer session - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/delete-tracer-session
scraped_at: 2026-11-15T03:42:09.664363
word_count: 30
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

session\_id

string<uuid>

required

#### Response

202

Deletion accepted; background cleanup may still be running.