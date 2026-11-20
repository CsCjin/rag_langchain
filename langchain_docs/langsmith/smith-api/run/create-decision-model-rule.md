---
title: "Create decision model rule - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/create-decision-model-rule
scraped_at: 2026-11-15T03:41:38.032156
word_count: 526
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

A decision-model evaluator to create and attach to a project or dataset.

display\_name

string

required

The evaluator's name.

prompt

tuple[]

required

The prompt the model reads, as (role, template) pairs.

Show child attributes

questions

Questions · object

required

The questions, keyed by feedback key, in the order to ask them.

Show child attributes

session\_id

string<uuid> | null

The tracing project to evaluate.

dataset\_id

string<uuid> | null

The dataset whose experiments to evaluate.

template\_format

enum<string>

default:mustache

Available options:

`mustache`,

`f-string`

variable\_mapping

Variable Mapping · object | null

Maps the prompt's variables to run fields.

Show child attributes

provider

enum<string>

default:typesafe

typesafe for Jev and SemIf, typesafe\_compatible for a TypeSafe-compatible endpoint, or openai\_decisions.

Available options:

`typesafe`,

`typesafe_compatible`,

`openai_decisions`

model

string | null

Defaults to jev-latest for typesafe and gpt-6-luna for openai\_decisions. Use semif-qwen3.5-4b for SemIf.

base\_url

string | null

Call this endpoint directly instead of through the LangSmith gateway, with the workspace's TYPESAFE\_API\_KEY or OPENAI\_API\_KEY secret. Required for typesafe\_compatible.

model\_headers

Model Headers · object | null

Headers sent with each model call. They are saved in the evaluator's prompt as given, so do not put API keys here.

Show child attributes

timeout\_seconds

integer | null

Seconds to wait for each model call. openai\_decisions only.

max\_retries

integer | null

How many times to retry a failed model call. openai\_decisions only.

playground\_settings\_id

string<uuid> | null

A saved model configuration to start from: its model, endpoint, key and settings apply unless set here.

sampling\_rate

number

default:1

The fraction of runs to evaluate.

filter

string | null

Only evaluate runs that match this filter.

#### Response

200

application/json

Successful Response

Run rules schema.

id

string<uuid>

required

tenant\_id

string<uuid>

required

display\_name

string

required

sampling\_rate

number

required

webhooks

RunRulesWebhookSchema · object[] | null

required

Show child attributes

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

evaluator\_version

integer

required

is\_enabled

boolean

default:true

session\_id

string<uuid> | null

session\_name

string | null

dataset\_id

string<uuid> | null

dataset\_name

string | null

filter

string | null

trace\_filter

string | null

tree\_filter

string | null

add\_to\_annotation\_queue\_id

string<uuid> | null

add\_to\_annotation\_queue\_name

string | null

add\_to\_dataset\_id

string<uuid> | null

add\_to\_dataset\_name

string | null

add\_to\_dataset\_prefer\_correction

boolean

default:false

corrections\_dataset\_id

string<uuid> | null

use\_corrections\_dataset

boolean

default:false

num\_few\_shot\_examples

integer | null

evaluators

EvaluatorTopLevel · object[] | null

Show child attributes

code\_evaluators

CodeEvaluatorTopLevel · object[] | null

Show child attributes

alerts

RunRulesPagerdutyAlertSchema · object[] | null

Show child attributes

extend\_only

boolean

default:false

is\_managed\_evaluator

boolean

default:false

is\_tracing\_disabled

boolean

default:false

extend\_evaluator\_trace\_retention

boolean | null

extend\_dataset\_trace\_retention

boolean | null

extend\_annotation\_queue\_trace\_retention

boolean | null

extend\_webhook\_trace\_retention

boolean | null

include\_extended\_stats

boolean

default:false

backfill\_from

string<date-time> | null

backfill\_id

string<uuid> | null

backfill\_status

string | null

backfill\_progress

number | null

backfill\_error

string | null

backfill\_completed\_at

string<date-time> | null

transient

boolean

default:false

evaluator\_id

string<uuid> | null

evaluator\_name

string | null

evaluator\_type

string | null

alignment\_annotation\_queue\_id

string<uuid> | null

group\_by

enum<string> | null

Available options:

`thread_id`,

`trajectory_id`

spend\_limit

RunRuleSpendLimitSchema · object | null

Show child attributes

effective\_spend\_limit

RunRuleSpendLimitSchema · object | null

spend\_limit if set; otherwise the organization's default evaluator spend limit, once the rule has made its first evaluator call.

Show child attributes

trace\_count

integer | null

spend\_usd

number | null