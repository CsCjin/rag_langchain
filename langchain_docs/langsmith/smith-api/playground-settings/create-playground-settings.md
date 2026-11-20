---
title: "Create playground settings - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/playground-settings/create-playground-settings
scraped_at: 2026-11-15T03:41:30.461257
word_count: 216
---

#### Authorizations

API KeyTenant IDOrganization IDBearer AuthAPI KeyTenant IDOrganization IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

settings

Settings · object

required

name

string | null

description

string | null

options

PlaygroundSavedOptions · object | null

Show child attributes

settings\_type

enum<string>

default:complex

Available options:

`complex`,

`simple`

scope

enum<string>

default:workspace

Available options:

`workspace`,

`organization`

oauth\_enabled

boolean | null

oauth\_token\_url

string | null

oauth\_client\_id

string | null

oauth\_client\_secret

string | null

oauth\_token\_endpoint\_auth\_method

enum<string> | null

Available options:

`client_secret_basic`,

`client_secret_post`

oauth\_params

Oauth Params · object | null

Show child attributes

oauth\_headers

Oauth Headers · object | null

Show child attributes

#### Response

200

application/json

Successful Response

id

string<uuid>

required

settings

Settings · object

required

created\_at

string<date-time>

required

updated\_at

string<date-time>

required

options

PlaygroundSavedOptions · object | null

Show child attributes

name

string | null

organization\_id

string<uuid> | null

description

string | null

settings\_type

enum<string>

default:complex

Available options:

`complex`,

`simple`

created\_by\_ls\_user\_id

string<uuid> | null

updated\_by\_ls\_user\_id

string<uuid> | null

available\_in\_playground

boolean

default:true

available\_in\_evaluators

boolean

default:true

available\_in\_agent\_builder

boolean

default:false

available\_in\_polly

boolean

default:false

available\_in\_insights\_heavy

boolean

default:false

available\_in\_insights\_light

boolean

default:false

oauth\_enabled

boolean | null

oauth\_token\_url

string | null

oauth\_client\_id

string | null

oauth\_client\_secret

string | null

oauth\_token\_endpoint\_auth\_method

enum<string> | null

Available options:

`client_secret_basic`,

`client_secret_post`

oauth\_params

Oauth Params · object | null

Show child attributes

oauth\_headers

Oauth Headers · object | null

Show child attributes