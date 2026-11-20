---
title: "Patch Listener - Docs by LangChain"
url: https://docs.langchain.com/api-reference/listeners-v2/patch-listener
scraped_at: 2026-11-15T03:38:04.909066
word_count: 203
---

#### Path Parameters

listener\_id

string<uuid>

required

#### Body

application/json

Requst body for patching a listener.

version

string | null

The version of the listener.

compute\_config

ListenerComputeConfig · object | null

Fields for a listener that are specific to `compute_type`.

All fields are nullable, but are validated based on `compute_type`.

Show child attributes

#### Response

200

application/json

Successful Response

Listener resource.

compute\_type

string

required

The compute type of the listener.

This cannot be changed (`PUT`) once the listener is created.

Allowed value: `"k8s"`

compute\_id

string

required

User assigned unique ID of the compute infrastructure for the listener.

For example, if `compute_type` is `k8s`, then the user may set this field to the Kubernetes cluster name. This cannot be changed (`PUT`) once the listener is created.

compute\_config

ListenerComputeConfig · object

required

Fields for a listener that are specific to `compute_type`.

All fields are nullable, but are validated based on `compute_type`.

Show child attributes

id

string<uuid>

required

System assigned ID of the listener.

This is a read-only field.

created\_at

string<date-time>

required

The creation time of the listener.

This is a read-only field.

updated\_at

string<date-time>

required

The last update time of the listener.

This is a read-only field.

version

string | null

The version of the listener.