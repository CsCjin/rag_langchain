---
title: "Create comparative experiment - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/create-comparative-experiment
scraped_at: 2026-11-15T03:40:47.727209
word_count: 84
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Create class for ComparativeExperiment.

experiment\_ids

string<uuid>[]

required

id

string<uuid>

name

string | null

description

string | null

created\_at

string<date-time>

modified\_at

string<date-time>

reference\_dataset\_id

string<uuid> | null

extra

Extra · object | null

#### Response

200

application/json

Successful Response

ComparativeExperiment schema.

id

string<uuid>

required

tenant\_id

string<uuid>

required

created\_at

string<date-time>

required

modified\_at

string<date-time>

required

reference\_dataset\_id

string<uuid>

required

name

string | null

description

string | null

extra

Extra · object | null