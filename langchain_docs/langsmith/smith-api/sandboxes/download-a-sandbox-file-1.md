---
title: "Download a sandbox file - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/download-a-sandbox-file-1
scraped_at: 2026-11-15T03:41:48.711079
word_count: 55
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Headers

Range

string

Byte range to return, e.g. bytes=0-1023

#### Path Parameters

sandbox\_id

string

required

Sandbox ID or name

#### Query Parameters

path

string

required

File path to download

#### Response

200

application/octet-stream

File content

The response is of type `file`.