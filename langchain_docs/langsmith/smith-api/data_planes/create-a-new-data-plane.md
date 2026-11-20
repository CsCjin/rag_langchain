---
title: "Create a new data plane - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/data_planes/create-a-new-data-plane
scraped_at: 2026-11-16T08:49:03.560167
word_count: 166
---

#### Authorizations

API KeyOrganization IDBearer AuthAPI KeyOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

* Option 1
* Option 2
* Option 3

name

string

required

region

string

required

role\_arn

string

required

additional\_tags

object[]

Maximum array length: `40`

Show child attributes

byoiam

object

Show child attributes

byovpc

object

Show child attributes

eks\_api\_privatelink\_disabled

boolean

Use a public EKS API endpoint restricted to LangSmith control-plane egress IPs instead of creating a managed PrivateLink endpoint service. Defaults to false.

public\_load\_balancer

boolean

trace\_storage

enum<string>

TraceStorage selects the run and trace store. Defaults to SMITHDB.

Available options:

`CLICKHOUSE`,

`SMITHDB`

vpc\_cidr

string

VPCCIDR is used only when LangSmith creates the VPC.

#### Response

202

application/json

Data plane requested

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