---
title: "Connect Managed Deep Agents to channels - Docs by LangChain"
url: https://docs.langchain.com/langsmith/python/managed-deep-agents-channels
scraped_at: 2026-11-15T03:39:37.827021
word_count: 478
---

A channel makes a managed deep agent available in an external messaging service. Messages from the service can start agent runs, and the agent’s final responses return through the same service.

Managed Deep Agents is in **public [beta](/langsmith/release-stages)** on [LangSmith Cloud](/langsmith/cloud) and [Bring Your Own Cloud (BYOC)](/langsmith/byoc). Use Managed Deep Agents CLI and SDK v0.10 or later for BYOC.

## Project structure

Channel declarations live in the project-level `channels/` directory:

```
my-agent/
  agent.py
  channels/
    slack.py
```

## Understand channels

A channel combines three parts of an external messaging integration:

* **Inbound events**: Verify and normalize provider events, then start an agent run.
* **Outbound messaging**: Send the agent’s response back to the originating conversation.
* **Provisioning**: Create and configure the provider resources that connect the service to the deployed agent.

In Managed Deep Agents, a channel connects a deployed agent to a messaging provider.
The managed runtime handles the channel lifecycle:

Provider adapters determine which events are accepted, how provider conversations map to Managed Deep Agents threads, and how responses are delivered. The channel declaration exposes the supported configuration for that provider.

### Send messages to a running agent

Steering lets a user add to a run that is already in progress. When the same user sends a message while the agent runs on that thread, the message joins the active run at its next model call. It does not start a new run.

Steering is in beta and requires `managed-deepagents` 0.10.2 or later.

## Declare channels in a project

Put each channel in a separate module under `channels/`.
Export a module-level `channel` from each file.
The file name becomes the configured channel name and identifies the channel within the deployment.
Do not name a declaration `channels/channel.py`.
Channel names must be unique within a project.
The provider factory creates the declaration.
For example, `channels.slack()` creates a Slack channel.
See the provider guide for its declaration, app configuration, and deployment procedure.

## Distinguish channels from connectors

A channel receives messages that start agent runs and delivers responses. An [MCP connector](/langsmith/python/managed-deep-agents-mcp-connectors) gives the agent tools from a remote MCP server. A project can use either or both.

## Supported channels

## Slack

Start runs from Slack mentions, direct messages, and thread replies.

## Custom (HTTP)

Start runs from any service that can send a JSON webhook.

An HTTP adapter can also live in a community-maintained package. See [Share a channel adapter as a package](/langsmith/python/managed-deep-agents-channels-http#share-a-channel-adapter-as-a-package) to publish reusable provider code that users import into their channel declarations.

## See also

* [Identity](/langsmith/python/managed-deep-agents-identity): authenticate callers and scope channel runs to the resolved user.
* [Schedules](/langsmith/python/managed-deep-agents-schedules): deliver scheduled results through a configured channel.
* [Deploy an agent](/langsmith/python/managed-deep-agents-deploy): deploy project changes and configure secrets.
* [CLI reference](/langsmith/python/managed-deep-agents-cli): review channel project-file conventions.

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-channels.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).