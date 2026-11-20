---
title: "List pending workspace invites - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/workspaces/list-pending-workspace-invites
scraped_at: 2026-11-15T03:42:22.032455
word_count: 67
---

#### Authorizations

Authorization

string

header

required

Bearer tokens are used to authenticate from the UI. Must also specify x-tenant-id or x-organization-id (for org scoped apis).

#### Response

200 - application/json

Successful Response

id

string<uuid>

required

created\_at

string<date-time>

required

display\_name

string

required

is\_personal

boolean

required

is\_deleted

boolean

required

organization\_id

string<uuid> | null

tenant\_handle

string | null

data\_plane\_url

string | null

data\_plane\_name

string | null

data\_plane\_region

string | null