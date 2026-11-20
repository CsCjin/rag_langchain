---
title: "List GitHub Repositories - Docs by LangChain"
url: https://docs.langchain.com/api-reference/integrations-v1/list-github-repositories
scraped_at: 2026-11-15T03:38:02.256974
word_count: 100
---

#### Path Parameters

integration\_id

string<uuid>

required

GitHub integration ID.

#### Response

200

application/json

Successful Response

host\_integration\_id

string<uuid>

required

GitHub Integration ID.

For example, in the `POST /v2/deployments` request body, set `integration_id` to the value of this field.

id

integer

required

GitHub repository ID.

name

string

required

GitHub repository name.

owner

string

required

GitHub repository owner.

url

string

required

GitHub repository URL.

For example, in the `POST /v2/deployments` request body, set `source_config.repo_url` to the value of this field.

default\_branch

string

required

GitHub repository default branch.

For example, in the `POST /v2/deployments` request body, set `source_revision_config.repo_ref` to the value of this field.