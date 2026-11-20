---
title: "Set who controls a browser window (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/set-who-controls-a-browser-window-beta
scraped_at: 2026-11-15T03:41:53.717866
word_count: 457
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

Browser name or ID

attachment\_id

string

required

Attachment ID

#### Body

application/json

controller

enum<string>

Controller is "user" to give the window to a person, or "agent" to give
it back to the attached sandbox.

Available options:

`agent`,

`user`

#### Response

200

application/json

OK

act\_url

string

api\_cdp\_url

string

APICDPURL is the same Chrome DevTools endpoint through the LangSmith API,
for clients outside any sandbox. It takes any API credential: headers as
for any API call (X-Api-Key, or Authorization: Bearer with an OAuth
access token, plus X-Tenant-Id where needed), or, for clients that take
only a URL, api\_key, token and tenant\_id query parameters.

cdp\_url

string

CDPURL is the Chrome DevTools endpoint the attached sandbox connects to,
for example with Playwright's connect\_over\_cdp. It works only from inside
that sandbox.

clients

string[]

Clients are the sandboxes currently connected to this window, with "api"
for each client connected through api\_cdp\_url. An unrestricted window's
connections are not listed.

controller

enum<string>

Controller is "agent" while the attached sandbox drives the window and
"user" while a person has taken it over.

Available options:

`agent`,

`user`

created\_at

string

height

integer

id

string

links\_expire\_at

string<date-time>

localhost\_alias

string

LocalhostAlias is the sandbox's localhost as the browser sees it: open
http://<localhost\_alias>: in a window to reach a server listening
on that port in the sandbox, whether bound to localhost or to all
interfaces (any port but 80 and 443). While this is the only sandbox
sharing its localhost, [http://localhost](http://localhost/): works too. Pages on other
sites can navigate to a plain-HTTP server there but cannot fetch from it.
Set only for windows attached with share\_localhost.

name

string

reason

string

Reason is why the agent asked a person to take over, when it did.

sandbox

string

Sandbox is the attached sandbox; empty for a window a person opened.

tabs

object[]

Show child attributes

unrestricted

boolean

Unrestricted windows give their sandbox the whole browser over CDP, with
nothing filtered: every window and tab, every site's cookies, and
commands that close or crash the browser. Taking over such a window does
not pause its sandbox, and the LSBrowserControl domain is not available.

view\_url

string

ViewURL and ActURL open the window on the sandbox service domain with no
LangSmith login, for an agent to send to a person: ViewURL to watch it,
ActURL also to use it while its controller is "user". Anyone holding a
link can open the window until LinksExpireAt. Each response mints new
ones; they are returned only to those who may use the browser.

width

integer

Width and Height are the window's page size in CSS pixels, when it was
given one; a window without one keeps Chrome's default of 1280x800.