---
title: "Test prompt webhook - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/prompt-webhooks/test-prompt-webhook
scraped_at: 2026-11-15T03:41:32.544075
word_count: 51
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Schema for testing a prompt webhook.

webhook

PromptWebhookBase · object

required

Base schema for prompt webhooks.

Show child attributes

payload

PromptWebhookPayload · object

required

Show child attributes

#### Response

200

application/json

Successful Response

{key}

string