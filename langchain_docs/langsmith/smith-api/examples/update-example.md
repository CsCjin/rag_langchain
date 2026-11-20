---
title: "Update example - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/examples/update-example
scraped_at: 2026-11-15T03:40:57.131127
word_count: 128
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

example\_id

string<uuid>

required

#### Body

application/json

Update class for Example.

dataset\_id

string<uuid> | null

The example's current dataset. An example can't move to another dataset.

inputs

Inputs · object | null

New inputs. Replaces the existing inputs; omit to keep them.

outputs

Outputs · object | null

New outputs. Replaces the existing outputs; omit to keep them.

attachments\_operations

AttachmentsOperations · object | null

Attachments to rename or keep.

Show child attributes

metadata

Metadata · object | null

New metadata. Replaces the existing metadata; omit to keep it.

split

string[]stringstring[]string

Split or splits to put the example in. Replaces its current splits.

overwrite

boolean

default:false

Not used.

#### Response

200

application/json

Successful Response