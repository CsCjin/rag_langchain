---
title: "List Deployment Logs - Docs by LangChain"
url: https://docs.langchain.com/api-reference/deployments-v2/list-deployment-logs
scraped_at: 2026-11-15T03:37:59.834462
word_count: 84
---

#### Path Parameters

deployment\_id

string<uuid>

required

#### Query Parameters

start\_time

string<date-time> | null

end\_time

string<date-time> | null

order

enum<string>

default:asc

Available options:

`asc`,

`desc`

limit

integer

default:50

Required range: `1 <= x <= 1000`

offset

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

Log lines plus a pagination cursor.

logs

DeploymentLogEntry · object[]

Show child attributes

next\_offset

string | null