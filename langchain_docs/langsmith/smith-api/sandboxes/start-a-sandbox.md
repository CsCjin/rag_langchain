---
title: "Start a sandbox - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/start-a-sandbox
scraped_at: 2026-11-15T03:41:54.088864
word_count: 237
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

Sandbox display name

#### Body

application/json

discard\_memory

boolean

DiscardMemory cold-boots the sandbox, discarding any memory saved when it stopped.

volumes

object[]

Volumes, when present, replaces the attached volumes. A start whose volumes differ from those the sandbox's saved memory was captured with fails unless discard\_memory is set.

Maximum array length: `4`

Show child attributes

#### Response

202

application/json

Accepted

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