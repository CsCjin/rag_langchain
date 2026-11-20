---
title: "Generate a service access token - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/generate-a-service-access-token
scraped_at: 2026-11-15T03:41:49.372002
word_count: 286
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

name

string

required

Sandbox display name

#### Body

application/json

access

enum<string>

Access selects the login mode, mutually exclusive with the minted token.
Omit the field for token mode: mint a short-lived service token (default).
"restricted" — LangSmith login: the sandbox's creator, or any user with SandboxesExec on it (admins by default).
"workspace" — LangSmith login: any member of the owning workspace.
"off" — remove an existing LangSmith login grant and mint a token.
A LangSmith login grant is durable; token mode is refused (409) while one exists.

Available options:

`restricted`,

`workspace`,

`off`

embed\_origins

string[]

EmbedOrigins are the pages allowed to show the service URL in an iframe,
besides LangSmith itself: at most 5 origins such as
[https://app.example.com](https://app.example.com/) (http only for localhost). In token mode they are
bound into the minted token, so they last as long as it does. With
access "restricted" or "workspace" each call sets the grant's whole list,
so omitting the field removes any origins set before.

expires\_in\_seconds

integer

port

integer

#### Response

200

application/json

OK

access

enum<string>

Access echoes the enabled LangSmith login level ("restricted"/"workspace"); omitted in token mode.

Available options:

`restricted`,

`workspace`

browser\_url

string

embed\_origins

string[]

EmbedOrigins echoes the origins that may embed the URL, normalized; omitted when there are none.

embed\_url

string

EmbedURL opens the service in an iframe: the token rides the URL
fragment, which no server, log or Referer header sees, and the page it
loads trades it for the cookie. Append &redirect=/path to land
elsewhere than /. Omitted in LangSmith login mode.

expires\_at

string

service\_url

string

token

string

Token and ExpiresAt are empty in LangSmith login mode (no token is minted).