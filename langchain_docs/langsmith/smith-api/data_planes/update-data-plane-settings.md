---
title: "Update data plane settings - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/data_planes/update-data-plane-settings
scraped_at: 2026-11-16T08:49:04.147363
word_count: 118
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

#### Body

application/json

firewall

object

Show child attributes

fleet\_oidc

object

Show child attributes

maintenance\_window

string

MaintenanceWindow is a weekly UTC window: two hours on AWS and GCP, or four hours on Azure.

ttl

object

Show child attributes

#### Response

200

application/json

Updated data plane

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