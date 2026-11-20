---
title: "Stop sharing a sandbox service URL - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/stop-sharing-a-sandbox-service-url
scraped_at: 2026-11-15T03:41:54.459622
word_count: 56
---

#### Authorizations

API Key & Tenant IDBearer Auth & Tenant IDAPI Key & Tenant IDBearer Auth & Tenant ID

X-API-Key

string

header

required

X-Tenant-Id

string

header

required

#### Path Parameters

name

string

required

Sandbox name or ID

#### Query Parameters

port

integer

Port to stop sharing. Omit to stop sharing every port.

#### Response

204

deleted