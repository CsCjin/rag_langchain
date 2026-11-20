---
title: "Create feedback with token post - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/feedback/create-feedback-with-token-post
scraped_at: 2026-11-15T03:41:01.020308
word_count: 56
---

#### Path Parameters

token

string<uuid>

required

Feedback ingest token. It's a credential: anyone who has it can submit feedback.

#### Body

application/json

Feedback create schema with token.

score

numberintegerbooleannumberintegerboolean

extend\_trace\_retention

boolean

default:true

value

numberintegerbooleanstringnumberintegerbooleanstring

comment

string | null

correction

Correction · objectstringCorrection · objectstring

metadata

Metadata · object | null

#### Response

200

application/json

Successful Response