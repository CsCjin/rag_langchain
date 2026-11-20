---
title: "Store or update an item. - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/store/store-or-update-an-item
scraped_at: 2026-11-15T03:38:13.790714
word_count: 85
---

#### Body

application/json

Request to store or update an item.

namespace

string[]

required

A list of strings representing the namespace path.

key

string

required

The unique identifier for the item within the namespace.

value

Value · object

required

A dictionary containing the item's data.

index

enum<boolean>string[]enum<boolean>string[]

Controls search indexing - null (use defaults), false (disable), or list of field paths to index.

Available options:

`false`

ttl

number | null

Optional time-to-live in minutes for the item, or null for no expiration.

#### Response

204

Success