---
title: "Get bulk export runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/bulk-exports/get-bulk-export-runs
scraped_at: 2026-11-15T03:40:39.840217
word_count: 104
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

bulk\_export\_id

string<uuid>

required

#### Query Parameters

limit

integer | null

Required range: `1 <= x <= 1000`

offset

integer

default:0

Required range: `x >= 0`

#### Response

200

application/json

Successful Response

bulk\_export\_id

string<uuid>

required

metadata

BulkExportRunMetadata · object

required

Show child attributes

id

string<uuid>

required

status

enum<string>

required

Available options:

`Cancelled`,

`Completed`,

`Created`,

`Failed`,

`TimedOut`,

`Running`

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

finished\_at

string<date-time> | null

required

session\_id

string<uuid> | null

retry\_number

integer

default:0

errors

Errors · object | null

start\_time

string<date-time> | null

end\_time

string<date-time> | null