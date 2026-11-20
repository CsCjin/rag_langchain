---
title: "Get insights job configs (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/get-insights-job-configs-beta
scraped_at: 2026-11-15T03:42:09.916547
word_count: 45
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

session\_id

string<uuid>

required

#### Query Parameters

include\_prebuilts

boolean

default:false

#### Response

200

application/json

Successful Response

A collection of Insights job configurations.

configs

ClusteringJobConfigResponse · object[]

required

Show child attributes