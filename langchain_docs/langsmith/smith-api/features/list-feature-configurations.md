---
title: "List feature configurations - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/features/list-feature-configurations
scraped_at: 2026-11-15T03:40:58.608330
word_count: 82
---

#### Authorizations

API KeyTenant IDBearer AuthAPI KeyTenant IDBearer Auth

X-API-Key

string

header

required

#### Response

200

application/json

OK

default\_model

string

disabled\_models

string[]

DisabledModels is the effective disabled set for the feature: the union of
this workspace's own disabled providers/models and the org-wide disabled
providers. Every consumer (pickers, Fleet catalog) hides these.

feature

string

org\_disabled\_providers

string[]

OrgDisabledProviders is the subset of DisabledModels that is enforced at the
organization level. The workspace settings UI renders these locked so a
workspace admin cannot re-enable them.