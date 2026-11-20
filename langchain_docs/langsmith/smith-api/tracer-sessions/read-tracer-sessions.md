---
title: "Read tracer sessions - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/read-tracer-sessions
scraped_at: 2026-11-15T03:42:12.817013
word_count: 271
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Headers

accept

string | null

#### Query Parameters

reference\_free

boolean | null

reference\_dataset

string<uuid>[] | null

id

string<uuid>[] | null

name

string | null

name\_contains

string | null

dataset\_version

string | null

sort\_by

enum<string>

default:start\_time

Available options:

`name`,

`start_time`,

`last_run_start_time`,

`latency_p50`,

`latency_p99`,

`error_rate`,

`feedback`

sort\_by\_desc

boolean

default:true

metadata

string | null

sort\_by\_feedback\_key

string | null

sort\_by\_feedback\_source

enum<string> | null

Available options:

`session`,

`run`

offset

integer

default:0

Required range: `x >= 0`

limit

integer

default:100

Required range: `1 <= x <= 100`

tag\_value\_id

string<uuid>[] | null

facets

boolean

default:false

filter

string | null

include\_stats

boolean

default:false

use\_approx\_stats

boolean

default:false

stats\_start\_time

string<date-time> | null

stats\_select

string[] | null

stats\_filter

string | null

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