---
title: "Create tracer session - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/create-tracer-session
scraped_at: 2026-11-15T03:42:08.779351
word_count: 237
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Query Parameters

upsert

boolean

default:false

#### Body

application/json

Create class for TracerSession.

tag\_value\_ids

string<uuid>[] | null

Maximum array length: `100`

start\_time

string<date-time>

end\_time

string<date-time> | null

extra

Extra · object | null

name

string

description

string | null

default\_dataset\_id

string<uuid> | null

reference\_dataset\_id

string<uuid> | null

trace\_tier

enum<string> | null

Available options:

`longlived`,

`shortlived`

id

string<uuid> | null

num\_examples

integer | null

num\_repetitions

integer | null

evaluator\_keys

string[] | null

kicked\_off\_by

string | null

#### Response

200

application/json

Successful Response

TracerSession schema.

id

string<uuid>

required

tenant\_id

string<uuid>

required

start\_time

string<date-time>

end\_time

string<date-time> | null

extra

Extra · object | null

name

string

description

string | null

default\_dataset\_id

string<uuid> | null

reference\_dataset\_id

string<uuid> | null

trace\_tier

enum<string> | null

Available options:

`longlived`,

`shortlived`

run\_count

integer | null

latency\_p50

number | null

latency\_p99

number | null

first\_token\_p50

number | null

first\_token\_p99

number | null

total\_tokens

integer | null

prompt\_tokens

integer | null

completion\_tokens

integer | null

total\_cost

string | null

Pattern: `^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$`

prompt\_cost

string | null

Pattern: `^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$`

completion\_cost

string | null

Pattern: `^(?!^[-+.]*$)[+-]?0*\d*\.?\d*$`

last\_run\_start\_time

string<date-time> | null

last\_run\_start\_time\_live

string<date-time> | null

feedback\_stats

Feedback Stats · object | null

session\_feedback\_stats

Session Feedback Stats · object | null

run\_facets

Run Facets · object[] | null

error\_rate

number | null

streaming\_rate

number | null

test\_run\_number

integer | null

experiment\_progress

ExperimentProgress · object | null

Show child attributes