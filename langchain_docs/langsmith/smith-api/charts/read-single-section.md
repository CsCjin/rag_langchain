---
title: "Read single section - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/charts/read-single-section
scraped_at: 2026-11-15T03:40:43.568804
word_count: 118
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

section\_id

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