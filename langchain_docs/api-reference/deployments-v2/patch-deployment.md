---
title: "Patch Deployment - Docs by LangChain"
url: https://docs.langchain.com/api-reference/deployments-v2/patch-deployment
scraped_at: 2026-11-15T03:38:00.895536
word_count: 1114
---

#### Path Parameters

deployment\_id

string<uuid>

required

#### Body

application/json

Request body for patching a deployment.

Patching a deployment may trigger a new revision depending on the provided `source` configurations.

display\_name

string | null

Human-readable display name for the deployment. Updating this does not create a new revision.

Minimum string length: `1`

revision\_source

enum<string> | null

Override the source for this revision. If omitted, falls back to deployment's default source.

Available options:

`github`,

`internal_docker`,

`internal_source`

source\_config

SourceConfigRequest · object | null

Deployment configuration fields specific to the `source`.

All fields are nullable, but are validated based on the `source`.
Updating `custom_url`, `resource_spec`, `install_command`, or `build_command` creates a new revision.

Show child attributes

source\_revision\_config

SourceRevisionConfigRequest · object | null

Fields for a deployment that are specific to the `source` and require a new revision when modified.

All fields are nullable, but are validated based on the `source`.

Show child attributes

tracked\_repo\_ref

string | null

Retarget the git ref the deployment tracks without creating a new revision. Use `source_revision_config.repo_ref` to deploy from a ref instead.

Minimum string length: `1`

deployment\_tier

enum<string> | null

Fixed resource tier to apply to the deployment. Serverless deployments support `SERVERLESS_S`, `SERVERLESS_M`, and `SERVERLESS_L`; dedicated deployments support `DEDICATED_S`, `DEDICATED_M`, and `DEDICATED_L`.

Available options:

`SERVERLESS_S`,

`SERVERLESS_M`,

`SERVERLESS_L`,

`DEDICATED_S`,

`DEDICATED_M`,

`DEDICATED_L`

secrets

Secret · object[] | null

Show child attributes

secret\_references

SecretReference · object[] | null

List of Kubernetes Secret references.

Only applicable for `external_docker` source.

Show child attributes

extra\_manifests

Extra Manifests · object[] | null

Additional Kubernetes objects to apply in the deployment's namespace. Only available on self-hosted installations with extra manifests enabled.

Supports `v1` `ServiceAccount` and `secrets-store.csi.x-k8s.io/v1` `SecretProviderClass` objects, up to 16 objects. `ServiceAccount` objects may only set `automountServiceAccountToken` besides `metadata`. `metadata` may only contain `name`, `labels`, and `annotations`, and `metadata.name` must start with `extra_manifests_name_prefix`. Not supported for deployments on a remote listener.

`SecretProviderClass` objects must use pod workload identity. `spec` may only contain `provider` and `parameters`; `secretObjects` is rejected. Allowed `parameters`: `aws`: `objects`, `region`, `failoverRegion`, `pathTranslation`, `usePodIdentity`, `preferredAddressType`. `azure`: `clientID` (required), `tenantId`, `keyvaultName`, `cloudName`, `objects`, and `usePodIdentity` or `useVMManagedIdentity` set to `false`. `gcp`: `secrets`, and `auth` set to `pod-adc`.

Objects are stored in plaintext, so do not include credentials. They are stored per deployment, not per revision. On PATCH, omit or null to leave unchanged; send an empty list to clear previously stored objects.

route\_through\_gateway

boolean | null

Enable or disable routing OpenAI and Anthropic model calls through the LangSmith LLM gateway.

#### Response

200

application/json

Successful Response

Deployment resource.

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

source\_config

SourceConfig · object

required

Source configuration.

Show child attributes

source\_revision\_config

SourceRevisionConfig · object

required

Source revision configuration.

For a `Deployment` resource, the field values refer to the latest revision of the `Deployment`. For a `Revision` resource, the field values refer to the `Revision` itself.

Show child attributes

secrets

Secret · object[]

required

Show child attributes

id

string<uuid>

required

The ID of the deployment.

This is a read-only field.

tenant\_id

string<uuid>

required

The ID of the tenant that owns the deployment.

This is a read-only field.

created\_at

string<date-time>

required

The creation time of the deployment.

This is a read-only field.

updated\_at

string<date-time>

required

The last update time of the deployment.

This is a read-only field.

status

enum<string>

required

The status of the deployment.

This is a read-only field.

Available options:

`AWAITING_DATABASE`,

`READY`,

`UNUSED`,

`AWAITING_DELETE`,

`AWAITING_FINAL_DELETE`,

`UNKNOWN`

latest\_revision\_id

string<uuid> | null

required

The ID of the latest revision of the deployment.

This is a read-only field.

active\_revision\_id

string<uuid> | null

required

The ID of the current (actively deployed) revision of the deployment.

This is a read-only field.

name

string | null

Deployment name. Required when agent is omitted; retained as the agent identity in the production environment when agent associations are enabled. Omit when supplying agent to generate a deployment name.

Minimum string length: `1`

agent

DeploymentAgent · object | null

Agent and environment to deploy. Both fields are required when supplied.

Show child attributes

secret\_references

SecretReference · object[] | null

List of Kubernetes Secret references.

Only applicable for `external_docker` source.

Show child attributes

extra\_manifests

Extra Manifests · object[]

Extra Kubernetes objects stored for this deployment, in the format accepted by `extra_manifests` on create and PATCH. An empty list means no objects are stored.

Returned only by the get deployment endpoint, to user callers with permission to update the deployment, when extra manifests are enabled on this self-hosted installation and the deployment is not on a remote listener. Omitted otherwise.

shareable

boolean

default:false

Whether the deployment can be shared with LangSmith users outside the organization.

route\_through\_gateway

boolean

default:false

Route OpenAI and Anthropic model calls through the LangSmith LLM gateway.

extra\_manifests\_configured

boolean

default:false

Whether extra Kubernetes manifests are stored for this deployment.

This is a read-only field.

extra\_manifests\_name\_prefix

string | null

Required `metadata.name` prefix for extra manifests, or null when extra manifests are unavailable for this deployment.

This is a read-only field.

tracer\_session\_id

string<uuid> | null

The ID of the LangSmith tracing project the deployment writes runs to.

This is a read-only field.

url

string | null

The deployment's serving URL, once provisioned.

This is a read-only field.

is\_preview

boolean

default:false

Whether this is a preview-build deployment. Full preview metadata (parent deployment, PR, lifecycle) is available from the preview-builds details endpoint.

This is a read-only field.

image\_version

string | null

Image version of the deployment.

display\_name

string | null

Human-readable display name for the deployment.

is\_managed\_deep\_agent

boolean

default:false

Whether this deployment is a Managed Deep Agent deployment.

This is a read-only field.

deployment\_tier

enum<string> | null

The selected fixed resource tier for this deployment. Existing deployments without an explicit selection return the default tier for their deployment type. When compute and database tiers differ, this reflects the compute tier. Null when compute has a custom size.

Available options:

`SERVERLESS_S`,

`SERVERLESS_M`,

`SERVERLESS_L`,

`DEDICATED_S`,

`DEDICATED_M`,

`DEDICATED_L`

compute\_tier

enum<string>stringenum<string>string

The selected fixed resource tier for this deployment's compute. Deployments without an explicit selection return the default tier for their deployment type. `LEGACY_CUSTOM` means the compute has a custom size that matches no tier.

Available options:

`SERVERLESS_S`,

`SERVERLESS_M`,

`SERVERLESS_L`,

`DEDICATED_S`,

`DEDICATED_M`,

`DEDICATED_L`

database\_tier

enum<string>stringenum<string>string

The selected fixed resource tier for this deployment's database. Deployments without an explicit selection return the default tier for their deployment type. `LEGACY_CUSTOM` means the database has a custom size that matches no tier.

Available options:

`SERVERLESS_S`,

`SERVERLESS_M`,

`SERVERLESS_L`,

`DEDICATED_S`,

`DEDICATED_M`,

`DEDICATED_L`