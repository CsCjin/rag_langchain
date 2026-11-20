---
title: "Create chart - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/charts/create-chart
scraped_at: 2026-11-15T03:40:40.702647
word_count: 129
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

* CustomChartCreate
* CustomTextBlockCreate

title

string

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

CustomChartSeriesCreate · object[]

required

Show child attributes

description

string | null

index

integer | null

Required range: `0 <= x <= 100`

section\_id

string<uuid> | null

metadata

Metadata · object | null

common\_filters

CustomChartSeriesFilters · object | null

Show child attributes

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