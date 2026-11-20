---
title: "Wait For Auth Completion - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/wait-for-auth-completion
scraped_at: 2026-11-15T03:37:56.915622
word_count: 49
---

#### Path Parameters

auth\_id

string

required

Authentication ID to wait for

#### Query Parameters

timeout

integer

default:30

Timeout in seconds (default: 30)

#### Response

200

application/json

Successful Response

Auth wait response.

status

enum<string>

required

Valid auth wait status values.

Available options:

`completed`,

`pending`,

`timeout`,

`not_found`

token

string | null