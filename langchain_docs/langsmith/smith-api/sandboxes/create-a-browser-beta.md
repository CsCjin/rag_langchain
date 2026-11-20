---
title: "Create a browser (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/sandboxes/create-a-browser-beta
scraped_at: 2026-11-15T03:41:46.029013
word_count: 235
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Body

application/json

delete\_after\_stop\_seconds

integer

DeleteAfterStopSeconds deletes the browser this long after it stops.
Defaults to the sandbox default; 0 keeps a stopped browser until it is
deleted.

Required range: `x >= 0`

hidpi

boolean

HiDPI renders pages at twice the resolution, so the live view is sharp on
HiDPI screens, at four times the pixels for the browser to render and
stream. Off by default, and fixed once the browser is created.

idle\_ttl\_seconds

integer

IdleTTLSeconds stops the browser after this long without use. A stopped
browser resumes with its memory on the next connection. Defaults to the
sandbox default; 0 disables the idle stop.

Required range: `x >= 0`

mem\_bytes

integer

name

string

Name of the browser sandbox. Generated when omitted, as "browser-"
followed by the browser's ID.

proxy\_config

object

ProxyConfig applies a sandbox's proxy rules to the pages the browser
loads: header injection, access control, and relay rules.

Show child attributes

vcpus

integer

VCPUs and MemBytes size the browser sandbox, as for any sandbox. With
neither set, a browser gets 2 vCPUs and 8 GiB.

#### Response

201

application/json

Created

attachments

object[]

Attachments are listed only while the browser is running.

Show child attributes

hidpi

boolean

HiDPI reports whether pages render at twice the resolution. It is
reported only while the browser is running.

id

string

name

string

status

string