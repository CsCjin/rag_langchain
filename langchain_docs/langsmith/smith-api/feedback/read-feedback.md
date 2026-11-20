---
title: "Read feedback - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/feedback/read-feedback
scraped_at: 2026-11-15T03:41:01.953309
word_count: 117
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

feedback\_id

string<uuid>

required

#### Query Parameters

include\_user\_names

boolean | null

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