---
title: "Create rule - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/create-rule
scraped_at: 2026-11-15T03:41:38.300033
word_count: 414
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

display\_name

string

required

sampling\_rate

number

required

session\_id

string<uuid> | null

is\_enabled

boolean

default:true

dataset\_id

string<uuid> | null

filter

string | null

trace\_filter

string | null

tree\_filter

string | null

backfill\_from

string<date-time> | null

use\_corrections\_dataset

boolean

default:false

num\_few\_shot\_examples

integer | null

extend\_only

boolean

default:false

is\_tracing\_disabled

boolean

default:true

extend\_evaluator\_trace\_retention

boolean

default:false

extend\_dataset\_trace\_retention

boolean | null

extend\_annotation\_queue\_trace\_retention

boolean | null

extend\_webhook\_trace\_retention

boolean | null

transient

boolean

default:false

add\_to\_annotation\_queue\_id

string<uuid> | null

add\_to\_dataset\_id

string<uuid> | null

add\_to\_dataset\_prefer\_correction

boolean

default:false

evaluators

EvaluatorTopLevel · object[] | null

Show child attributes

code\_evaluators

CodeEvaluatorTopLevel · object[] | null

Show child attributes

evaluator\_id

string<uuid> | null

alerts

RunRulesPagerdutyAlertSchema · object[] | null

Show child attributes

webhooks

RunRulesWebhookSchema · object[] | null

Show child attributes

evaluator\_version

integer | null

create\_alignment\_queue

boolean

default:false

include\_extended\_stats

boolean

default:false

group\_by

enum<string> | null

Available options:

`thread_id`,

`trajectory_id`

spend\_limit

RunRuleSpendLimitSchema · object | null

Show child attributes

tracer\_session\_issue\_id

string<uuid> | null

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