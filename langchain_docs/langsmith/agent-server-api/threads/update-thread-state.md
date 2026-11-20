---
title: "Update Thread State - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/threads/update-thread-state
scraped_at: 2026-11-15T03:38:20.090631
word_count: 77
---

#### Path Parameters

thread\_id

string<uuid>

required

The ID of the thread.

#### Body

application/json

Payload for updating the state of a thread.

values

any[]Values · objectany[]Values · object

The values to update the state with.

checkpoint

Checkpoint · object

The checkpoint to update the state of.

Show child attributes

as\_node

string

Update the state as if this node had just executed.

#### Response

200

application/json

Success

Response for adding state to a thread.

checkpoint

Checkpoint · object