---
title: "Update annotation queue - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/update-annotation-queue
scraped_at: 2026-11-15T03:40:31.338290
word_count: 179
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

queue\_id

string<uuid>

required

ID of the annotation queue.

#### Body

application/json

AnnotationQueue update schema.

name

string | null

New name for the queue.

description

string | null

New description.

default\_dataset

string<uuid> | null

Dataset that reviewed runs are added to by default.

num\_reviewers\_per\_item

integerMissing · objectintegerMissing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

How many reviewers must review each run.

enable\_reservations

booleanMissing · objectbooleanMissing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

Whether a reviewer reserves a run while reviewing it, so others skip it.

reservation\_minutes

integerMissing · objectintegerMissing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

How long a reservation lasts, in minutes.

rubric\_items

AnnotationQueueRubricItemSchema · object[] | null

Feedback keys reviewers fill in for each run.

Show child attributes

rubric\_instructions

string | null

Instructions shown to reviewers.

metadata

Metadata · object

Metadata to store on the queue. Replaces the existing metadata.

* Metadata
* Missing

reviewer\_access\_mode

enum<string> | null

Who completes a run: any (one reviewer is enough) or assigned (every assigned reviewer must submit).

Available options:

`any`,

`assigned`

#### Response

200

application/json

Successful Response