---
title: "Hard delete examples - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/examples/hard-delete-examples
scraped_at: 2026-11-15T03:40:55.372926
word_count: 70
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

example\_ids

string[]

required

ExampleIDs is a list of UUIDs identifying the examples to delete.

Required array length: `1 - 1000` elements

hard\_delete

boolean

required

HardDelete indicates whether to perform a hard delete.
Currently only True is supported.

#### Response

200

application/json

OK

count

integer

Example:

`1`

example\_ids

string[]

Example:

```
[
  "[\"123e4567-e89b-12d3-a456-426614174000\"]"
]
```