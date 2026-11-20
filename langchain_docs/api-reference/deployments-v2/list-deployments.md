---
title: "List Deployments - Docs by LangChain"
url: https://docs.langchain.com/api-reference/deployments-v2/list-deployments
scraped_at: 2026-11-15T03:38:00.147010
word_count: 234
---

#### Query Parameters

limit

integer

default:20

Maximum number of resources to return.

Required range: `1 <= x <= 100`

offset

integer

default:0

Pagination offset. Pass this value to subsequent requests to fetch the next page of resources.

Required range: `x >= 0`

name\_contains

string | null

Name of the deployment to filter by.

name

string | null

Exact deployment name to filter by.

status

string | null

`status` of the deployment to filter by.

remote\_reconciled

boolean | null

Flag to filter by remote reconciled deployments.

tag\_value\_ids

string | null

Comma separated list of tag value IDs of the deployment to filter by.

image\_version

string | null

Image version to filter by.

deployment\_type

enum<string> | null

Deployment type to filter by.

Available options:

`dev_free`,

`dev`,

`prod`,

`dev_zero`,

`dev_free_zero`

deployment\_ids

string | null

Comma separated list of deployment IDs to filter by.

url

string | null

Serving URL of the deployment to filter by.

agent\_id

string | null

Exact agent ID (slug) to filter by: 1 to 63 lowercase letters, digits, or hyphens, starting with a letter. Requires agent mode.

Required string length: `1 - 63`

Pattern: `^[a-z](?:[a-z0-9-]{0,61}[a-z0-9])?$`

agent\_environment

enum<string> | null

Agent environment to filter by. Requires agent mode.

Available options:

`local`,

`development`,

`staging`,

`production`

#### Response

200

application/json

Successful Response

resources

Deployment · object[]

required

Show child attributes

offset

integer

required

Pagination offset. Pass this value to subsequent requests to fetch the next page.