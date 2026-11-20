---
title: "Generate a sandbox file download link - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/generate-a-sandbox-file-download-link
scraped_at: 2026-11-15T03:41:49.245161
word_count: 142
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

Sandbox ID or name

#### Body

application/json

path

string

required

content\_disposition

string

content\_type

string

csp\_sandbox

boolean

CSPSandbox false serves the file with no CSP sandbox directive; omit to keep it.

csp\_sandbox\_flags

enum<string>[]

CSPSandboxFlags loosen the CSP sandbox the file is served under; omit for the most restrictive policy.

Available options:

`allow-downloads`,

`allow-forms`,

`allow-modals`,

`allow-orientation-lock`,

`allow-pointer-lock`,

`allow-popups`,

`allow-presentation`,

`allow-scripts`,

`allow-top-navigation-by-user-activation`,

`allow-same-origin`

csp\_source\_bundles

enum<string>[]

CSPSourceBundles allow the served file to fetch from named third-party origins; omit to send no fetch directive.

Available options:

`cdnjs`,

`google-fonts`,

`jsdelivr`,

`unpkg`,

`none`,

`any`

expires\_in\_seconds

integer

ExpiresInSeconds is optional; a link with no expiry never expires.

#### Response

200

application/json

OK

download\_url

string

required

token

string

required

expires\_at

string | null

ExpiresAt is null for a link that never expires.