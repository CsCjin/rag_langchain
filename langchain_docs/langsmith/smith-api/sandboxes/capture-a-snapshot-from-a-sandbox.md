---
title: "Capture a snapshot from a sandbox - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/capture-a-snapshot-from-a-sandbox
scraped_at: 2026-11-15T03:41:45.520815
word_count: 648
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

name

string

required

checkpoint

string

if omitted, creates a fresh checkpoint from the running VM

confirm\_allow\_snapshot\_secret\_values

boolean

Must be true when the included settings hold literal secret values (opaque values rather than workspace secret references, and any env var value), acknowledging that the snapshot stores them and every sandbox created from it can use them.

description

string

Description says what this snapshot's image can do, so a caller can hand it to an agent as a capability summary. At most 1024 characters.

Maximum string length: `1024`

docker\_image

string

sandbox-local Docker image to export

fs\_capacity\_bytes

integer

required for Docker image export unless the sandbox has a capacity

image\_config

object

ImageConfig sets the command and ports the snapshot records, as a Docker image's ENTRYPOINT, CMD and EXPOSE do. By default a capture keeps
those of the snapshot the sandbox was created from; each field given here replaces that one, and an empty list clears it. A function
serving the snapshot runs this command and listens on its one exposed port.

Show child attributes

include

enum<string>[]

Sandbox settings to carry into the snapshot. Sandboxes created from it start with each carried setting their create request leaves unset: "mounts" (the mount\_config, with its auth), "proxy\_config", "env\_vars", "resources" (CPU and memory), "lifecycle" (idle\_ttl\_seconds, delete\_after\_stop\_seconds, preserve\_memory\_on\_stop), and "labels" (merged under this request's labels; reserved com.langchain.\* labels are left out). "all" names every one of these. VM memory is captured with include\_memory, not here. Warning: mounts, proxy\_config and env\_vars carry the sandbox's credentials, and every sandbox created from the snapshot can use them.

Available options:

`all`,

`mounts`,

`proxy_config`,

`env_vars`,

`resources`,

`lifecycle`,

`labels`

include\_memory

boolean

IncludeMemory, when true, captures a full VM memory snapshot
alongside the filesystem clone. Only honored when the sandbox is running
AND Checkpoint is omitted (i.e. a fresh in-VM checkpoint is requested).
Defaults to false to keep snapshots small unless memory restore is
explicitly desired.

labels

object

Labels seed the captured snapshot's labels.

Show child attributes

run\_config

object

RunConfig overrides the runtime configuration the snapshot carries: for a
docker\_image export, the image's USER, WORKDIR and ENV; for a capture of
the running VM, the sandbox's own. user and work\_dir replace, env\_vars
merge.

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