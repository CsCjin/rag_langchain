---
title: "Read single chart - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/charts/read-single-chart
scraped_at: 2026-11-15T03:40:44.246051
word_count: 118
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

chart\_id

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

after\_index

integer | null

tag\_value\_id

string<uuid>[] | null

#### Response

200

application/json

Successful Response

* SingleCustomChartResponseSerialized
* CustomTextBlockResponse

data

CustomChartsDataPoint · object[]

required

Show child attributes

id

string<uuid>stringstring<uuid>string

required

title

string

required

index

integer

required

chart\_type

enum<string>

required

Available options:

`line`,

`bar`,

`table`,

`kpi`,

`top-k`,

`pie`

series

CustomChartSeries · object[]

required

Show child attributes

description

string | null

metadata

Metadata · object | null

common\_filters

CustomChartSeriesFilters · object | null

Show child attributes