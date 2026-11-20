---
title: "Prune Threads - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/threads/prune-threads
scraped_at: 2026-11-15T03:38:19.512593
word_count: 83
---

#### Body

application/json

Payload for pruning threads.

thread\_ids

string<uuid>[]

required

List of thread IDs to prune.

strategy

enum<string>

default:delete

The prune strategy. 'delete' removes threads entirely. 'keep\_latest' prunes old checkpoints but keeps threads and their latest state.

Available options:

`delete`,

`keep_latest`

sync\_checkpoint\_delete

boolean

default:false

If true, delete checkpoints before responding instead of deferring them to background deletion. Use when thread data must be gone on return.

#### Response

200

application/json

Success

Response from pruning threads.

pruned\_count

integer

required

Number of threads successfully pruned.