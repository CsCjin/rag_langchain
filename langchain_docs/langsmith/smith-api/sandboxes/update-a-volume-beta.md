---
title: "Update a volume (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/update-a-volume-beta
scraped_at: 2026-11-15T03:41:55.663523
word_count: 100
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

#### Body

application/json

description

string | null

Description replaces the description; null or an empty string clears it.

Maximum string length: `1024`

labels

object | null

Labels replaces every label; null or an empty object clears them.

Show child attributes

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