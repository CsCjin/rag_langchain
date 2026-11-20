---
title: "Update prompt webhook - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/prompt-webhooks/update-prompt-webhook
scraped_at: 2026-11-15T03:41:32.665656
word_count: 310
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

webhook\_id

string<uuid>

required

#### Body

application/json

Schema for updating a prompt webhook.

Omitted fields keep their current values. A list or headers value that is
set replaces the stored value.

include\_prompts

string<uuid>[] | null

IDs of the prompts whose events fire the webhook, replacing the current list. Omit to keep it.

exclude\_prompts

string<uuid>[] | null

IDs of prompts whose events never fire the webhook, replacing the current list. Omit to keep it.

url

string<uri> | null

URL that receives the POST requests. Omit to keep the current URL.

Minimum string length: `1`

headers

Headers · object | null

HTTP headers sent with each request, replacing all current headers. Omit to keep them. Masked values (\*\*\*\*\*\*\*\*) from a read are rejected.

triggers

enum<string>[] | null

Events that fire the webhook (commit, tag:create, tag:update), replacing the current list. Omit to keep it.

Valid trigger types for prompt webhooks.

Available options:

`commit`,

`tag:create`,

`tag:update`

#### Response

200

application/json

Successful Response

Schema for a prompt webhook.

url

string<uri>

required

URL that receives a POST request with the prompt event payload.

Minimum string length: `1`

id

string<uuid>

required

tenant\_id

string<uuid>

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

headers

Headers · object | null

HTTP headers sent with each request, for example an Authorization header. Values are stored encrypted and are masked in responses to callers who cannot update prompts.

include\_prompts

string<uuid>[] | null

IDs of the prompts whose events fire the webhook. When empty, events from every prompt in the workspace fire it.

exclude\_prompts

string<uuid>[] | null

IDs of prompts whose events never fire the webhook.

triggers

enum<string>[]

Events that fire the webhook: commit (a new prompt commit), tag:create, and tag:update. A webhook with no triggers never fires.

Valid trigger types for prompt webhooks.

Available options:

`commit`,

`tag:create`,

`tag:update`