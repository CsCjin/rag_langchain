---
title: "Clone a volume (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/clone-a-volume-beta
scraped_at: 2026-11-15T03:41:46.252330
word_count: 91
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

Source volume ID or name

#### Body

application/json

name

string

required

Name of the new volume, unique within the workspace.

Maximum string length: `255`

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