---
title: "List a sandbox's shared service urls - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/list-a-sandboxs-shared-service-urls
scraped_at: 2026-11-15T03:41:51.609840
word_count: 110
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

page\_size

integer

default:20

Number of results per page

cursor

string

Opaque pagination cursor from a prior response's next\_cursor

#### Response

200

application/json

OK

items

object[]

required

This page of the ports the sandbox is shared on.

Show child attributes

next\_cursor

string | null

required

Cursor for the next page, or null on the last page. A non-null value is
the only signal that more pages exist. Treat it as opaque.