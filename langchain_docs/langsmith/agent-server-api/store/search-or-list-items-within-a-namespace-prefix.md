---
title: "Search or list items within a namespace prefix. - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/store/search-or-list-items-within-a-namespace-prefix
scraped_at: 2026-11-15T03:38:13.702299
word_count: 146
---

#### Body

application/json

Request to list or search for items within a namespace prefix. Without a query, lists items by last updated time. With a query, performs natural language search.

namespace\_prefix

string[] | null

List of strings representing the namespace prefix.

filter

Filter · object | null

Optional dictionary of key-value pairs to filter results.

limit

integer

default:10

Maximum number of items to return (default is 10).

offset

integer

default:0

Number of items to skip before returning results (default is 0).

query

string | null

Optional natural language search query. If not provided, items are returned ordered by last updated time (listing mode). If provided, performs a natural language search over item contents.

refresh\_ttl

boolean | null

Whether to refresh the TTL on items returned by this search. If null, uses the store's default behavior.

#### Response

200

application/json

Success

items

object[]

required

Show child attributes