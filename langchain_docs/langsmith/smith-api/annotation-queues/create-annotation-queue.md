---
title: "Create annotation queue - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/create-annotation-queue
scraped_at: 2026-11-15T03:40:27.870751
word_count: 151
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

AnnotationQueue schema.

name

string

required

description

string | null

created\_at

string<date-time>

updated\_at

string<date-time>

num\_reviewers\_per\_item

integer | null

default:1

enable\_reservations

boolean | null

default:true

reservation\_minutes

integer | null

default:1

reviewer\_access\_mode

string

default:any

id

string<uuid>

default\_dataset

string<uuid> | null

rubric\_items

AnnotationQueueRubricItemSchema · object[] | null

Show child attributes

rubric\_instructions

string | null

session\_ids

string<uuid>[] | null

metadata

Metadata · object | null

#### Response

200

application/json

Successful Response

AnnotationQueue schema.

name

string

required

id

string<uuid>

required

tenant\_id

string<uuid>

required

queue\_type

enum<string>

required

Available options:

`single`,

`pairwise`

description

string | null

created\_at

string<date-time>

updated\_at

string<date-time>

num\_reviewers\_per\_item

integer | null

default:1

enable\_reservations

boolean | null

default:true

reservation\_minutes

integer | null

default:1

reviewer\_access\_mode

string

default:any

source\_rule\_id

string<uuid> | null

run\_rule\_id

string<uuid> | null

default\_dataset

string<uuid> | null

metadata

Metadata · object | null

assigned\_reviewers

AssignedReviewerSchema · object[]

Show child attributes