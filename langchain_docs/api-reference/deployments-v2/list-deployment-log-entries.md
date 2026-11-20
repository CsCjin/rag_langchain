---
title: "List Deployment Log Entries - Docs by LangChain"
url: https://docs.langchain.com/api-reference/deployments-v2/list-deployment-log-entries
scraped_at: 2026-11-15T03:37:59.652650
word_count: 90
---

#### Query Parameters

deployment\_id

string<uuid>

required

revision\_id

string<uuid> | null

log\_type

enum<string>

default:DEPLOY

Available options:

`BUILD`,

`DEPLOY`

start\_time

string<date-time> | null

end\_time

string<date-time> | null

sort\_order

enum<string>

default:asc

Available options:

`asc`,

`desc`

page\_size

integer

default:20

Required range: `1 <= x <= 100`

cursor

string | null

query

string | null

Maximum string length: `1000`

level

enum<string> | null

Available options:

`DEBUG`,

`INFO`,

`WARNING`,

`ERROR`,

`CRITICAL`

run\_id

string | null

#### Response

200

application/json

Successful Response

Canonical cursor-paginated deployment-log collection.

items

DeploymentLogEntry · object[]

Show child attributes

next\_cursor

string | null