---
title: "Get Revision - Docs by LangChain"
url: https://docs.langchain.com/api-reference/deployments-v2/get-revision
scraped_at: 2026-11-15T03:37:58.986899
word_count: 220
---

#### Path Parameters

deployment\_id

string<uuid>

required

revision\_id

string<uuid>

required

#### Response

200

application/json

Successful Response

Revision resource.

id

string<uuid>

required

The ID of the revision.

This is a read-only field.

created\_at

string<date-time>

required

The creation time of the revision.

This is a read-only field.

updated\_at

string<date-time>

required

The last update time of the revision.

This is a read-only field.

status

enum<string>

required

The status of the revision.

This is a read-only field.

Available options:

`CREATING`,

`QUEUED`,

`AWAITING_BUILD`,

`BUILDING`,

`AWAITING_DEPLOY`,

`DEPLOYING`,

`CREATE_FAILED`,

`BUILD_FAILED`,

`DEPLOY_FAILED`,

`DEPLOYED`,

`SKIPPED`,

`INTERRUPTED`,

`UNKNOWN`

source

enum<string>

required

Deploy from a GitHub repository (`github`), an external Docker image (`external_docker`), a CLI-pushed image (`internal_docker`), uploaded source (`internal_source`), or a prebuilt LangChain template (`internal_template`).

Deploying from GitHub, internal Docker, internal source, or a template is only available for Cloud SaaS deployments. Deploying from an external Docker image is only available for self-hosted deployments. This cannot be changed once the deployment is created.

Available options:

`github`,

`external_docker`,

`internal_docker`,

`internal_source`,

`internal_template`

source\_revision\_config

SourceRevisionConfig · object

required

Source revision configuration.

For a `Deployment` resource, the field values refer to the latest revision of the `Deployment`. For a `Revision` resource, the field values refer to the `Revision` itself.

Show child attributes

status\_message

string | null

Human-readable detail about the current status, such as why a build or deploy failed.

This is a read-only field.