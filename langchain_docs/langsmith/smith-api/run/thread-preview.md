---
title: "Thread preview - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/thread-preview
scraped_at: 2026-11-15T03:41:41.237726
word_count: 66
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

thread\_id

string

required

#### Query Parameters

session\_id

string<uuid>

required

select

enum<string>[] | null

Enum for thread messages format types.

Available options:

`all_messages`,

`human_ai_pairs`,

`first_human_last_ai`

variables

string[] | null

#### Response

200

application/json

Successful Response

Response to preview a thread.

thread\_id

string

required

previews

Previews · object

required

Show child attributes