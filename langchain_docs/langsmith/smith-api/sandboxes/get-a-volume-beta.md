---
title: "Get a volume (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/get-a-volume-beta
scraped_at: 2026-11-15T03:41:50.608381
word_count: 60
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

volume

string

required

Volume ID or name

#### Response

200

application/json

OK

attachments

object[]

Show child attributes

created\_at

string<date-time>

created\_by

string

description

string

id

string

labels

object

Show child attributes

name

string

size\_bytes

integer

source\_volume\_id

string

status

string

status\_message

string

updated\_at

string<date-time>

updated\_by

string