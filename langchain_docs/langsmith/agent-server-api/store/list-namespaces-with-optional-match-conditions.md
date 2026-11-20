---
title: "List namespaces with optional match conditions. - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/store/list-namespaces-with-optional-match-conditions
scraped_at: 2026-11-15T03:38:13.372440
word_count: 70
---

#### Body

application/json

prefix

string[]

Optional list of strings representing the prefix to filter namespaces.

suffix

string[]

Optional list of strings representing the suffix to filter namespaces.

max\_depth

integer

Optional integer specifying the maximum depth of namespaces to return.

limit

integer

default:100

Maximum number of namespaces to return (default is 100).

offset

integer

default:0

Number of namespaces to skip before returning results (default is 0).

#### Response

200

application/json

Success