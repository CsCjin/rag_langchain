---
title: "Open a tab in a browser window (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/open-a-tab-in-a-browser-window-beta
scraped_at: 2026-11-15T03:41:53.208146
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

attachment\_id

string

required

Attachment ID

#### Body

application/json

url

string

URL to open; about:blank when empty.

#### Response

201

application/json

Created

id

string

title

string

url

string