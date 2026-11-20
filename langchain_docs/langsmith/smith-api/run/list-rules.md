---
title: "List rules - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/list-rules
scraped_at: 2026-11-15T03:41:39.769816
word_count: 300
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

dataset\_id

string<uuid> | null

session\_id

string<uuid> | null

type

enum<string> | null

Available options:

`session`,

`dataset`

name\_contains

string | null

id

string<uuid>[] | null

evaluator\_id

string<uuid> | null

tag\_value\_id

string<uuid>[] | null

include\_backfill\_progress

boolean

default:false

#### Response

200

application/json

Successful Response

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