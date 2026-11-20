---
title: "Get Thread Storage - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-storage
scraped_at: 2026-11-15T03:38:19.155160
word_count: 85
---

#### Path Parameters

thread\_id

string<uuid>

required

The ID of the thread.

#### Response

200

application/json

Success

Bytes a thread occupies in the checkpointer, as stored.

thread\_id

string<uuid>

required

total\_bytes

integer

required

Sum of the three sections below.

checkpoints

Checkpoints · object

required

Checkpoint rows: serialized checkpoint plus metadata.

Show child attributes

channel\_values

Channel Values · object

required

Stored channel values, one row per channel version.

Show child attributes

pending\_writes

Pending Writes · object

required

Task writes not yet folded into a checkpoint.

Show child attributes