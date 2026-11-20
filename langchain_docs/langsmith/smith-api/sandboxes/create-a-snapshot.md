---
title: "Create a snapshot - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/create-a-snapshot
scraped_at: 2026-11-15T03:41:46.887516
word_count: 392
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

docker\_image

string

required

fs\_capacity\_bytes

integer

required

name

string

required

description

string

Description says what this snapshot's image can do, so a caller can hand it to an agent as a capability summary. At most 1024 characters.

Maximum string length: `1024`

labels

object

Labels seed the snapshot's labels, overriding any label of the same key derived from the Docker image.

Show child attributes

registry\_id

string

run\_config

object

RunConfig overrides the runtime configuration taken from the Docker image.
Every sandbox created from the snapshot runs as the image's USER, in its
WORKDIR, with its ENV beneath the sandbox's own env\_vars; user and
work\_dir given here replace the image's, and env\_vars merge over it.

Show child attributes

tag

string

mutable Docker-style tag; defaults to "latest"

#### Response

201

application/json

Created

created\_at

string

created\_by

string

description

string

Description says what this snapshot's image can do, so a caller can hand it to an agent as a capability summary.

docker\_image

string

fs\_capacity\_bytes

integer

fs\_used\_bytes

integer

id

string

image\_digest

string

included

enum<string>[]

The settings this snapshot carries, in include terms: sandboxes created from it start with each one their create request leaves unset. Env var values are never returned.

Available options:

`mounts`,

`proxy_config`,

`env_vars`,

`resources`,

`lifecycle`,

`labels`

labels

object

Show child attributes

memory\_snapshot\_size\_bytes

integer

MemorySnapshotSizeBytes is non-nil iff the snapshot was captured with
VM memory state. A non-nil value is the canonical signal that this
snapshot can warm-restore from memory; nil means rootfs only.

mount\_config

object

The mount\_config sandboxes created from this snapshot start with when their create request has none, with secret values redacted. Present only on snapshots captured with include "mounts" or "all" from a sandbox that had mounts.

Show child attributes

name

string

proxy\_config

object

The proxy\_config sandboxes created from this snapshot start with when their create request has none, with secret values redacted. Present only on snapshots captured with include "proxy\_config" or "all".

Show child attributes

registry\_id

string

run\_config

object

RunConfig is what sandboxes from this snapshot boot with. Absent on
snapshots built before it was recorded, which run as root with their own env.

Show child attributes

source\_sandbox\_id

string

status

string

status\_message

string

tags

string[]

Tags currently resolving to this snapshot, under Name. A snapshot with no
tags is dangling — addressable only by id.

updated\_at

string