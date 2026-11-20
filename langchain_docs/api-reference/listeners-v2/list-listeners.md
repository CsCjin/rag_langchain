---
title: "List Listeners - Docs by LangChain"
url: https://docs.langchain.com/api-reference/listeners-v2/list-listeners
scraped_at: 2026-11-15T03:38:04.755279
word_count: 72
---

#### Query Parameters

limit

integer

default:20

Maximum number of resources to return.

Required range: `1 <= x <= 100`

offset

integer

default:0

Pagination offset. Pass this value to subsequent requests to fetch the next page of resources.

Required range: `x >= 0`

#### Response

200

application/json

Successful Response

resources

Listener · object[]

required

Show child attributes

offset

integer

required

Pagination offset. Pass this value to subsequent requests to fetch the next page.