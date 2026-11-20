---
title: "Get annotation queues for run - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-annotation-queues-for-run
scraped_at: 2026-11-15T03:40:29.825157
word_count: 96
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

run\_id

string<uuid>

required

ID of the run.

#### Response

200

application/json

Successful Response

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