---
title: "Create feedback ingest token - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/feedback/create-feedback-ingest-token
scraped_at: 2026-11-15T03:41:00.313334
word_count: 89
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

* FeedbackIngestTokenCreateSchema · object
* FeedbackIngestTokenCreateSchema · object[]

Feedback ingest token create schema.

run\_id

string<uuid>

required

feedback\_key

string

required

expires\_in

TimedeltaInput · object | null

Timedelta input.

Show child attributes

expires\_at

string<date-time> | null

feedback\_config

FeedbackConfig · object | null

Show child attributes

#### Response

200

application/json

Successful Response

* FeedbackIngestTokenSchema · object
* FeedbackIngestTokenSchema · object[]

Feedback ingest token schema.

id

string<uuid>

required

url

string

required

expires\_at

string<date-time>

required

feedback\_key

string

required