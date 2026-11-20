---
title: "Update dataset - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/update-dataset
scraped_at: 2026-11-15T03:40:51.429603
word_count: 480
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

#### Body

application/json

Update class for Dataset.

name

stringMissing · objectstringMissing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

New dataset name. Must be unique in the workspace; a name already used by another dataset returns 409. Null returns 400. Omit to keep the current name.

description

stringMissing · objectstringMissing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

New dataset description. Null clears it. Omit to keep the current description.

inputs\_schema\_definition

Inputs Schema Definition · object

JSON Schema that example inputs must match. Replaces the current inputs schema as a whole; null removes it, which returns 400 while transformations still point into inputs. Only key-value datasets support schemas. Every existing example must match the new schema, otherwise the request returns 400 with the IDs of the examples that do not, and nothing is changed. Omit to keep the current schema.

* Inputs Schema Definition
* Missing

outputs\_schema\_definition

Outputs Schema Definition · object

JSON Schema that example outputs must match. Replaces the current outputs schema as a whole; null removes it, which returns 400 while transformations still point into outputs. Only key-value datasets support schemas. Every existing example must match the new schema, otherwise the request returns 400 with the IDs of the examples that do not, and nothing is changed. Omit to keep the current schema.

* Outputs Schema Definition
* Missing

patch\_examples

Patch Examples · object | null

Example updates keyed by example ID, applied in the same transaction so existing examples can be fixed to match a new schema. Only used when the request also sets inputs\_schema\_definition, outputs\_schema\_definition, or transformations and the dataset ends up with at least one schema; otherwise it is ignored. Each update replaces the inputs, outputs, metadata, or split it sets and keeps the rest; attachment operations are ignored. An ID that is not an example in this dataset returns 404.

Show child attributes

transformations

DatasetTransformation · object

* DatasetTransformation · object[]
* Missing · object

Show child attributes

metadata

Metadata · object

Dataset metadata as a JSON object. Replaces the current metadata as a whole; keys are not merged. Send an empty object to clear it. Omit to keep the current metadata.

* Metadata
* Missing

baseline\_experiment\_id

string<uuid>Missing · objectstring<uuid>Missing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

ID of the experiment used as the baseline when comparing experiments on this dataset. Must be an experiment run on this dataset, otherwise returns 400. Null clears it. Omit to keep the current baseline.

#### Response

200

application/json

Dataset updated successfully

name

string

required

id

string<uuid>

required

tenant\_id

string<uuid>

required

description

string | null

created\_at

string<date-time>

inputs\_schema\_definition

Inputs Schema Definition · object | null

outputs\_schema\_definition

Outputs Schema Definition · object | null

externally\_managed

boolean | null

default:false

transformations

DatasetTransformation · object[] | null

Show child attributes

data\_type

enum<string> | null

default:kv

Enum for dataset data types.

Available options:

`kv`,

`llm`,

`chat`