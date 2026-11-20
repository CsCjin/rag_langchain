---
title: "Authenticate - Docs by LangChain"
url: https://docs.langchain.com/api-reference/auth-service-v2/authenticate
scraped_at: 2026-11-15T03:37:51.370393
word_count: 92
---

#### Body

application/json

Auth authenticate request.

provider

string

required

scopes

string[]

required

user\_id

string | null

ls\_user\_id

string | null

agent\_id

string | null

use\_agent\_builder\_public\_oauth

boolean

default:false

force\_new

boolean

default:false

token\_id

string<uuid> | null

redirect\_uri

string | null

is\_default

boolean

default:true

check\_only

boolean

default:false

#### Response

200

application/json

Successful Response

Auth authenticate response.

status

enum<string>

required

Valid authentication status values.

Available options:

`completed`,

`pending`,

`connection_required`,

`token_expired`

provider\_display\_name

string | null

url

string | null

auth\_id

string | null

token

string | null

user\_id

string | null

metadata

Metadata · object | null