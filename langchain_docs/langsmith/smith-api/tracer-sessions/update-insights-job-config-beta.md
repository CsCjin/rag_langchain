---
title: "Update insights job config (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/update-insights-job-config-beta
scraped_at: 2026-11-15T03:42:13.133232
word_count: 101
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

config\_id

string<uuid>

required

#### Body

application/json

Request to update an Insights job configuration.

name

string | null

Maximum string length: `255`

description

string | null

config

CreateRunClusteringJobRequest · object | null

Configuration for an Insights job.

Show child attributes

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