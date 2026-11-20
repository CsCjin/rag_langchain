---
title: "Update a registry - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/update-a-registry
scraped_at: 2026-11-15T03:41:54.929258
word_count: 84
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

name

string

required

Registry name

#### Body

application/json

auth\_type

enum<string>

Available options:

`DOCKER_CONFIG`,

`AWS_ROLE`

aws\_role\_arn

string

name

string

password

string

url

string

username

string

#### Response

200

application/json

OK

auth\_type

enum<string>

Available options:

`DOCKER_CONFIG`,

`AWS_ROLE`

aws\_role\_arn

string

created\_at

string

created\_by

string

id

string

name

string

provider

enum<string>

Available options:

`DOCKER_REGISTRY`,

`HARBOR`,

`GHCR`,

`ECR`,

`GAR`,

`DOCKER_HUB`

repository\_search\_mode

enum<string>

Available options:

`GLOBAL`,

`SCOPED`,

`NONE`

updated\_at

string

updated\_by

string

url

string