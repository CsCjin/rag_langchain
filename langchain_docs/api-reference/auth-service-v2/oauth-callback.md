---
title: "Oauth Callback - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/oauth-callback
scraped_at: 2026-11-15T03:37:55.640680
word_count: 31
---

#### Path Parameters

provider\_id

string

required

#### Body

application/json

Request model for OAuth callback finalization (frontend bridge and headless).

code

string

required

state

string

required

#### Response

200

application/json

Successful Response