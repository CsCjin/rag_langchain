---
title: "Upload a sandbox file - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/upload-a-sandbox-file
scraped_at: 2026-11-15T03:41:55.822349
word_count: 50
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

sandbox\_id

string

required

Sandbox ID or name

#### Query Parameters

path

string

required

Destination file path

#### Body

multipart/form-data

file

file

required

File to upload

#### Response

200

application/json

OK

path

string

written

integer