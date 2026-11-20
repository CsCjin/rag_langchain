---
title: "Delete a data plane - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/data_planes/delete-a-data-plane
scraped_at: 2026-11-16T08:49:03.732704
word_count: 82
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

id

string<uuid>

required

Data plane ID

#### Response

202

application/json

Data plane deprovisioning started

api\_url

string

created\_at

string

firewall

object

Show child attributes

fleet\_oidc

object

Show child attributes

id

string

maintenance\_window

string

name

string

provisioning\_settings

object

Show child attributes

region

string

status

enum<string>

Available options:

`requested`,

`provisioning`,

`provisioning_failed`,

`active`,

`updating`,

`inactive`,

`deprovisioning`,

`deleted`,

`revoked`

status\_updated\_at

string

ttl

object

Show child attributes

workspaces

object[]

Show child attributes