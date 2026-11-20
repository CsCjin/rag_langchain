---
title: "Set up LangSmith - Docs by LangChain"
url: https://docs.langchain.com/langsmith/platform-setup
scraped_at: 2026-11-15T03:39:33.931103
word_count: 449
---

Set up **LangSmith** for [observability](/langsmith/observability), [evaluation](/langsmith/evaluation), and [prompt engineering](/langsmith/prompt-context-hub#prompts). LangSmith offers Cloud, Bring Your Own Cloud (BYOC), and Self-hosted options. Choose the option that matches where your data has to live and who runs the infrastructure.

If you also want to deploy agents in production, you can use [**LangSmith Agent Server**](/langsmith/deployment) with Cloud, BYOC, or Self-hosted.

## Cloud

Fully managed observability, evaluation, and prompt engineering.

Get started

## BYOC

Full control over your data, while LangChain manages the infrastructure.

Learn about BYOC

## Self-hosted

Full control with observability, evaluation, and prompt engineering in your infrastructure.

Run self-hosted

Self-hosted and BYOC are available on the [Enterprise plan](/langsmith/pricing-plans). [Get a demo](https://www.langchain.com/contact-sales) to learn more.

## Compare Cloud, BYOC, and Self-hosted

| Feature | **Cloud** | **BYOC** | **Self-hosted** |
| --- | --- | --- | --- |
| **Who runs the infrastructure** | LangChain | LangChain runs the control plane, you run your data planes | You |
| **Where sensitive data lives** | LangChain’s cloud | Your VPC | Your VPC |
| **Upgrades and patches** | Automatic | Automatic | Manual |
| **Scaling** | Automatic | Automatic, managed by LangChain | Manual |

[Managed Deep Agents](/langsmith/python/managed-deep-agents-overview) is available in public beta on Cloud and BYOC. For BYOC, use Managed Deep Agents CLI and SDK v0.10 or later.
Cloud, BYOC, and Self-hosted support [LangSmith Agent Server](/langsmith/deployment) for agent workloads. Refer to the [LangSmith Agent Server overview](/langsmith/deployment) to pick a topology (Cloud managed, BYOC, Hybrid, self-hosted with control plane, or standalone).

## Common setups

* **Fastest to start, managed everything.** [LangSmith Cloud](/langsmith/cloud) paired with [LangSmith Agent Server](/langsmith/deployment) on Cloud. LangChain hosts the platform, and, when you use LangSmith Agent Server, also hosts your [Agent Servers](/langsmith/agent-server).
* **Bring Your Own Cloud.** Data stays in your VPC, and LangChain manages the infrastructure. Refer to the [BYOC overview](/langsmith/byoc).
* **Observability data must stay in your infrastructure.** Self-hosted LangSmith, paired with any Agent Server hosting topology, including [self-hosted Agent Server hosting](/langsmith/deploy-with-control-plane) for agent workloads.
* **Managed observability, agents in your VPC.** LangSmith Cloud paired with [Hybrid](/langsmith/hybrid) LangSmith Agent Server. Traces and evaluations stay on SaaS while agent workloads stay in your infrastructure.
* **Observability only, no agent hosting.** LangSmith Cloud or self-hosted, without Agent Server hosting. Run your agents wherever you already run apps and send traces to LangSmith.

## Related

## Account setup

Create an account, manage API keys, and choose a pricing tier.

Set up your account

## Plans and pricing

Compare LangSmith plans and tiers.

View pricing

## Observability

Trace and monitor your LLM applications.

Learn more

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/platform-setup.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).