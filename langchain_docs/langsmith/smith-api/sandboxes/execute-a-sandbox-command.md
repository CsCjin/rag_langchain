---
title: "Execute a sandbox command - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/execute-a-sandbox-command
scraped_at: 2026-11-15T03:41:48.942966
word_count: 104
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

sandbox\_id

string

required

Sandbox ID or name

#### Body

application/json

command

string[]

Command accepts either a shell command string or an argv string array.

cwd

string

deprecated

Deprecated: use run\_config.work\_dir. Rejected when run\_config is also set.

env

object

deprecated

Deprecated: use run\_config.env\_vars. Rejected when run\_config is also set.

Show child attributes

run\_config

object

RunConfig overrides, for this command only, the user, working directory and env the sandbox's commands run with.

Show child attributes

shell

string

timeout\_seconds

integer

#### Response

200

application/json

OK

exit\_code

integer

stderr

string

stdout

string