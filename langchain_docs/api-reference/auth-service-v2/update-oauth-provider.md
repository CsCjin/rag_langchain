---
title: "Update Oauth Provider - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/update-oauth-provider
scraped_at: 2026-11-15T03:37:56.566241
word_count: 191
---

#### Path Parameters

provider\_id

string

required

#### Body

application/json

Request model for updating OAuth provider.

name

string | null

client\_id

string | null

client\_secret

string | null

auth\_url

string | null

token\_url

string | null

uses\_pkce

boolean | null

code\_challenge\_method

string | null

authorization\_params

Authorization Params · object | null

Show child attributes

scopes

string[] | null

token\_params

ClientCredentialsTokenParams · object | null

Optional extra fields for a client\_credentials token request.

Show child attributes

allowed\_redirect\_uris

string[] | null

default\_redirect\_uri

string | null

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