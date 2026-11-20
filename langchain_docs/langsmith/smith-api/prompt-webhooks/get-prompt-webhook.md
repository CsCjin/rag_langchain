---
title: "Get prompt webhook - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/prompt-webhooks/get-prompt-webhook
scraped_at: 2026-11-15T03:41:32.094211
word_count: 162
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