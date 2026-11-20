---
title: "Create a sandbox - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/create-a-sandbox
scraped_at: 2026-11-15T03:41:46.699603
word_count: 724
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

access\_delegation

object

AccessDelegation lets code inside the sandbox call the LangSmith API as you, with at most the permissions granted here. Omit for no access.

Show child attributes

cpu\_millicores

integer

CPUMillicores optionally requests CPU at millicore granularity (e.g. 500 = 0.5 vCPU); takes precedence over VCPUs. Fractional (sub-vCPU) values are not available for every sandbox.

delete\_after\_stop\_seconds

integer

env\_vars

object

Show child attributes

fs\_capacity\_bytes

integer

Disk for the sandbox, in bytes; defaults to the snapshot's and cannot be smaller. A sandbox with persistent=false gets at most 16 GiB of disk per vCPU, so at most 256 GiB: omit CPU and it is derived from the disk, set it and a larger disk is rejected.

idle\_ttl\_seconds

integer

Required range: `0 <= x <= 2147483640`

labels

object

Labels are free-form key/value metadata persisted with the sandbox and returned on reads. Labels from the source snapshot are inherited unless overridden here.

Show child attributes

mem\_bytes

integer

Memory for the sandbox, in bytes. Memory is tied to CPU at 4 GiB per vCPU: omit it and it follows that ratio; set it and it must stay within 50% of the ratio for the requested CPU, so a 1 vCPU sandbox accepts 2-6 GiB. Setting memory without CPU derives the CPU from the same ratio. Maximum 64 GiB.

mount\_config

object

Show child attributes

name

string

persistent

boolean

Persistent keeps the sandbox's filesystem across stops (the default, true). Set it to false for a disposable sandbox: its writes are discarded whenever it stops, the next start boots it fresh from its snapshot, and it is never charged for storage. A sandbox that is not persistent cannot preserve memory on stop or have its filesystem captured as a snapshot (exporting a Docker image from it with docker\_image still works), and some snapshots captured from other sandboxes cannot start one; such a create is rejected.

preserve\_memory\_on\_stop

boolean

PreserveMemoryOnStop, when true, suspends the sandbox's memory on a
voluntary stop (idle timeout or explicit stop) so the next start resumes
from where it left off. Default false discards memory and keeps only the
filesystem, so the next start is a cold boot. Restarts triggered by
infrastructure maintenance always preserve memory regardless of this setting.

proxy\_config

object

Show child attributes

restore\_memory

boolean

RestoreMemory selects how the sandbox handles a snapshot's captured memory:

nil → if-present: resume from memory when the snapshot has it, else cold-boot (default).
true → always: resume from memory; rejected if the snapshot has none.
false → never: always cold-boot.

Applies to this request only.

run\_config

object

RunConfig overrides the snapshot's run config for this sandbox: user and
work\_dir replace the snapshot's, env\_vars merge over it. The result is
what the sandbox boots with, and what a snapshot captured from it carries.

Show child attributes

snapshot

string

Snapshot is a Docker-style name or name:tag reference to boot from. A bare name resolves to name:latest.

snapshot\_id

string

snapshot\_name

string

SnapshotName is a synonym for Snapshot, accepted for compatibility with clients that predate it. Set one or the other.

tag\_value\_ids

string[]

vcpus

integer

volumes

object[]

Volumes (beta) attaches existing volumes at mount paths inside the sandbox. At most 4; requires sandbox volumes to be enabled for your workspace. Attaching a volume requires being its creator or holding sandboxes:exec.

Maximum array length: `4`

Show child attributes

#### Response

201

application/json

Created

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