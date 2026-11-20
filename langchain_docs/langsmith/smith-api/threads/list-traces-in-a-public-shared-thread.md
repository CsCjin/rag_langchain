---
title: "List traces in a public shared thread - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/threads/list-traces-in-a-public-shared-thread
scraped_at: 2026-11-15T03:42:04.468732
word_count: 98
---

#### Path Parameters

share\_token

string<uuid>

required

Share token UUID

#### Query Parameters

selects

string[]

required

repeatable public thread trace fields to include

cursor

string

opaque cursor from a previous page

page\_size

integer

page size (default 20, max 100)

order

string

ASC or DESC

#### Response

200

application/json

OK

items

object[]

`items` is the page of root traces in this thread. Which properties are populated on each trace depends on the `selects` query parameter.

Show child attributes

next\_cursor

string

`next_cursor` is the opaque cursor to pass as `cursor` on the next request. Null on the final page.

Example:

`"eyJydW5zX2N1cnNvciI6Imx0KGN1cnNvciwiLi4uIikifQ=="`