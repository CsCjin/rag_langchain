---
title: "Evaluate experiment adhoc - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/experiments/evaluate-experiment-adhoc
scraped_at: 2026-11-15T03:40:57.983287
word_count: 56
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

experiment\_id

string<uuid>

required

#### Body

application/json

Request body for evaluating an experiment.

rule\_id

string<uuid>

required

#### Response

200

application/json

Successful Response

The response is of type `Response Evaluate Experiment Adhoc Api V1 Runs Experiments Experiment Id Evaluate Post · object`.