---
title: "List org members with workspace roles - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/list-org-members-with-workspace-roles
scraped_at: 2026-11-15T03:41:24.136585
word_count: 191
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

limit

integer

Page size (default 50, max 500)

offset

integer

Page offset (default 0)

active\_is

boolean

Filter: true = only active members; false = only pending members

pending\_is

boolean

Filter: true = only pending members; false = only active members

name\_like

string[]

Glob filter on display name; use \* as wildcard (repeatable, matches any)

email\_like

string[]

Glob filter on email; use \* as wildcard (repeatable, matches any)

workspace\_name\_like

string[]

Glob filter on workspace name or ID; use \* as wildcard (repeatable, matches any)

organization\_role\_like

string[]

Glob filter on organization role name; use \* as wildcard (repeatable, matches any)

workspace\_role\_like

string[]

Glob filter on workspace role name; use \* as wildcard (repeatable, matches any)

#### Response

200

application/json

Org members

avatar\_url

string

created\_at

string

display\_name

string

auth-resolved display name

email

string

id

string

identity\_id or pending\_identity\_id

is\_disabled

boolean

user disabled

is\_pending

boolean

true for pending invitations

linked\_login\_methods

object[]

Show child attributes

ls\_user\_id

string

nil for pending members

role\_id

string

org role

role\_name

string

org role name

scim\_groups

object[]

Show child attributes

workspace\_memberships

object[]

Show child attributes