---
title: "List hourly sandbox usage costs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/list-hourly-sandbox-usage-costs
scraped_at: 2026-11-15T03:41:51.843998
word_count: 253
---

#### Authorizations

API Key & Tenant IDBearer Auth & Tenant IDAPI Key & Tenant IDBearer Auth & Tenant ID

X-API-Key

string

header

required

X-Tenant-Id

string

header

required

#### Query Parameters

start\_time

string<date-time>

required

Inclusive RFC3339 start time

end\_time

string<date-time>

required

Exclusive RFC3339 end time; the range must not exceed 31 days

resource\_type

enum<string>

Resource type filter

Available options:

`SANDBOX`,

`SNAPSHOT`

resource\_ids

string[]

Resource UUID filter; repeat this parameter up to 100 times

page\_size

integer

default:20

Maximum rows to return

Required range: `1 <= x <= 100`

granularity

enum<string>

default:HOUR

HOUR returns hourly buckets. RESOURCE sums each resource over the requested interval and sets period\_start to start\_time.

Available options:

`HOUR`,

`RESOURCE`

cursor

string

Opaque pagination cursor

include\_totals

boolean

default:false

Include usage totals across the filtered interval (RESOURCE only). Omitted when unrestricted resource access cannot be verified or the service does not support totals. CLI: use --format raw to show this summary.

include\_daily

boolean

default:false

Include bounded daily physical usage for the top 10 resources per metric and Other. Requires RESOURCE and include\_totals. Omitted when unrestricted access or service support is unavailable. CLI: use --format raw to show this summary.

#### Response

200

application/json

OK

items

object[]

required

Show child attributes

next\_cursor

string | null

required

daily

object

Daily usage over the full filtered interval, independent of pagination.
Omitted unless requested, supported, and unrestricted resource access is verified.

Show child attributes

totals

object

Totals cover the entire filtered interval, independently of the cursor.
Omitted unless requested and unrestricted resource access is verified.

Show child attributes