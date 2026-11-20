---
title: "Ingest runs (multipart) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/runs/ingest-runs-multipart
scraped_at: 2026-11-15T03:41:43.554765
word_count: 70
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

multipart/form-data

post.{run\_id}

file

Run to create (JSON)

patch.{run\_id}

file

Run to update (JSON)

post.{run\_id}.inputs

file

Large inputs object (JSON) stored out‑of‑band

patch.{run\_id}.outputs

file

Large outputs object (JSON) stored out‑of‑band

feedback.{run\_id}

file

Feedback object (JSON) – must include trace\_id and session\_id

attachment.{run\_id}.{filename}

file

Binary attachment linked to run {run\_id}

#### Response

202

application/json

Accepted

{key}

string