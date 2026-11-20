---
title: "Get Oauth Provider - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/get-oauth-provider
scraped_at: 2026-11-15T03:37:54.122055
word_count: 118
---

#### Path Parameters

provider\_id

string

required

OAuth provider ID

#### Response

200

application/json

Successful Response

Response model for OAuth provider.

id

string

required

organization\_id

string

required

provider\_id

string

required

name

string

required

client\_id

string

required

token\_url

string

required

uses\_pkce

boolean

required

code\_challenge\_method

string | null

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

auth\_url

string | null

grant\_type

enum<string>

default:authorization\_code

OAuth 2 grant a provider uses to obtain access tokens.

Available options:

`authorization_code`,

`client_credentials`

scopes

string[]

token\_params

ClientCredentialsTokenParams · object

Optional extra fields for a client\_credentials token request.

Show child attributes

provider\_type

string | null

mcp\_server\_url

string | null

token\_endpoint\_auth\_method

string

default:client\_secret\_post

authorization\_params

Authorization Params · object

Show child attributes

is\_dynamic\_client

boolean

default:false

allowed\_redirect\_uris

string[]

default\_redirect\_uri

string | null