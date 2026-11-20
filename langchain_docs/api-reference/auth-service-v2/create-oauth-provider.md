---
title: "Create Oauth Provider - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/create-oauth-provider
scraped_at: 2026-11-15T03:37:53.067505
word_count: 193
---

#### Body

application/json

* AuthorizationCodeProviderCreateRequest
* ClientCredentialsProviderCreateRequest

Create an authorization\_code provider (the default when grant\_type is omitted).

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

auth\_url

string

required

Minimum string length: `1`

grant\_type

string

default:authorization\_code

Allowed value: `"authorization_code"`

client\_secret

string | null

uses\_pkce

boolean

default:false

code\_challenge\_method

string

default:S256

provider\_type

enum<string> | null

Available options:

`microsoft`,

`salesforce`,

`slack`,

`x`

token\_endpoint\_auth\_method

enum<string>

default:client\_secret\_post

Available options:

`none`,

`client_secret_basic`,

`client_secret_post`

authorization\_params

Authorization Params · object

Show child attributes

allowed\_redirect\_uris

string[]

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