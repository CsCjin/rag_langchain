---
title: "Get run from annotation queue - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/annotation-queues/get-run-from-annotation-queue
scraped_at: 2026-11-15T03:40:30.354495
word_count: 353
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

queue\_id

string<uuid>

required

index

integer

required

#### Query Parameters

include\_extra

boolean

default:false

#### Response

200

application/json

Successful Response

Run schema with annotation queue info.

name

string

required

run\_type

enum<string>

required

Enum for run types.

Available options:

`tool`,

`chain`,

`llm`,

`retriever`,

`embedding`,

`prompt`,

`parser`

trace\_id

string<uuid>

required

dotted\_order

string

required

id

string<uuid>

required

status

string

required

session\_id

string<uuid>

required

app\_path

string

required

queue\_run\_id

string<uuid>

required

inputs

Inputs · object | null

inputs\_preview

string | null

start\_time

string<date-time>

end\_time

string<date-time> | null

extra

Extra · object | null

error

string | null

execution\_order

integer

default:1

Required range: `x >= 1`

serialized

Serialized · object | null

outputs

Outputs · object | null

outputs\_preview

string | null

parent\_run\_id

string<uuid> | null

manifest\_id

string<uuid> | null

manifest\_s3\_id

string<uuid> | null

events

Events · object[] | null

tags

string[] | null

inputs\_s3\_urls

Inputs S3 Urls · object | null

outputs\_s3\_urls

Outputs S3 Urls · object | null

s3\_urls

S3 Urls · object | null

trace\_min\_start\_time

string<date-time> | null

trace\_max\_start\_time

string<date-time> | null

child\_run\_ids

string<uuid>[] | null

direct\_child\_run\_ids

string<uuid>[] | null

parent\_run\_ids

string<uuid>[] | null

feedback\_stats

Feedback Stats · object | null

Show child attributes

reference\_example\_id

string<uuid> | null

total\_tokens

integer

default:0

prompt\_tokens

integer

default:0

completion\_tokens

integer

default:0

prompt\_token\_details

Prompt Token Details · object | null

Show child attributes

completion\_token\_details

Completion Token Details · object | null

Show child attributes

total\_cost

string | null

Pattern: `^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$`

prompt\_cost

string | null

Pattern: `^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$`

completion\_cost

string | null

Pattern: `^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$`

prompt\_cost\_details

Prompt Cost Details · object | null

Show child attributes

completion\_cost\_details

Completion Cost Details · object | null

Show child attributes

price\_model\_id

string<uuid> | null

first\_token\_time

string<date-time> | null

messages

Messages · object[] | null

last\_queued\_at

string<date-time> | null

in\_dataset

boolean | null

share\_token

string<uuid> | null

trace\_tier

enum<string> | null

Available options:

`longlived`,

`shortlived`

trace\_first\_received\_at

string<date-time> | null

ttl\_seconds

integer | null

trace\_upgrade

boolean

default:false

reference\_dataset\_id

string<uuid> | null

thread\_id

string | null

last\_reviewed\_time

string<date-time> | null

added\_at

string<date-time> | null

effective\_added\_at

string<date-time> | null

reserved\_by

string<uuid>[]

completed\_by

string<uuid>[]

source\_proposed\_example\_id

string<uuid> | null