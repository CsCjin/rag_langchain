---
title: "Search Crons - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/crons/search-crons
scraped_at: 2026-11-15T03:38:11.382205
word_count: 275
---

#### Body

application/json

Payload for listing crons

assistant\_id

string<uuid>

The assistant ID or graph name to filter by using exact match.

thread\_id

string<uuid>

The thread ID to search for.

enabled

boolean

Filter by enabled status. If not provided, returns both enabled and disabled crons.

metadata

Metadata · object

Metadata to filter by. Exact match filter for each KV pair.

limit

integer

default:10

The maximum number of results to return.

Required range: `1 <= x <= 1000`

offset

integer

default:0

The number of results to skip.

Required range: `x >= 0`

sort\_by

enum<string>

default:created\_at

The field to sort by.

Available options:

`cron_id`,

`assistant_id`,

`thread_id`,

`next_run_date`,

`end_time`,

`created_at`,

`updated_at`

sort\_order

enum<string>

default:desc

The order to sort by.

Available options:

`asc`,

`desc`

select

enum<string>[]

Specify which fields to return. If not provided, all fields are returned.

Available options:

`cron_id`,

`assistant_id`,

`thread_id`,

`on_run_completed`,

`end_time`,

`schedule`,

`timezone`,

`created_at`,

`updated_at`,

`user_id`,

`payload`,

`next_run_date`,

`metadata`,

`enabled`

#### Response

200

application/json

Success

cron\_id

string<uuid>

required

The ID of the cron.

thread\_id

string<uuid>

required

The ID of the thread.

end\_time

string<date-time>

required

The end date to stop running the cron.

schedule

string

required

The schedule to run, cron format.

created\_at

string<date-time>

required

The time the cron was created.

updated\_at

string<date-time>

required

The last time the cron was updated.

payload

Payload · object

required

The run payload to use for creating new run.

enabled

boolean

default:true

required

Whether the cron job should be enabled. Disabled crons are not executed.

assistant\_id

string<uuid> | null

The ID of the assistant.

user\_id

string | null

The ID of the user.

next\_run\_date

string<date-time> | null

The next run date of the cron.

metadata

Metadata · object

The cron metadata.