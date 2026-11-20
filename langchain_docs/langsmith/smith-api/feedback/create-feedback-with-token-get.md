---
title: "Create feedback with token get - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/feedback/create-feedback-with-token-get
scraped_at: 2026-11-15T03:41:00.384915
word_count: 43
---

#### Path Parameters

token

string<uuid>

required

Feedback ingest token. It's a credential: anyone who has it can submit feedback.

#### Query Parameters

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

string | null

#### Response

200

application/json

Successful Response