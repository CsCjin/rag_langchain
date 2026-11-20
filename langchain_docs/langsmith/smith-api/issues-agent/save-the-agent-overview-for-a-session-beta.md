---
title: "Save the agent overview for a session (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/issues-agent/save-the-agent-overview-for-a-session-beta
scraped_at: 2026-11-15T03:41:06.556575
word_count: 37
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

session\_id

string

required

Tracer session ID (UUID)

#### Body

application/json

content

string

#### Response

200

application/json

OK

commit\_hash

string

session\_agent\_overview\_repo\_id

string