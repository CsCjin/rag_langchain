---
title: "Get Cron - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/crons/get-cron
scraped_at: 2026-11-15T03:38:11.248950
word_count: 136
---

#### Path Parameters

cron\_id

string<uuid>

required

#### Response

200

application/json

Success

Represents a scheduled task.

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