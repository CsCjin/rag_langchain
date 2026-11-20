---
title: "Get openid connect userinfo - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/oauth/get-openid-connect-userinfo
scraped_at: 2026-11-15T03:41:13.080625
word_count: 44
---

#### Authorizations

Authorization

string

header

required

Bearer tokens are used to authenticate from the UI. Must also specify x-tenant-id or x-organization-id (for org scoped apis).

#### Response

200

application/json

OK

email

string

email\_verified

boolean

ls\_org\_id

string

ls\_org\_name

string

name

string

picture

string

sub

string