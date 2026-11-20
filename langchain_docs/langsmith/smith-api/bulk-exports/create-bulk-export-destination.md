---
title: "Create bulk export destination - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/bulk-exports/create-bulk-export-destination
scraped_at: 2026-11-15T03:40:39.135787
word_count: 94
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

display\_name

string

required

Minimum string length: `1`

Pattern: `^[a-zA-Z0-9\-_ ']+$`

config

BulkExportDestinationS3Config · object

required

Show child attributes

destination\_type

enum<string>

default:s3

Available options:

`s3`

credentials

BulkExportDestinationS3Credentials · object | null

Show child attributes

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