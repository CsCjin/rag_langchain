---
title: "Update bulk export destination - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/bulk-exports/update-bulk-export-destination
scraped_at: 2026-11-15T03:40:40.269574
word_count: 96
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

destination\_id

string<uuid>

required

#### Body

application/json

credentials

BulkExportDestinationS3Credentials · object | null

Show child attributes

aws\_role\_arn

string | null

AWS IAM role ARN that LangSmith assumes instead of using static credentials.

Minimum string length: `1`

#### Response

200

application/json

Successful Response

display\_name

string

required

Minimum string length: `1`

Pattern: `^[a-zA-Z0-9\-_ ']+$`

config

BulkExportDestinationS3Config · object

required

Show child attributes

id

string<uuid>

required

tenant\_id

string<uuid>

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

credentials\_keys

string[]

required

destination\_type

enum<string>

default:s3

Available options:

`s3`