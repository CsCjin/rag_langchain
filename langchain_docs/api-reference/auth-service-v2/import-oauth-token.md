---
title: "Import Oauth Token - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/import-oauth-token
scraped_at: 2026-11-15T03:37:54.570834
word_count: 97
---

#### Body

application/json

Import a directly-obtained OAuth token (no authorization-code exchange).

Used by the Slack managed-install flow, which receives a bot token inline
from `apps.managedInstall` rather than via the browser OAuth redirect. The
token is persisted for the caller's org/user against `provider_id` (which
must already exist in the caller's org).

provider\_id

string

required

access\_token

string

required

refresh\_token

string | null

expires\_in\_seconds

integer | null

scopes

string[]

metadata

Metadata · object | null

is\_default

boolean

default:true

#### Response

200

application/json

Successful Response

Response for a token import — the created token id only, no secrets.

token\_id

string

required