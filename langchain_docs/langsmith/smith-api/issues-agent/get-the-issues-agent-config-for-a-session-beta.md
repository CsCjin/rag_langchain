---
title: "Get the issues agent config for a session (Beta) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smith-api/issues-agent/get-the-issues-agent-config-for-a-session-beta
scraped_at: 2026-11-15T03:41:06.208990
word_count: 448
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

#### Response

200

application/json

OK

agent\_overview\_accepted

boolean

analysis\_level

enum<string>

AnalysisLevel controls coverage vs cost: "standard" (default), "reduced"
(one scan a day, fewer traces per scan), or "expanded" (2x traces per
run). Stored NULL in the DB means standard; reads always return a
concrete value.

Available options:

`standard`,

`reduced`,

`expanded`

auto\_open\_fix\_pr

boolean

When true, every fix run on this board opens a pull request instead of
parking the fix for someone to publish. Defaults to false.

context\_hub\_repo\_handle

string

created\_at

string

cron\_enabled

boolean

cron\_schedule

string

engine\_version

string

github\_base\_branch

string

Legacy: aliases the oldest GitHub entry in GithubRepos.

github\_repo\_subdir

string

Legacy: aliases the oldest GitHub entry in GithubRepos.

github\_repo\_url

string

Legacy: aliases the oldest GitHub entry in GithubRepos.

github\_repos

object[]

Show child attributes

id

string

issue\_count

integer

latest\_run\_id

string

latest\_thread\_id

string

IDs of the latest run on LangSmith Deployments; NULL until first trigger.

linear\_available

boolean

linear\_integration

object

Show child attributes

linear\_sync\_health

object

Show child attributes

preview\_verify\_enabled

boolean

PreviewVerifyEnabled lets this board's fix runs use preview deployments
when issue validation is enabled for its tracing project.

preview\_verify\_no\_trigger

boolean

PreviewVerifyNoTrigger tells fix verification not to request a preview.
The deployment builds one itself for the fix commit.

priorities

string[]

red\_team\_target

object | null

RedTeamTarget is the external endpoint red-team runs probe instead of
the validation deployment, or null when none is configured.

Show child attributes

run\_filter

string

RunFilter is a runs-filter-DSL string scoping which traces Engine analyzes
(prompt guidance, not an enforced query). NULL = no scope. Clamped by
validateRunFilter.

selected\_trace\_count

integer

deprecated

Compatibility alias for selected\_trace\_count\_last\_14\_days.
Deprecated: use selected\_trace\_count\_last\_14\_days.

selected\_trace\_count\_last\_14\_days

integer

The number of traces Engine inspected in the last 14 days.

selected\_trace\_count\_last\_7\_days

integer

The number of traces Engine inspected in the last 7 days.

session\_agent\_overview\_repo\_id

string

session\_id

string

session\_lcu\_spend\_limit\_monthly

string

SessionLCUSpendLimitMonthly is the per-project monthly Engine LCU spend
limit: NULL/negative = no limit; 0 or positive = monthly cap (spend is
never negative, so a cap of 0 always reads as reached). Enforced in
addition to (and independently of) the org-level limit. Serialized as a
string to preserve NUMERIC(28,6) precision.

session\_name

string

JOINed from tracer\_session

target\_auth

object

Show child attributes

tenant\_id

string

tenant\_name

string

JOINed from tenants (workspace label); resolved server-side so the org-admin list can label rows across workspaces the caller isn't a member of

updated\_at

string

user\_instructions

string

User-owned freeform preferences. Engine reads this as authoritative
context and reconciles it into the Agent Overview on the next scan, but
never edits it. NULL when the user hasn't set any.

validation\_deployment\_id

string

ValidationDeploymentID selects the deployment used for baseline replay
and as the parent of fix-verification previews.