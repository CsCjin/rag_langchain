---
title: "List Forge GitHub Integrations - Docs by LangChain"
url: https://docs.langchain.com/api-reference/integrations-v1/list-forge-github-integrations
scraped_at: 2026-11-15T03:38:01.420246
word_count: 94
---

#### Response

200 - application/json

Successful Response

id

string<uuid>

required

GitHub Integration ID.

For example, in the `POST /v2/deployments` request body, set `integration_id` to the value of this field.

installation\_id

integer

required

GitHub installation ID.

name

string

required

GitHub accout name.

repository\_selection

string | null

Whether the GitHub App install grants access to 'all' repos or only 'selected' ones. When 'selected', newly created repos are not auto-included and must be added on GitHub.

settings\_url

string | null

Deep link to the install's GitHub settings page, where repo access can be edited. GitHub's installation `html_url`.