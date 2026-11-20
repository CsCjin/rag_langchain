---
title: "Validate rule - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/run/validate-rule
scraped_at: 2026-11-15T03:41:42.268758
word_count: 251
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Schema for validating rules without creating them.

Extends RunRulesCreateSchema with test data fields for validation.
Only LLM-as-judge rules (evaluators) are supported, not code\_evaluators.

For trace-level evaluators, provide test\_inputs / test\_outputs.
For thread evaluators (group\_by="thread\_id"), provide test\_thread\_id +
session\_id instead; the backend fetches and assembles all turns automatically.

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

test\_inputs

Test Inputs · object | null

test\_outputs

Test Outputs · object | null

test\_reference\_outputs

Test Reference Outputs · object | null

test\_attachments

Test Attachments · object | null

test\_thread\_id

string | null

validate\_project\_compatibility

boolean

default:false

#### Response

200

application/json

Successful Response