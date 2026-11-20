---
title: "Create log - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/optimization-jobs/create-log
scraped_at: 2026-11-15T03:41:15.335360
word_count: 73
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

job\_id

string<uuid>

required

#### Body

application/json

log\_type

enum<string>

required

Available options:

`info`,

`result`,

`error`,

`link`

message

string

required

data

Data · object | null

#### Response

200

application/json

Successful Response

log\_type

enum<string>

required

Available options:

`info`,

`result`,

`error`,

`link`

message

string

required

id

string<uuid>

required

job\_id

string<uuid>

required

created\_at

string<date-time>

required

data

Data · object | null