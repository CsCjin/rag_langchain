---
title: "Update section - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/charts/update-section
scraped_at: 2026-11-15T03:40:44.312415
word_count: 86
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

title

stringMissing · objectstringMissing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

description

stringMissing · objectstringMissing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

index

integerMissing · objectintegerMissing · object

default:{"\_\_missing\_\_":"\_\_missing\_\_"}

layout

DashboardLayout · object

* DashboardLayout
* Missing

Show child attributes

#### Response

200

application/json

Successful Response

title

string

required

id

string<uuid>

required

description

string | null

index

integer | null

chart\_count

integer | null

created\_at

string<date-time> | null

modified\_at

string<date-time> | null