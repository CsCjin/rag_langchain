---
title: "Check Oauth Tokens Exist Batch - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/check-oauth-tokens-exist-batch
scraped_at: 2026-11-15T03:37:52.096506
word_count: 42
---

#### Body

application/json

Provider IDs to check token presence for, for the current user.

provider\_ids

string[]

required

#### Response

200

application/json

Successful Response

Per-provider token presence for the current user (provider\_id -> has\_token).

has\_token

Has Token · object

required

Show child attributes