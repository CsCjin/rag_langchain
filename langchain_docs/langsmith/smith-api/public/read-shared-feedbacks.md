---
title: "Read shared feedbacks - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/public/read-shared-feedbacks
scraped_at: 2026-11-15T03:41:35.944122
word_count: 165
---

#### Path Parameters

share\_token

string<uuid>

required

#### Query Parameters

run

string<uuid>[] | null

key

string[] | null

session

string<uuid>[] | null

source

enum<string>[] | null

Enum for feedback source types.

Available options:

`api`,

`model`,

`app`,

`auto_eval`

limit

integer

default:100

Required range: `1 <= x <= 100`

offset

integer

default:0

Required range: `x >= 0`

user

string<uuid>[] | null

has\_comment

boolean | null

has\_score

boolean | null

level

enum<string> | null

Enum for feedback levels.

Available options:

`run`,

`session`

#### Response

200

application/json

Successful Response

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