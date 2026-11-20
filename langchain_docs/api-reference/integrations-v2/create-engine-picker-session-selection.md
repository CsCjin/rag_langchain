---
title: "Create Engine Picker Session Selection - Docs by LangChain"
url: https://docs.langchain.com/api-reference/integrations-v2/create-engine-picker-session-selection
scraped_at: 2026-11-15T03:38:02.357507
word_count: 102
---

#### Path Parameters

session\_id

string

required

#### Body

application/json

Selection from a Forge GitHub App installation picker.

action

enum<string>

required

Whether to attach an installation or install the GitHub App.

Available options:

`ATTACH`,

`INSTALL_NEW`

installation\_id

integer | null

GitHub installation ID required when action is ATTACH.

#### Response

200

application/json

Successful Response

Response for POST /forge/github/picker-session/{id}/select. The FE
navigates the browser to `redirect_url` — that URL is either the FE
result page (for "attach") or a github.com install picker (for
"install\_new"). Returning JSON instead of 302 keeps the FE's POST-as-API
flow predictable and lets it surface errors before navigating.

redirect\_url

string

required