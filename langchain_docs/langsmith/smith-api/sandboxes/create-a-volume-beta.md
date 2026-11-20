---
title: "Create a volume (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/create-a-volume-beta
scraped_at: 2026-11-15T03:41:47.091413
word_count: 91
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

name

string

required

Name is unique within the workspace.

Maximum string length: `255`

size\_bytes

integer

required

SizeBytes is the volume's capacity, rounded up to a whole GiB.

description

string

Maximum string length: `1024`

labels

object

Show child attributes

#### Response

201

application/json

Created

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