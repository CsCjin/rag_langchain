---
title: "Retrieve a single item. - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/store/retrieve-a-single-item
scraped_at: 2026-11-15T03:38:13.524379
word_count: 120
---

#### Query Parameters

key

string

required

namespace

string[]

refresh\_ttl

boolean

Whether to refresh the TTL on this read operation. If not provided, uses the store's default behavior.

#### Response

200

application/json

Success

Represents a single document or data entry in the graph's Store. Items are used to store cross-thread memories.

namespace

string[]

required

The namespace of the item. A namespace is analogous to a document's directory.

key

string

required

The unique identifier of the item within its namespace. In general, keys needn't be globally unique.

value

object

required

The value stored in the item. This is the document itself.

created\_at

string<date-time>

required

The timestamp when the item was created.

updated\_at

string<date-time>

required

The timestamp when the item was last updated.