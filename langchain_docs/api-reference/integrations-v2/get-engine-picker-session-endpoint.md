---
title: "Get Engine Picker Session Endpoint - Docs by LangChain"
url: https://docs.langchain.com/api-reference/integrations-v2/get-engine-picker-session-endpoint
scraped_at: 2026-11-15T03:38:02.447068
word_count: 62
---

#### Path Parameters

session\_id

string

required

#### Response

200

application/json

Successful Response

Payload for GET /forge/github/picker-session/{id}. The FE renders
`installs` plus a hardcoded "Install on a new GitHub org" affordance.
`return_to` round-trips back through the select endpoint so the final
result page lands the user back on their originating view.

installs

EnginePickerInstallOption · object[]

required

Show child attributes

return\_to

string | null