---
title: "List Revisions - Docs by LangChain"
url: https://docs.langchain.com/api-reference/deployments-v2/list-revisions
scraped_at: 2026-11-15T03:38:00.389024
word_count: 116
---

#### Path Parameters

deployment\_id

string<uuid>

required

#### Query Parameters

limit

integer

default:20

Maximum number of resources to return.

Required range: `1 <= x <= 100`

offset

integer

default:0

Pagination offset. Pass this value to subsequent requests to fetch the next page of resources.

Required range: `x >= 0`

status

string | null

Comma separated list of revision `status` (CREATING, QUEUED, AWAITING\_BUILD, BUILDING, AWAITING\_DEPLOY, DEPLOYING, CREATE\_FAILED, BUILD\_FAILED, DEPLOY\_FAILED, DEPLOYED, SKIPPED, INTERRUPTED, UNKNOWN) fields to filter by.

remote\_reconciled

boolean | null

Flag to filter by remote reconciled revisions.

#### Response

200

application/json

Successful Response

resources

Revision · object[]

required

Show child attributes

offset

integer

required

Pagination offset. Pass this value to subsequent requests to fetch the next page.