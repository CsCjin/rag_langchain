---
title: "Load a browser's extensions (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/load-a-browsers-extensions-beta
scraped_at: 2026-11-15T03:41:52.727035
word_count: 50
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

name

string

required

Browser name or ID

#### Response

200

application/json

OK

loaded

string[]

Loaded are the ids of the extensions this call loaded; empty when Chrome
already had every extension in the directory.