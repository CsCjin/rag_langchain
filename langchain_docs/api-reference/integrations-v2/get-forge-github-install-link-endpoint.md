---
title: "Get Forge Github Install Link Endpoint - Docs by LangChain"
url: https://docs.langchain.com/api-reference/integrations-v2/get-forge-github-install-link-endpoint
scraped_at: 2026-11-15T03:38:02.843885
word_count: 90
---

#### Body

application/json

Request to create a GitHub App installation link.

return\_to

string | null

URL to return to after completing the GitHub App installation.

#### Response

200

application/json

Successful Response

Engine GitHub App connect-link response. Returned by
`/forge/github/install`. `install_url` is now the *OAuth authorize* URL —
the user lands on GitHub OAuth first, the callback enumerates what they
can actually see, and either auto-routes to a fresh install or shows a
server-rendered picker. Field name kept for backwards compatibility with
the FE, but the contents changed.

install\_url

string

required