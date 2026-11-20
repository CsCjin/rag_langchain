---
title: "Update tracer session - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/update-tracer-session
scraped_at: 2026-11-15T03:42:13.500184
word_count: 205
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

session\_id

string<uuid>

required

#### Body

application/json

Update class for TracerSession.

name

string | null

description

string | null

default\_dataset\_id

string<uuid> | null

end\_time

string<date-time> | null

extra

Extra · object | null

trace\_tier

enum<string> | null

Available options:

`longlived`,

`shortlived`

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