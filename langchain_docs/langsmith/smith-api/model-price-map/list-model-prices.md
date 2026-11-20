---
title: "List model prices - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/model-price-map/list-model-prices
scraped_at: 2026-11-15T03:41:11.513906
word_count: 430
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

offset

integer

default:0

Number of entries to skip before this page.

Required range: `x >= 0`

limit

integer

default:100

Maximum number of entries to return.

Required range: `1 <= x <= 100`

q

string | null

Case-insensitive substring matched against the entry name, match pattern, and provider. Hyphens and spaces are treated as equivalent.

Maximum string length: `200`

provider

string[] | null

Only return price maps for these providers (case-insensitive).

Maximum array length: `20`

Minimum string length: `1`

sort\_by

string | null

Field to sort on. Defaults to match priority order.

Allowed value: `"start_time"`

sort\_order

enum<string>

default:desc

Sort direction for sort\_by. Unset start dates sort last.

Available options:

`asc`,

`desc`

#### Response

200

application/json

Successful Response

name

string

required

Display name for the entry, usually the model name.

match\_pattern

string

required

Regular expression matched against the run's model name, for example `^gpt-4o-mini$`.

prompt\_cost

string

required

Cost in US dollars per input (prompt) token.

Pattern: `^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$`

completion\_cost

string

required

Cost in US dollars per output (completion) token.

Pattern: `^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$`

id

string<uuid>

ID of the entry.

start\_time

string<date-time> | null

Only price runs that started at or after this time. Null applies to runs from any time.

tenant\_id

string<uuid> | null

Workspace that owns the entry. Null for organization entries and for LangSmith default entries.

organization\_id

string<uuid> | null

Organization that owns the entry, which every workspace in it prices against unless the workspace overrides it. Null otherwise.

scope

enum<string>

default:BUILTIN

Which scope owns the entry. Server-assigned from the route that created it.

Available options:

`BUILTIN`,

`ORGANIZATION`,

`WORKSPACE`

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