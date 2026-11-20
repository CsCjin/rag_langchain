---
title: "BYOC shared responsibility model - Docs by LangChain"
url: https://docs.langchain.com/langsmith/byoc-shared-responsibility
scraped_at: 2026-11-15T03:38:30.022031
word_count: 1598
---

The BYOC shared responsibility model defines what LangChain manages and what your organization manages in a LangSmith BYOC deployment. Under this model, sensitive data does not transit LangChain infrastructure during normal operation. The sections below cover this division across platform and infrastructure, data and security, and operations and support.
For the multi-tenant SaaS equivalent, see the [LangSmith shared responsibility model](/langsmith/shared-responsibility-model). For the technical structure of the control plane and data plane, see [BYOC architecture](/langsmith/byoc-architecture-aws).

## Access model

* **Control plane and data plane are split**: LangChain runs the control plane. You own the cloud environment that contains the data plane, and LangChain manages the infrastructure inside that environment through delegated access.
* **Access is least privilege, with break-glass as the exception**: The routine access LangChain holds is scoped to provisioning and operations. Data access is not required for normal operations. Incident troubleshooting may require customer-approved break-glass access, granted through the shared support channel.
* **You remain accountable for your cloud account**: You control your cloud account or subscription governance, network connectivity, and internal access policies.

For GCP project access and networking requirements, see [GCP onboarding](/langsmith/byoc-onboarding-gcp).
For Azure resource group access, Key Vault setup, and networking requirements, see [Azure onboarding](/langsmith/byoc-onboarding-azure). For Azure resources and permissions, see [Azure architecture](/langsmith/byoc-architecture-azure).

## Platform and infrastructure

| Area | LangChain responsibilities | Your responsibilities |
| --- | --- | --- |
| **Service scope and architecture** | * Define the BYOC architecture * Operate the control plane, covering organization configuration, authentication, billing metadata, and frontend assets | * Get sign-off from your security, infrastructure, and application teams * Confirm the BYOC architecture meets your requirements |
| **Cloud account ownership** | * Operate only through customer-delegated roles and in-scope permissions | * Own your cloud accounts or subscriptions and budgets * Own account guardrails, such as service control policies on AWS * Own organization structure and account lifecycle |
| **Provisioning and changes** | * Provision the BYOC infrastructure and Kubernetes resources that run the LangSmith data plane * Manage updates and rollouts for BYOC-managed components * Acknowledge and schedule change requests through the shared support channel | * Approve onboarding steps and provide the required account and region details * Avoid manual edits to BYOC-managed resources * Request changes through the shared support channel |
| **Networking** | * Configure LangSmith components for the supported connectivity model, such as PrivateLink * Communicate the required endpoints and constraints | * Own the internal connectivity your users and applications need to reach the LangSmith BYOC data plane |
| **Control plane** | * Operate authentication, organization configuration, and API key management * Serve the static frontend assets and operate the usage and billing surfaces | * Manage organization-level admins and govern who can create and manage data planes and workspaces |
| **Data plane services** | * Operate the services that ingest and query traces, prompts, datasets, evaluations, insights, and deployments * Keep those services healthy through monitoring, scaling, and upgrades | * Do not co-locate unrelated workloads in the BYOC cluster or private network * Validate application behavior in your environment |
| **Scaling and capacity** | * Monitor and scale BYOC-managed services * Give advance notice before material scaling events where possible, with the expected cost impact | * Ensure cloud service quotas are high enough for the deployed services, and request increases as needed * Accept the cost implications in your cloud account * Define internal cost guardrails and alerts |
| **Upgrades and patching** | * Roll out upgrades and patches to BYOC-managed components * Coordinate for major changes and maintenance windows | * Plan change management internally, including stakeholder communication and staging validation * Follow your own change control processes |

For details on how upgrades, autoscaling, and maintenance windows work, see [BYOC operations](/langsmith/byoc-operations-aws).

On AWS, with [BYOVPC](/langsmith/byoc-byovpc-aws), you also create and maintain:

* VPC
* Subnets
* Routes,
* Gateways
* Customer-side VPC endpoints
* Flow logs
* Egress controls

LangChain validates the supplied network before provisioning and manages the workload infrastructure inside it. Customer-managed network resources remain your responsibility during operation and after data plane deletion.

## Data and security

| Area | LangChain responsibilities | Your responsibilities |
| --- | --- | --- |
| **Customer data** | * Design the system so that sensitive data does not transit LangChain infrastructure for normal operation * Avoid access to customer data in normal operation | * Own the data in the data plane, including classification, retention, and access controls * Own the legal and compliance obligations for that data * Approve any data export or sharing internally |
| **Data residency** | * Provision all data plane components and storage only within the cloud region you designate * Keep customer data out of LangChain-managed infrastructure during normal operation | * Specify the required cloud region at onboarding * Communicate any change to your data residency requirements in advance |
| **Secrets management** | * Use secret stores in the customer account for runtime secrets * Reference secrets without persisting sensitive values in the control plane | * Apply any organization-specific key management requirements |
| **Break-glass access** | * Use break-glass access only for incident mitigation, with customer approval and a defined process * Minimize the duration and scope of that access * Give advance notice where possible * Deliver a post-access summary covering timestamps, actions taken, and any data accessed | * Approve break-glass access when it is required * Define the internal approval workflow * Review post-incident access logs and notes |
| **Access audit logs** | * Provision the logging infrastructure in your account so LangChain access is recorded, including EKS audit logs * Do not view, analyze, or alert on those logs on your behalf | * Retain AWS CloudTrail and account-level logs for all LangChain-assumed roles * View and analyze those logs, and set up your own alerting on them * Escalate anomalies to LangChain through the shared support channel |
| **Security incident notification** | * Notify you of a confirmed security incident in LangChain-owned infrastructure that affects your deployment, covering the control plane, corporate systems, and the BYOC build and release pipeline * Share the incident scope, impact assessment, and remediation steps * Cooperate on joint forensics * Do not run security monitoring inside your cloud account | * Deploy and operate security monitoring for the BYOC components in your account, such as EDR, IDS, container security, cloud security posture management, and log aggregation * Keep that monitoring from affecting the operation of BYOC-managed resources * Designate a security contact and define internal incident response procedures * Notify LangChain promptly of any suspected compromise of customer-side credentials or access |
| **Compliance and audits** | * Provide documentation on the BYOC architecture and operational model * Supply audit evidence for LangChain-operated controls, including access logs, change history, security policies, and penetration test summaries * Support SOC 2, ISO 27001, and equivalent audit programs | * Own the compliance posture of your cloud environment and all customer-managed controls * Run or coordinate audits and evidence collection for that environment |

The IAM permissions that scope LangChain access are described in [Cross-account IAM permissions](/langsmith/byoc-architecture-aws#cross-account-iam-permissions). For how break-glass access works in practice, see [Troubleshooting](/langsmith/byoc-operations-aws#troubleshooting). For where the audit logs live and how to access them, see [Auditing](/langsmith/byoc-operations-aws#auditing).

## Operations and support

| Area | LangChain responsibilities | Your responsibilities |
| --- | --- | --- |
| **Observability** | * Provide and operate service-level monitoring and alerts for BYOC-managed components * Request customer-provided signals when they are needed for diagnosis | * Provide requested logs, metrics, and timestamps from your own systems * Provide the same from your networking layers when troubleshooting requires it |
| **Incident response and support** | * Act as primary responder for LangChain-managed components, covering the control plane and the BYOC-managed data plane services * Coordinate communication through the shared support channel | * Act as primary responder for customer-owned layers, including cloud policies, internal networking, and access controls * Provide timely access and approvals for investigation |
| **Backup and disaster recovery** | * Define and operate backup processes for LangChain-managed data plane components * Provision data planes for high availability across multiple availability zones in a single region | * Define your internal recovery objectives and validate them with the LangChain team * Own backups for any customer-managed data stores outside the BYOC scope |
| **Maintenance windows and change freezes** | * Perform infrastructure maintenance and upgrades inside the agreed maintenance window * Act outside that window only when a change is required to keep the data plane functioning correctly, such as under increased load * Accommodate requested change freezes for sensitive business periods, with reasonable advance notice | * Set an AWS maintenance window in the LangSmith UI, or use the API for GCP and Azure * Communicate upcoming change freezes, such as fiscal close or major releases, with reasonable advance notice |
| **Offboarding and termination** | * Remove all LangChain-managed resources, IAM roles, and delegated access within the agreed timeframe on contract termination * Provide written confirmation that deprovisioning is complete | * Initiate offboarding through the shared support channel * Verify resource and access cleanup after confirmation * Revoke customer-managed roles and access grants tied to BYOC |

## See also

* [BYOC architecture](/langsmith/byoc-architecture-aws)
* [BYOC operations](/langsmith/byoc-operations-aws)
* [BYOC FAQ](/langsmith/byoc-faq)
* [LangSmith shared responsibility model](/langsmith/shared-responsibility-model)

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/byoc-shared-responsibility.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).