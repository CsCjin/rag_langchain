---
title: "Clone dataset - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/clone-dataset
scraped_at: 2026-11-15T03:40:46.780049
word_count: 173
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

target\_dataset\_id

string<uuid>

required

ID of the dataset in this workspace that receives the copied examples. Its current examples are kept.

source\_dataset\_id

string<uuid>

required

ID of the dataset in this workspace to copy examples from. It is not modified.

as\_of

string<date-time>stringstring<date-time>string

Only modifications made on or before this time are included. If None, the latest version of the dataset is used.

examples

string<uuid>[]

IDs of source examples to copy. Defaults to every example in the source version. When IDs are given and nothing is copied, because none match or either dataset is not found, the request fails with 404.

split

stringstring[]stringstring[]

Split name, or list of split names, assigned to every copied example in place of its source splits. Defaults to keeping the source splits.

tag\_value\_ids

string<uuid>[] | null

List of resource tag value IDs to attach to the target dataset, up to 100. Requires the datasets:tag\_on\_create permission.

Maximum array length: `100`

#### Response

200

application/json

Successful Response