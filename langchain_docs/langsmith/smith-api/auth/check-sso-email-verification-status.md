---
title: "Check SSO email verification status - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/auth/check-sso-email-verification-status
scraped_at: 2026-11-15T03:40:35.887398
word_count: 95
---

Error

```
A valid request URL is required to generate request examples
```

200

422

```
{
  "email_confirmed_at": "2023-11-07T05:31:56Z"
}
```

```
{
  "detail": [
    "<string>"
  ]
}
```

POST

/

api

/

v1

/

sso

/

email-verification

/

status

Try it

Error

```
A valid request URL is required to generate request examples
```

200

422

```
{
  "email_confirmed_at": "2023-11-07T05:31:56Z"
}
```

```
{
  "detail": [
    "<string>"
  ]
}
```

#### Body

application/json

email

string

required

saml\_provider\_id

string<uuid>

required

#### Response

200

application/json

Successful Response

email\_confirmed\_at

string<date-time> | null

Was this page helpful?

YesNo