---
title: "Get bulk export runs filtered - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/bulk-exports/get-bulk-export-runs-filtered
scraped_at: 2026-11-15T03:40:40.053375
word_count: 101
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

source\_bulk\_export\_id

string<uuid>

required

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