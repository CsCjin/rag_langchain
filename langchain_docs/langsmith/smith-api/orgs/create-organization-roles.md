---
title: "Create organization roles - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/create-organization-roles
scraped_at: 2026-11-15T03:41:18.863523
word_count: 98
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

display\_name

string

required

description

string

required

permissions

string[]

required

Permissions to grant. Organization roles do not require organization:read or organization:read-metadata. Omitting these permissions may limit access to organization settings pages.

access\_scope

enum<string>

default:workspace

Scope of the role. Cannot be changed after creation.

Available options:

`organization`,

`workspace`

#### Response

200

application/json

Successful Response

id

string<uuid>

required

name

string

required

display\_name

string

required

description

string

required

permissions

string[]

required

organization\_id

string<uuid> | null

access\_scope

enum<string> | null

Available options:

`organization`,

`workspace`

is\_restricted

boolean

default:false