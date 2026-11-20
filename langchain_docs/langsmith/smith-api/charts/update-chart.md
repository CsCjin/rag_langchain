---
title: "Update chart - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/charts/update-chart
scraped_at: 2026-11-15T03:40:44.144064
word_count: 168
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

title

stringMissing · objectstringMissing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

description

stringMissing · objectstringMissing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

index

integer

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

Required range: `0 <= x <= 100`

chart\_type

enum<string>Missing · objectenum<string>Missing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

Enum for custom chart types.

Available options:

`line`,

`bar`,

`table`,

`kpi`,

`top-k`,

`pie`,

`text`

series

CustomChartSeriesUpdate · object

* CustomChartSeriesUpdate · object[]
* Missing · object

Show child attributes

section\_id

string<uuid>Missing · objectstring<uuid>Missing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

metadata

Metadata · object

* Metadata
* Missing

common\_filters

CustomChartSeriesFilters · object

* CustomChartSeriesFilters
* Missing

Show child attributes

markdown

stringMissing · objectstringMissing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

#### Response

200

application/json

Successful Response

* CustomChartResponse
* CustomTextBlockResponse

id

string<uuid>

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

section\_id

string<uuid>

required

series

CustomChartSeries · object[] | null

required

Show child attributes

description

string | null

metadata

Metadata · object | null