---
title: "Delete Assistant - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/assistants/delete-assistant
scraped_at: 2026-11-15T03:38:08.626135
word_count: 56
---

#### Path Parameters

assistant\_id

string<uuid>

required

The ID of the assistant.

#### Query Parameters

delete\_threads

boolean

default:false

If true, delete all threads with metadata.assistant\_id matching this assistant, along with runs and checkpoints belonging to those threads. Auth filters are applied, so threads not visible to the user will not be deleted.

#### Response

200

application/json

Success