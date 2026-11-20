---
title: "Roll an issues agent webhook signing secret - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/issues-agent/roll-an-issues-agent-webhook-signing-secret
scraped_at: 2026-11-15T03:41:06.324028
word_count: 211
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Path Parameters

session\_id

string

required

Tracer session ID (UUID)

id

string

required

Webhook ID (UUID)

#### Response

200

application/json

OK

created\_at

string

destination\_type

enum<string>

Available options:

`webhook`,

`jira`,

`slack`

event\_types

string[]

has\_jira\_token

boolean

has\_signing\_secret

boolean

has\_unreadable\_credentials

boolean

HasUnreadableCredentials marks a row retained in the settings list whose
encrypted credential envelope could not be opened. No credential-derived
fields are populated for such a row; it must be deleted and recreated.

header\_names

string[]

HeaderNames lists configured header names for write-only clients.

headers

object

Show child attributes

id

string

issue\_statuses

string[]

organization\_id

string

session\_id

string

severity\_threshold

enum<integer>

Available options:

`0`,

`1`,

`2`,

`3`

signing\_secret

string

SigningSecret is present only in successful create, URL-conversion update,
and roll responses.

slack\_channel\_id

string

Keep empty Slack fields in the response. The frontend uses an explicit
empty string to distinguish URL destinations from Slack destinations.

slack\_handoff

object | null

SlackHandoff is nil when no coding-agent hand-off is set on this destination.

Show child attributes

slack\_team\_id

string

tenant\_id

string

updated\_at

string

url

string

URL and Headers are retained as always-empty fields so a client written
against the pre-write-only contract still parses the response. Use
URLDisplay and HeaderNames instead.

url\_display

string

URLDisplay contains only the destination hostname.