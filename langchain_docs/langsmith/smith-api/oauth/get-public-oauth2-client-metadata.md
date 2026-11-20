---
title: "Get public OAuth2 client metadata - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/oauth/get-public-oauth2-client-metadata
scraped_at: 2026-11-15T03:41:13.436489
word_count: 136
---

Error

```
A valid request URL is required to generate request examples
```

200

400

404

```
{
  "client_id": "<string>",
  "client_name": "<string>",
  "client_uri": "<string>",
  "logo_uri": "<string>",
  "policy_uri": "<string>",
  "tos_uri": "<string>"
}
```

```
{
  "error": "<string>",
  "error_description": "<string>"
}
```

```
{
  "error": "<string>",
  "error_description": "<string>"
}
```

GET

/

oauth

/

client

/

{clientID}

Try it

Error

```
A valid request URL is required to generate request examples
```

200

400

404

```
{
  "client_id": "<string>",
  "client_name": "<string>",
  "client_uri": "<string>",
  "logo_uri": "<string>",
  "policy_uri": "<string>",
  "tos_uri": "<string>"
}
```

```
{
  "error": "<string>",
  "error_description": "<string>"
}
```

```
{
  "error": "<string>",
  "error_description": "<string>"
}
```

#### Path Parameters

clientID

string

required

OAuth2 client ID

#### Response

200

application/json

OK

client\_id

string

client\_name

string

client\_uri

string

logo\_uri

string

policy\_uri

string

tos\_uri

string

Was this page helpful?

YesNo