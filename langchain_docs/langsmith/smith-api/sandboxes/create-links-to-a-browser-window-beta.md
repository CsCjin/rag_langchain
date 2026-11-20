---
title: "Create links to a browser window (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/create-links-to-a-browser-window-beta
scraped_at: 2026-11-15T03:41:47.258029
word_count: 171
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

embed\_origins

string[]

EmbedOrigins are the origins whose pages may show the window's pages in
an iframe, such as [https://app.example.com](https://app.example.com/): https, or http on
localhost, with no path. Without them no page may frame the window.

Maximum array length: `5`

ttl\_seconds

integer

TTLSeconds is how long the links work, from 60 seconds to 24 hours.
Defaults to 24 hours.

Required range: `60 <= x <= 86400`

#### Response

200

application/json

OK

act\_embed\_url

string

act\_url

string

ActURL also lets the person take control of the window, use it, and
hand it back.

expires\_at

string<date-time>

view\_embed\_url

string

ViewEmbedURL and ActEmbedURL open the same window in an iframe with the
token in the URL fragment, which no server, log or Referer header sees.
Viewer options follow the token in the fragment, as in
{act\_embed\_url}&fit=follow&zoom=1.

view\_url

string

ViewURL shows the window and takes no input.