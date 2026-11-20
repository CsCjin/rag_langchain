---
title: "Migrate to SmithDB-backed APIs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/smithdb-sdk-migration
scraped_at: 2026-11-15T03:42:25.087245
word_count: 1700
---

## Context

In May 2026, we released [SmithDB](https://www.langchain.com/blog/introducing-smithdb?utm_source=docs), a new observability database built for modern AI agents. SmithDB delivers industry-leading performance across every key observability workload, making core LangSmith experiences dramatically faster.
New SDK methods are required to query your traces with SmithDB. This guide helps you migrate your codebase.

## Why migrate

* Queries run up to 12x faster on SmithDB. See the [benchmarks](https://www.langchain.com/blog/introducing-smithdb?utm_source=docs#performance).
* On LangSmith Cloud, the new query endpoints have higher rate limits than the deprecated ones.
* Dedicated methods for [traces](/langsmith/smithdb-sdk-migration-traces) and [threads](/langsmith/smithdb-sdk-migration-threads) replace filtering runs by hand.
* The deprecated methods stop working on January 31, 2027 on LangSmith Cloud, and when ClickHouse is turned off on self-hosted, at the latest with v0.19. Migrating early avoids a last-minute rush.

## Migrate with an AI agent

Copy the following prompt into your coding agent. It first sums up the change in plain words and waits for your go. Then it finds every SDK method and direct API call to the deprecated endpoints, waits for your approval, and migrates them locally. It pushes and opens a pull request only if you approve.

Migrate off deprecated LangSmith endpoints

CopiedCopy prompt

## Deprecation and removal

Each SDK method and its underlying endpoint share the same deprecation date.

| Deployment | Deprecation | Removal |
| --- | --- | --- |
| All Cloud regions | End of July 2026 | 31 Jan 2027 |
| Self-Hosted | `v0.16` | `v0.19` |

For details on how LangSmith deprecates and removes API endpoints and SDK methods, see [API and SDK deprecation policy](/langsmith/endpoint-deprecation).

## Minimum SDK version

The new SDK methods are available starting at these SDK versions:

| Language | Package | Minimum version |
| --- | --- | --- |
| Python | `langsmith` | `>=0.10.15` |
| TypeScript | `langsmith` | `>=0.8.9` |
| Java | `langsmith-java` | `0.1.0-beta.22` |
| Go | `langsmith-go` | `v0.25.4` |
| CLI | `langsmith-cli` | `v0.2.44` |

The [LangSmith CLI](/langsmith/langsmith-cli) queries the same SmithDB-backed endpoints and requires `v0.2.44` or later.

## About self-hosted

* The new methods documented in this guide require self-hosted version 0.16 or later, independent of the data store used.
* The deprecated methods stop working once ClickHouse is disabled.
* Where possible, the SDK raises a warning or error identifying the version to upgrade to, instead of failing without explanation.

## Methods by area

The before and after change for each method is documented on the page for its area.

## Query runs

Search the runs in a project: filters, field projection, sorting, and pagination. The largest surface area in the migration.

## Retrieve runs

Fetch one run by ID, load its child runs, and build the URL of a run in the LangSmith UI.

## Traces

Query the traces in a project, read their token and cost aggregates, and list the runs that belong to one trace.

## Threads

Query the threads in a project and list the traces (turns) that belong to one thread.

## Dataset experiment runs

Query the runs recorded by an experiment on a dataset, including pagination and sorting by feedback score.

## Feedback and sharing

Create feedback on a run, add runs to an annotation queue, and share, unshare, or read publicly shared runs.

## Affected methods and endpoints

Every SDK method and API endpoint below is deprecated and stops working on the removal date above. Search your codebase for all of them. Endpoint paths are relative to `/api/v1`; the area pages have before/after examples for each one, except where noted.

### SDK methods

* Python
* TypeScript
* Java
* Go

Deprecated methods on `Client` and `AsyncClient`:

| Deprecated | Replacement |
| --- | --- |
| `list_runs()` | `client.runs.query()` |
| `read_run()` | `client.runs.retrieve()` |
| `get_run_url()` | `client.runs.get_url()` |
| `list_threads()` | `client.threads.query()` |
| `read_thread()` | `client.threads.list_traces()` |
| `share_run()` | `client.runs.share.create()` |
| `unshare_run()` | `client.runs.share.delete()` |
| `read_run_shared_link()`, `run_is_shared()` | `client.runs.retrieve(selects=["SHARE_URL"])` |
| `list_shared_runs()` | `client.public.runs.query()` |
| `read_shared_run()` | `client.public.runs.retrieve()` |
| `get_experiment_results()` | `client.datasets.experiment_runs.query()` |
| `add_runs_to_annotation_queue()` | `client.annotation_queues.items.create()` |
| `list_runs_from_annotation_queue()`, `get_run_from_annotation_queue()` | `client.annotation_queues.items.list()` |
| `delete_run_from_annotation_queue()` | `client.annotation_queues.items.delete_all()` |
| `evaluate_run()`, `aevaluate_run()` | No replacement: run the evaluator yourself and log the result with `create_feedback()` |

Deprecated methods on `Client`:

| Deprecated | Replacement |
| --- | --- |
| `listRuns()` | `client.runs.query()` |
| `readRun()` | `client.runs.retrieve()` |
| `getRunUrl()` | `client.runs.getURL()` |
| `listThreads()`, `listGroupRuns()` | `client.threads.query()` |
| `readThread()` | `client.threads.listTraces()` |
| `shareRun()` | `client.runs.share.create()` |
| `unshareRun()` | `client.runs.share.delete()` |
| `readRunSharedLink()` | `client.runs.retrieve({ selects: ["SHARE_URL"] })` |
| `listSharedRuns()` | `client.public.runs.query()` |
| `addRunsToAnnotationQueue()` | `client.annotationQueues.items.create()` |
| `listRunsFromAnnotationQueue()`, `getRunFromAnnotationQueue()` | `client.annotationQueues.items.list()` |
| `deleteRunFromAnnotationQueue()` | `client.annotationQueues.items.deleteAll()` |
| `getSizeFromAnnotationQueue()` | `client.annotationQueues.items.retrieveCount()` |

| Deprecated | Replacement |
| --- | --- |
| `client.runs().query()`, `queryV1()` | `client.runs().queryV2()` |
| `client.runs().retrieve()`, `retrieveV1()` | `client.runs().retrieveV2()` |
| `client.datasets().runs().query()` | `client.datasets().experimentRuns().query()` |
| `client.annotationQueues().runs().create()`, `createByKey()` | `client.annotationQueues().items().create()` |
| `client.annotationQueues().runs().list()`, `client.annotationQueues().retrieveRun()` | `client.annotationQueues().items().list()` |
| `client.annotationQueues().runs().update()` | `client.annotationQueues().items().update()` |
| `client.annotationQueues().runs().deleteAll()`, `deleteQueue()` | `client.annotationQueues().items().deleteAll()` |
| `client.annotationQueues().retrieveSize()`, `retrieveTotalSize()`, `retrieveTotalArchived()` | `client.annotationQueues().items().retrieveCount()` |
| `client.annotationQueues().createRunStatus()` | `client.annotationQueues().items().createStatus()` |

| Deprecated | Replacement |
| --- | --- |
| `client.Runs.Query()`, `QueryAutoPaging()`, `QueryV1()` | `client.Runs.QueryV2()` |
| `client.Runs.Get()`, `GetV1()` | `client.Runs.GetV2()` |
| `client.Datasets.Runs.Query()` | `client.Datasets.ExperimentRuns.Query()` |
| `client.AnnotationQueues.Runs.New()`, `NewByKey()` | `client.AnnotationQueues.Items.New()` |
| `client.AnnotationQueues.Runs.List()`, `client.AnnotationQueues.GetRun()` | `client.AnnotationQueues.Items.List()` |
| `client.AnnotationQueues.Runs.Update()` | `client.AnnotationQueues.Items.Update()` |
| `client.AnnotationQueues.Runs.DeleteAll()`, `DeleteQueue()` | `client.AnnotationQueues.Items.DeleteAll()` |
| `client.AnnotationQueues.GetSize()`, `GetTotalSize()`, `GetTotalArchived()` | `client.AnnotationQueues.Items.GetCount()` |
| `client.AnnotationQueues.NewRunStatus()` | `client.AnnotationQueues.Items.NewStatus()` |

### Endpoints

| Deprecated | Replacement | Area |
| --- | --- | --- |
| `POST /runs/query` | `POST /api/v2/runs/query` | [Query runs](/langsmith/smithdb-sdk-migration-query-runs) |
| `GET /runs/{run_id}` | `GET /api/v2/runs/{run_id}` | [Retrieve runs](/langsmith/smithdb-sdk-migration-runs) |
| `POST /runs/group` | `POST /api/v2/threads/query` | [Threads](/langsmith/smithdb-sdk-migration-threads) |
| `GET /runs/{run_id}/share` | `GET /api/v2/runs/{run_id}?selects=SHARE_URL` | [Feedback and sharing](/langsmith/smithdb-sdk-migration-feedback) |
| `PUT /runs/{run_id}/share` | `POST /api/v2/runs/{run_id}/share` | [Feedback and sharing](/langsmith/smithdb-sdk-migration-feedback) |
| `DELETE /runs/{run_id}/share` | `DELETE /api/v2/runs/{trace_id}/share` (takes the trace ID) | [Feedback and sharing](/langsmith/smithdb-sdk-migration-feedback) |
| `POST /datasets/{dataset_id}/runs` | `POST /api/v2/datasets/{dataset_id}/experiment-runs` | [Dataset experiment runs](/langsmith/smithdb-sdk-migration-experiments) |
| `GET /public/{share_token}/run/{run_id}` | `GET /api/v2/public/{share_token}/run/{run_id}` | [Feedback and sharing](/langsmith/smithdb-sdk-migration-feedback) |
| `POST /public/{share_token}/runs/query` | `POST /api/v2/public/{share_token}/runs/query` | [Feedback and sharing](/langsmith/smithdb-sdk-migration-feedback) |

The annotation queue run endpoints move to the queue items API under `/api/v1/platform/annotation-queues`. For adding runs to a queue, see [Annotation queues: add runs](/langsmith/smithdb-sdk-migration-feedback#annotation-queues-add-runs). For listing and counting queue items, see [Annotation queues: read runs](/langsmith/smithdb-sdk-migration-feedback#annotation-queues-read-runs). For the other endpoints, see the [API reference](/langsmith/smith-api) for request and response shapes.

| Deprecated (`/annotation-queues/...`) | Replacement (`/api/v1/platform/annotation-queues/...`) |
| --- | --- |
| `POST /{queue_id}/runs`, `POST /{queue_id}/runs/by-key` | `POST /{queue_id}/items` |
| `GET /{queue_id}/runs`, `GET /{queue_id}/run/{index}` | `GET /{queue_id}/items` |
| `GET /{queue_id}/runs/resolve/{queue_run_id}` | `GET /{queue_id}/items/{item_id}/placement` |
| `PATCH /{queue_id}/runs/{queue_run_id}` | `PATCH /{queue_id}/items/{item_id}` |
| `DELETE /{queue_id}/runs/{queue_run_id}`, `POST /{queue_id}/runs/delete` | `POST /{queue_id}/items/delete` |
| `GET /{queue_id}/size`, `GET /{queue_id}/total_size`, `GET /{queue_id}/total_archived` | `GET /{queue_id}/items/count` |
| `POST /status/{annotation_queue_run_id}` | `POST /items/{queue_item_id}/status` |

## Exceptions

* Python
* TypeScript
* Java
* Go
* cURL

The SmithDB-backed methods raise new exception classes instead of the legacy `langsmith.utils` exception classes.

| Before (`langsmith.utils`) | After (`langsmith`) | Notes |
| --- | --- | --- |
| `LangSmithError` | `LangsmithError` | Base exception class for the SDK; casing changed |
| `LangSmithAPIError` | `InternalServerError` | 5xx |
| `LangSmithRequestTimeout` | `APITimeoutError` | Raised when a request times out |
| `LangSmithUserError` | *(removed)* | No direct equivalent. The 403 org-scoped-key case now raises `PermissionDeniedError`; client-side argument validation now raises a standard `ValueError` or `TypeError` |
| `LangSmithRateLimitError` | `RateLimitError` | 429; unchanged name |
| `LangSmithAuthError` | `AuthenticationError` | 401 |
| `LangSmithNotFoundError` | `NotFoundError` | 404; unchanged name |
| `LangSmithConflictError` | `ConflictError` | 409; unchanged name |
| `LangSmithConnectionError` | `APIConnectionError` | Raised when the client cannot connect to the API |
| `LangSmithExceptionGroup` | *(removed)* | No equivalent |
| *(not available)* | `APIError` | New: base class for all API-related errors, with `message`, `request`, and `body` attributes |
| *(not available)* | `APIStatusError` | New: base class for all 4xx/5xx status errors |
| *(not available)* | `BadRequestError` | New: 400 |
| *(not available)* | `PermissionDeniedError` | New: 403 |
| *(not available)* | `UnprocessableEntityError` | New: 422 |
| *(not available)* | `APIResponseValidationError` | New: raised when a response does not match the expected schema |

The SmithDB-backed methods raise new exception classes instead of plain `Error`.

| Before (plain `Error`) | After (`langsmith`) | Notes |
| --- | --- | --- |
| *(not available)* | `LangsmithError` | base class for all SDK errors |
| *(not available)* | `InternalServerError` | 5xx |
| *(not available)* | `APIConnectionTimeoutError` | Raised when a request times out |
| *(not available)* | `RateLimitError` | 429 |
| *(not available)* | `AuthenticationError` | 401 |
| *(not available)* | `NotFoundError` | 404 |
| *(not available)* | `ConflictError` | 409 |
| *(not available)* | `APIConnectionError` | Raised when the client cannot connect to the API |
| *(not available)* | `APIError` | base class for all API-related errors, with `status`, `headers`, and `error` properties |
| *(not available)* | `BadRequestError` | 400 |
| *(not available)* | `PermissionDeniedError` | 403 |
| *(not available)* | `UnprocessableEntityError` | 422 |
| *(not available)* | `APIUserAbortError` | Raised when a request is aborted via an `AbortController` |

No change. Error handling is unaffected by this migration.

No change. Error handling is unaffected by this migration.

No change. Error handling is unaffected by this migration.

## Discontinued

The following methods are discontinued. They call the retired `/feedback/formulas` endpoints, which return `410 Gone` on composite-feedback v2 and are scheduled for removal on 2026-08-20. Composite scores are now managed as [composite evaluators](/langsmith/composite-evaluators-ui), which implement a composite score as a code evaluator plus a run rule. There is no SDK replacement.

### Feedback formula methods

| Python | TypeScript |
| --- | --- |
| [`list_feedback_formulas`](https://reference.langchain.com/python/langsmith/client/Client/list_feedback_formulas) | NA |
| [`get_feedback_formula_by_id`](https://reference.langchain.com/python/langsmith/client/Client/get_feedback_formula_by_id) | NA |
| [`create_feedback_formula`](https://reference.langchain.com/python/langsmith/client/Client/create_feedback_formula) | NA |
| [`update_feedback_formula`](https://reference.langchain.com/python/langsmith/client/Client/update_feedback_formula) | NA |
| [`delete_feedback_formula`](https://reference.langchain.com/python/langsmith/client/Client/delete_feedback_formula) | NA |

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/smithdb-sdk-migration.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).