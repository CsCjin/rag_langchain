---
title: "Create insights job config (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/create-insights-job-config-beta
scraped_at: 2026-11-15T03:42:08.595538
word_count: 96
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

#### Body

application/json

Request to create an Insights job configuration.

name

string

required

Maximum string length: `255`

config

CreateRunClusteringJobRequest · object

required

Configuration for an Insights job.

Show child attributes

description

string | null

schedule\_cron

string | null

#### Response

200

application/json

Successful Response

An Insights job configuration.

id

string<uuid>

required

name

string

required

description

string | null

required

config

SavedRunClusteringJobRequest · object

required

Saved configuration for an Insights job.

Show child attributes

schedule\_cron

string | null