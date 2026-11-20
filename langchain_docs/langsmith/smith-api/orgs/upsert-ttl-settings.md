---
title: "Upsert TTL settings - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/orgs/upsert-ttl-settings
scraped_at: 2026-11-15T03:41:29.729712
word_count: 80
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Base TTL settings model.

default\_trace\_tier

enum<string>

required

Available options:

`longlived`,

`shortlived`

tenant\_id

string<uuid> | null

apply\_to\_all\_projects

boolean

default:false

#### Response

200

application/json

Successful Response

TTL settings model.

default\_trace\_tier

enum<string>

required

Available options:

`longlived`,

`shortlived`

id

string<uuid>

required

organization\_id

string<uuid>

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

configured\_by

enum<string>

required

Available options:

`system`,

`user`

tenant\_id

string<uuid> | null

apply\_to\_all\_projects

boolean

default:false

longlived\_ttl\_days

integer | null