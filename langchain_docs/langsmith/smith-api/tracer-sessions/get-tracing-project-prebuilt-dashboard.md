---
title: "Get tracing project prebuilt dashboard - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/tracer-sessions/get-tracing-project-prebuilt-dashboard
scraped_at: 2026-11-15T03:42:11.122931
word_count: 124
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

#### Path Parameters

session\_id

string<uuid>

required

#### Body

application/json

timezone

string

default:UTC

start\_time

string<date-time> | null

end\_time

string<date-time> | null

stride

TimedeltaInput · object

Timedelta input.

Show child attributes

omit\_data

boolean

default:false

group\_by

RunStatsGroupBy · object | null

Group by param for run stats.

Show child attributes

#### Response

200

application/json

Successful Response

title

string

required

id

string<uuid>stringstring<uuid>string

required

charts

(SingleCustomChartResponseSerialized · object | CustomTextBlock · object)[]

required

* SingleCustomChartResponseSerialized
* CustomTextBlock

Show child attributes

description

string | null

index

integer | null

session\_id

string<uuid> | null

sub\_sections

SingleCustomChartSubSectionResponse · object[] | null

Show child attributes

layout

DashboardLayout · object | null

Show child attributes