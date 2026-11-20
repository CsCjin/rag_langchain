---
title: "Agent Server - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-overview
scraped_at: 2026-11-15T03:38:21.850563
word_count: 295
---

Configure and build applications on the [Agent Server](/langsmith/agent-server) runtime. Once deployed, agents work with three primitives: [**assistants**](/langsmith/assistants) for configuration, [**threads**](/langsmith/use-threads) for state, and [**runs**](/langsmith/runs) for workloads. The pages in this tab cover the capabilities Agent Server provides, how to [structure your application](/langsmith/application-structure), and how to [secure](/langsmith/auth) and [customize](/langsmith/custom-routes) the server.

## Capabilities

## Develop your application

Structure your app, configure dependencies for Python, JavaScript, and monorepos, and connect agents with RemoteGraph, semantic search, TTLs, and CI/CD.

Set up your project

## Agent Server runtime

Work with assistants, threads, runs, and cron jobs. Stream to users, pause for human review, handle concurrent input, and connect via MCP and A2A.

Explore the runtime

## Auth & access control

Authenticate users, enforce resource-level access, and connect external OAuth2 identity providers.

Secure your server

## Server customization

Add caching, custom stores and checkpointers, lifespan hooks, middleware, custom routes, encryption, and configurable headers and logs.

Customize your server

## REST API

Full REST API reference for assistants, threads, runs, crons, store, A2A, MCP, and system endpoints.

Browse the API

## Tutorials

* [Collect user feedback for Agent Server runs](/langsmith/agent-server-feedback): Attach end-user feedback to runs and traces
* [Deploy other frameworks (e.g., Strands, CrewAI)](/langsmith/deploy-other-frameworks): Wrap existing agents with Functional API and deploy
* [Implement generative user interfaces with LangGraph](/langsmith/generative-ui-react): Stream UI elements to a React client
* [Implement a CI/CD pipeline](/langsmith/cicd-pipeline-example): Automate tests, evaluations, and deployments with GitHub Actions

## Securing and customizing your server

* [Custom auth](/langsmith/auth): Authentication and multi-tenant access control
* [Server customization](/langsmith/custom-routes): Custom routes, [middleware](/langsmith/custom-middleware), [lifespan hooks](/langsmith/custom-lifespan), [encryption](/langsmith/encryption)

## Operations

* [CI/CD pipelines](/langsmith/cicd-pipeline-example)
* [TTL configuration](/langsmith/configure-ttl) for state and thread management
* [Semantic search](/langsmith/semantic-search)

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/agent-server-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).