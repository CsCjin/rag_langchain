---
title: "Replace a model price - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/model-price-map/replace-a-model-price
scraped_at: 2026-11-15T03:41:11.670263
word_count: 264
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

id

string<uuid>

required

#### Body

application/json

The full replacement for a custom model price entry.

name

string

required

Display name for the entry, usually the model name.

match\_pattern

string

required

Regular expression matched against the run's model name, for example `^gpt-4o-mini$`.

prompt\_cost

numberstringnumberstring

required

Cost in US dollars per input (prompt) token.

completion\_cost

numberstringnumberstring

required

Cost in US dollars per output (completion) token.

start\_time

string<date-time> | null

Only price runs that started at or after this time. Null applies to runs from any time.

match\_path

string[]

Invocation parameter keys checked, in order, for the model name when the run does not report `ls_model_name` metadata.

prompt\_cost\_details

Prompt Cost Details · object | null

Cost in US dollars per input token for specific token types, keyed by the token detail name the run reports, for example `cache_read`. Input tokens not covered here are priced at `prompt_cost`.

Show child attributes

completion\_cost\_details

Completion Cost Details · object | null

Cost in US dollars per output token for specific token types, keyed by the token detail name the run reports, for example `audio`. Output tokens not covered here are priced at `completion_cost`.

Show child attributes

provider

string | null

Only price runs from this provider (the `ls_provider` metadata, case-insensitive), for example `openai` or `anthropic`. Null matches any provider.

prompt\_tokens\_above

integer | null

Only price requests with more input tokens than this, for long-context pricing tiers. Null applies to every request.

Required range: `0 <= x <= 9007199254740991`

#### Response

200

application/json

Successful Response