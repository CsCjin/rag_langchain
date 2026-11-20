---
title: "Upload examples - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/examples/upload-examples
scraped_at: 2026-11-15T03:40:56.339847
word_count: 83
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

The Example info as JSON. Can have fields 'metadata', 'split', 'use\_source\_run\_io', 'source\_run\_id', 'created\_at', 'modified\_at'

{example\_id}.inputs

file

required

The Example inputs as JSON

{example\_id}.outputs

file

THe Example outputs as JSON

{example\_id}.attachments.{name}

file

File attachment named {name}

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