---
title: "Create feedback - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/feedback/create-feedback
scraped_at: 2026-11-15T03:40:59.995210
word_count: 422
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

Schema used for creating feedback.

key

string

required

Maximum string length: `180`

created\_at

string<date-time>

modified\_at

string<date-time>

score

numberintegerbooleannumberintegerboolean

value

numberintegerbooleanstringValue · objectnumberintegerbooleanstringValue · object

comment

string | null

correction

Correction · objectstringCorrection · objectstring

feedback\_group\_id

string<uuid> | null

comparative\_experiment\_id

string<uuid> | null

run\_id

string<uuid> | null

session\_id

string<uuid> | null

Required unless the feedback is addressed by address. The ID of the tracing project (session) the feedback belongs to.

address

string

Addresses the tracing project through an Agent environment, as lrn:agents/{id}/environments/{environment}, instead of session\_id. The id is 1 to 63 lowercase ASCII letters, digits, or hyphens, starting with a letter and ending with a letter or digit. The environment is local, development, staging, or production, matched case-insensitively. Never combined with session\_id. The Agent and the environment must already exist; sending feedback does not create them. Self-hosted deployments need LangSmith v0.18 or later.

Example:

`"lrn:agents/support-agent/environments/production"`

trace\_id

string<uuid> | null

start\_time

string<date-time> | null

feedback\_thread\_id

string | null

extend\_trace\_retention

boolean

default:true

id

string<uuid>

feedback\_source

AppFeedbackSource · object

Feedback from the LangChainPlus App.

* AppFeedbackSource
* APIFeedbackSource
* ModelFeedbackSource
* AutoEvalFeedbackSource

Show child attributes

feedback\_config

FeedbackConfig · object | null

The scale the score is checked against. If the feedback key already has a feedback config, this must match it exactly or the request is rejected; if it has none, this becomes the key's feedback config.

Show child attributes

feedback\_config\_id

string<uuid> | null

The ID of the feedback config this feedback was written against. It must be a feedback config for this feedback key in the same workspace, or the feedback is rejected. It doesn't change how the score is checked; feedback\_config does that. If omitted, the server may record the key's enforced feedback config, or the one created for the key by this request.

error

boolean | null

deprecated

Deprecated. Use `extra.error` instead. If both values are provided, `error` takes precedence.

extra

Extra · object | null

#### Response

200

application/json

Successful Response

Schema for getting feedback.

key

string

required

id

string<uuid>

required

created\_at

string<date-time>

modified\_at

string<date-time>

score

numberintegerbooleannumberintegerboolean

value

numberintegerbooleanstringValue · objectnumberintegerbooleanstringValue · object

comment

string | null

correction

Correction · objectstringCorrection · objectstring

feedback\_group\_id

string<uuid> | null

comparative\_experiment\_id

string<uuid> | null

run\_id

string<uuid> | null

session\_id

string<uuid> | null

trace\_id

string<uuid> | null

start\_time

string<date-time> | null

is\_root

boolean

default:false

feedback\_source

FeedbackSource · object | null

The feedback source loaded from the database.

Show child attributes

extra

Extra · object | null

feedback\_thread\_id

string | null