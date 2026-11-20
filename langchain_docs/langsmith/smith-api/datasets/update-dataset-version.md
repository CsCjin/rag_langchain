---
title: "Update dataset version - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/datasets/update-dataset-version
scraped_at: 2026-11-15T03:40:51.806620
word_count: 185
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

dataset\_id

string<uuid>

required

#### Body

application/json

as\_of

string<date-time>stringstring<date-time>string

required

The version to tag: an ISO 8601 timestamp, or the name of an existing tag on this dataset (latest resolves to the most recent example change, and returns 404 for a dataset with no examples). A value that does not parse as a timestamp is treated as a tag name, and an unknown tag name returns 404. Timestamps are not checked against the dataset history: the tag covers every example change made on or before that time, so a future time keeps picking up new changes until it passes. Use the exact as\_of of an existing version, since looking up a version by tag returns 404 when the tag's time does not match a version.

tag

string

required

The tag to set. If the dataset already has this tag, it is moved to the new version. The tag latest is reserved and returns 400.

#### Response

200

application/json

Successful Response

Dataset version schema.

as\_of

string<date-time>

required

tags

string[] | null