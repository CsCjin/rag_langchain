---
title: "Get server info - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/info/get-server-info
scraped_at: 2026-11-15T03:41:04.965893
word_count: 58
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Response

200 - application/json

OK

batch\_ingest\_config

object

Show child attributes

billing\_installation\_id

string

BillingInstallationID is the persistent per-installation identity for
self-hosted deployments.

customer\_info

object

Show child attributes

engine\_github\_web\_base\_url

string<uri>

git\_sha

string

instance\_flags

object

Show child attributes

license\_expiration\_time

string

sdk\_versions

object

Show child attributes

version

string