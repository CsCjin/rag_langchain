---
title: "Deploy to self-hosted - Docs by LangChain"
url: https://docs.langchain.com/langsmith/deploy-to-self-hosted-overview
scraped_at: 2026-11-15T03:38:45.417444
word_count: 479
---

Self-hosted Agent Server hosting runs [LangSmith Agent Server](/langsmith/agent-server) and its supporting databases inside infrastructure that you operate. With a full self-hosted LangSmith installation, you also run the control plane and data plane listener.
LangChain ships the container images, Helm charts, and license; you provide the Kubernetes cluster (or Docker host), PostgreSQL, Redis, and the networking and observability tooling that fit your environment. Self-hosted is the best deployment option when you have data residency, regulatory constraints, custom networking, or air-gapped requirements.

Self-hosted deployments require an [Enterprise plan](https://www.langchain.com/pricing) and the LangSmith license key delivered with that plan. For a setup guide, see [Self-hosted LangSmith](/langsmith/self-hosted).

## Topologies

LangSmith supports three self-hosted topologies that trade off setup complexity against control-plane features. Reference pages for [platform features](/langsmith/self-hosted-platform-features), [Agent Server metrics](/langsmith/self-hosted-agent-server-metrics), and [diagnostics](/langsmith/diagnostics-self-hosted) apply to all three.

## Full self-hosted platform

The complete LangSmith platform—[control plane](/langsmith/control-plane) UI and APIs, [data plane](/langsmith/data-plane) listener, observability, evaluation, and agent deployment management. Best for teams that want the LangSmith product experience inside their own network.

## Hybrid

LangChain-hosted control plane with the data plane (Agent Servers and databases) in your infrastructure. Best when you want managed deployment workflows but need agent workloads and customer data to stay inside your VPC.

## Standalone server

The lightest option—Agent Server containers (API + queue workers) with your own PostgreSQL and Redis. No control plane, no managed UI. Best for embedding the runtime into existing infrastructure or running air-gapped.

## Platform features

Reference for self-hosted-only platform behavior: custom Postgres and Redis, listeners, and resource customization.

## Agent Server metrics

Prometheus and Datadog export for Agent Server, including Agent Server UI metrics and internal metrics.

## Diagnostics

Collect logs, inspect state, and troubleshoot a self-hosted installation.

## Who manages what

Self-hosted shifts ownership of infrastructure operations from LangChain to your team, which provides flexibility and control over how you configure and operate is layer:

|  | **Who manages it** | **Where it runs** |
| --- | --- | --- |
| LangSmith platform (UI, APIs, datastores) | You | Your infrastructure |
| Agent Server runtime | You | Your infrastructure |
| PostgreSQL and Redis | You | Your infrastructure |
| CI/CD for your apps | You | Your CI environment |
| Upgrades, scaling, and backups | You | Your infrastructure |

In return, you can integrate with your own [Postgres](/langsmith/self-hosted-platform-features#custom-postgresql) and [Redis](/langsmith/self-hosted-platform-features#custom-redis), size [CPU and memory](/langsmith/self-hosted-platform-features#resource-customization) for your workload, and operate inside your existing network and observability stack. For the corresponding Cloud-managed model, see [Deploy to Cloud](/langsmith/deploy-to-cloud-overview).

## Next steps

## Pick a topology

Compare standalone server, full platform, and hybrid to find the right fit.

## Enable Agent Server hosting

Add a control plane and data plane to deploy and manage agents on self-hosted LangSmith.

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deploy-to-self-hosted-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).