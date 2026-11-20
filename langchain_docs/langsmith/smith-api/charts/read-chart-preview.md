---
title: "Read chart preview - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/charts/read-chart-preview
scraped_at: 2026-11-15T03:40:43.206763
word_count: 46
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

bucket\_info

CustomChartsRequestBase · object

required

Show child attributes

chart

CustomChartCreatePreview · object

required

Show child attributes

#### Response

200

application/json

Successful Response

data

CustomChartsDataPoint · object[]

required

Show child attributes