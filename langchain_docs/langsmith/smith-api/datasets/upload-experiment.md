---
title: "Upload experiment - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/upload-experiment
scraped_at: 2026-11-15T03:40:52.647504
word_count: 117
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Class for uploading the results of an already-run experiment.

experiment\_name

string

required

results

ExperimentResultRow · object[]

required

Show child attributes

experiment\_start\_time

string<date-time>

required

experiment\_end\_time

string<date-time>

required

tag\_value\_ids

string<uuid>[] | null

Maximum array length: `100`

experiment\_description

string | null

dataset\_id

string<uuid> | null

dataset\_name

string | null

dataset\_description

string | null

summary\_experiment\_scores

FeedbackCreateCoreSchema · object[] | null

Show child attributes

experiment\_metadata

Experiment Metadata · object | null

#### Response

200

application/json

Successful Response

Class for uploading the results of an already-run experiment.

dataset

Dataset · object

required

Dataset schema.

Show child attributes

experiment

TracerSession · object

required

TracerSession schema.

Show child attributes