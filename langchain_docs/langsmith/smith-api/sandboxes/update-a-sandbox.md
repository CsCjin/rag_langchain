---
title: "Update a sandbox - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/update-a-sandbox
scraped_at: 2026-11-15T03:41:55.488013
word_count: 274
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

Current sandbox display name

#### Body

application/json

cpu\_millicores

integer

delete\_after\_stop\_seconds

integer

fs\_capacity\_bytes

integer

idle\_ttl\_seconds

integer

Required range: `0 <= x <= 2147483640`

mem\_bytes

integer

New memory for the sandbox, in bytes. The 4 GiB per vCPU ratio applies when the sandbox is created; a resize enforces only the maximum of 64 GiB.

name

string

proxy\_config

object

Show child attributes

run\_config

object

RunConfig changes what subsequent commands run with: user and work\_dir
replace the current values, env\_vars merge over them. Commands already
running are unaffected.

Show child attributes

tag\_value\_ids

string[]

vcpus

integer

#### Response

200

application/json

OK

access\_delegation

object

AccessDelegation is the LangSmith access this sandbox was granted, absent when it has none. It is reported exactly as it was requested at create.

Show child attributes

cpu\_millicores

integer

created\_at

string

created\_by

string

dataplane\_url

string

delete\_after\_stop\_seconds

integer

fs\_capacity\_bytes

integer

id

string

idle\_ttl\_seconds

integer

labels

object

Show child attributes

mem\_bytes

integer

mount\_config

object

Show child attributes

name

string

persistent

boolean

Persistent reports whether the sandbox keeps its filesystem across stops. When false, its writes are discarded whenever it stops and it is not charged for storage.

preserve\_memory\_on\_stop

boolean

proxy\_config

object

Show child attributes

run\_config

object

RunConfig is what the sandbox's commands run with: the user, working directory and base env beneath env\_vars.

Show child attributes

size\_class

string

snapshot\_id

string

status

string

status\_message

string

stopped\_at

string

updated\_at

string

updated\_by

string

vcpus

integer

volumes

object[]

Volumes (beta) are the volumes attached to the sandbox, in slot order. Absent when the workspace does not have sandbox volumes enabled.

Show child attributes