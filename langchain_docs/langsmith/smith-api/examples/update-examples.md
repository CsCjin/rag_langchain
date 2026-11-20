---
title: "Update examples - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/examples/update-examples
scraped_at: 2026-11-15T03:40:56.218596
word_count: 90
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

dataset\_id

string<uuid>

required

Dataset ID

#### Body

multipart/form-data

{example\_id}

file

required

The Example update info as JSON. Can have fields 'metadata', 'split'

{example\_id}.inputs

file

The updated Example inputs as JSON

{example\_id}.outputs

file

The updated Example outputs as JSON

{example\_id}.attachments\_operations

file

JSON describing attachment operations (retain, rename)

{example\_id}.attachment.{name}

file

New file attachment named {name}

#### Response

201

application/json

Created

as\_of

string

Example:

`"2024-01-21T10:00:00.123456Z"`

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