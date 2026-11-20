---
title: "Get a browser (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/get-a-browser-beta
scraped_at: 2026-11-15T03:41:49.641888
word_count: 68
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

attachments

object[]

Attachments are listed only while the browser is running.

Show child attributes

hidpi

boolean

HiDPI reports whether pages render at twice the resolution. It is
reported only while the browser is running.

id

string

name

string

status

string