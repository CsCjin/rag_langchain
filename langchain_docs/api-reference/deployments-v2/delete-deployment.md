---
title: "Delete Deployment - Docs by LangChain"
url: https://docs.langchain.com/api-reference/deployments-v2/delete-deployment
scraped_at: 2026-11-15T03:37:57.863616
word_count: 100
---

#### Path Parameters

deployment\_id

string<uuid>

required

#### Query Parameters

delete\_tracing\_project

boolean

default:false

Optionally delete the deployment's tracing project.

force

boolean

default:false

Force delete the deployment's control-plane metadata, skipping Kubernetes resource cleanup. Only works on a deployment that has already been soft-deleted by a prior delete call; force-deleting a still-active deployment returns 400. Use to clear stale deployments whose runtime is already gone. This is unrecoverable and may orphan remaining cluster-side resources. Reusing the deployment name after a force delete is unsupported and may attach a new deployment to those orphaned resources; use a different name.

#### Response

204

Successful Response