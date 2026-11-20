---
title: "Managed Deep Agents quickstart - Docs by LangChain"
url: https://docs.langchain.com/langsmith/python/managed-deep-agents-quickstart
scraped_at: 2026-11-15T03:39:42.972478
word_count: 1205
---

Create and deploy your first Managed Deep Agent: scaffold a project, configure the model and instructions, add search, test in [LangSmith Studio](/langsmith/studio), and deploy with the [`mda` CLI](/langsmith/python/managed-deep-agents-cli). Managed Deep Agents supplies the [Deep Agents harness](/oss/python/deepagents/overview) and hosted runtime.
After this quickstart, the [tutorial](/langsmith/python/managed-deep-agents-tutorial) adds durable memory and a daily schedule on the same project.

Managed Deep Agents is in **public [beta](/langsmith/release-stages)** on [LangSmith Cloud](/langsmith/cloud) and [Bring Your Own Cloud (BYOC)](/langsmith/byoc). Use Managed Deep Agents CLI and SDK v0.10 or later for BYOC.

## Prerequisites

To follow along, you need:

* Python and `uv`.
* An API key for your model provider of choice.

## Add the `managed-deep-agents` skill

The [`managed-deep-agents` skill](https://github.com/langchain-ai/langchain-skills/blob/main/config/skills/managed-deep-agents/SKILL.md) walks a coding agent through building, testing, and deploying a Managed Deep Agent with the `mda` CLI. To add it to the current project, run:

```
npx skills add langchain-ai/langchain-skills --skill managed-deep-agents --yes
```

Or paste this prompt into your coding agent:

Build a Managed Deep Agent with the quickstart

CopiedCopy prompt

## Create and deploy an agent

1

Set up the project

Create a project and open its directory:

```
uvx --from managed-deepagents mda init research-assistant
cd research-assistant
```

You now have all the scaffolding for your agent.

2

Add your keys

Add your model provider API key to `.env`:

.env

```
OPENAI_API_KEY=<OPENAI_API_KEY>
# ANTHROPIC_API_KEY=<ANTHROPIC_API_KEY>
# GOOGLE_API_KEY=<GOOGLE_API_KEY>
# AZURE_AI_OPENAI_ENDPOINT=https://<resource>.services.ai.azure.com/openai/v1
# AZURE_OPENAI_API_KEY=<AZURE_OPENAI_API_KEY>
# AZURE_OPENAI_DEPLOYMENT_NAME=<AZURE_OPENAI_DEPLOYMENT_NAME>
```

This quickstart uses OpenAI by default. For Google, Anthropic, or Microsoft Foundry, set the matching values instead. `mda deploy` adds the provider key to the deployment. You can also use any [other chat provider](/oss/python/integrations/chat/).

Do not commit the `.env` file into version control. It contains secrets.

3

Set up LangSmith

Managed Deep Agents runs on LangSmith. Your LangSmith API key authenticates local development with `mda dev`, deploys the agent with `mda deploy`, and opens the agent in [LangSmith Studio](/langsmith/studio) so you can chat with it and inspect traces.[Sign up for LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=langsmith-managed-deep-agents-quickstart) if you do not already have an account.To create a LangSmith API key, open [Settings](https://smith.langchain.com/settings), go to **API Keys**, and click **Create API Key**. For more details, see [Create an account and API key](/langsmith/create-account-api-key).On [BYOC](/langsmith/byoc), sign in to your own data plane and create the key there. Set `LANGSMITH_ENDPOINT` to the data plane’s API URL as well. See [Select a BYOC data plane](/langsmith/python/managed-deep-agents-deploy#select-a-byoc-data-plane).Add your LangSmith API key to `.env`:

.env

```
LANGSMITH_API_KEY=<LANGSMITH_API_KEY>
```

4

Edit the instructions

Open `instructions.md` and describe how the agent should behave:

instructions.md

```
# Research assistant

You are a careful research assistant. Use internet search to find sources,
keep notes, and return concise answers with citations.
```

When you deploy, Managed Deep Agents syncs these instructions to [LangSmith Context Hub](/langsmith/python/managed-deep-agents-context-hub), where you can update them without redeploying the agent.

5

Configure your model and search

Now set the model and a built-in web search tool. Google, OpenAI, Anthropic, and Microsoft Foundry offer server-side search without a separate search package or search API key. Pass the provider tool dict that matches your model:Open `agent.py`:

OpenAI

Google

Anthropic

Microsoft Foundry

```
from managed_deepagents import define_deep_agent

# OpenAI's built-in web search — no extra install or API key needed
agent = define_deep_agent(
    name="research-assistant",
    model="openai:gpt-6.1-sol",
    tools=[{"type": "web_search"}],
)
```

```
from managed_deepagents import define_deep_agent

# Google's built-in search — no extra install or API key needed
agent = define_deep_agent(
    name="research-assistant",
    model="google_genai:gemini-4-hydrogen",
    tools=[{"google_search": {}}],
)
```

```
from managed_deepagents import define_deep_agent

# Anthropic's built-in web search — no extra install or API key needed
agent = define_deep_agent(
    name="research-assistant",
    model="anthropic:claude-sonnet-4-6",
    tools=[{"type": "web_search_20260209", "name": "web_search"}],
)
```

```
# Install the required dependency: uv add langchain-azure-ai
import os

from langchain_azure_ai.chat_models import AzureAIOpenAIApiChatModel
from managed_deepagents import define_deep_agent

model = AzureAIOpenAIApiChatModel(
    endpoint=os.environ["AZURE_AI_OPENAI_ENDPOINT"],
    credential=os.environ["AZURE_OPENAI_API_KEY"],
    model=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
)

agent = define_deep_agent(
    name="research-assistant",
    model=model,
    tools=[{"type": "web_search"}],
)
```

The agent name is also the default deployment name. For model concepts and provider options, see [Models](/oss/python/langchain/models).

Using another provider?

You can use a Tavily search tool instead. Store the key in a [connection](/langsmith/python/managed-deep-agents-connections) so it lives in your LangSmith workspace rather than the project.This accordion uses the connection slug `research-tavily`. For `mda dev`, an agent-owned connection reads its value from `MDA_DEV_<SLUG>`. Add a [Tavily API key](https://app.tavily.com) to `.env` as `MDA_DEV_RESEARCH_TAVILY`:

.env

```
MDA_DEV_RESEARCH_TAVILY=<TAVILY_API_KEY>
```

Install the Tavily client:

```
uv add tavily-python
```

Create a custom `internet_search` tool. `connections.get(...)` resolves the key at runtime, so the tool code is the same locally and on the deployment:

tools/search.py

```
from typing import Literal

from langchain.tools import tool
from managed_deepagents import connections
from tavily import AsyncTavilyClient

@tool
async def internet_search(
    query: str,
    max_results: int = 5,
    topic: Literal["general", "news", "finance"] = "general",
) -> dict:
    """Search the internet for relevant sources."""
    api_key = await connections.get("research-tavily", {"type": "agent"})
    tavily_client = AsyncTavilyClient(api_key=api_key)
    return await tavily_client.search(
        query,
        max_results=max_results,
        topic=topic,
    )
```

Import the tool and add it to the agent:

agent.py

```
from managed_deepagents import define_deep_agent

from tools.search import internet_search

agent = define_deep_agent(
    name="research-assistant",
    model="openai:gpt-6.1-sol",
    tools=[internet_search],
)
```

After you deploy in the agent in the next step, create the agent-owned connection. Agent-owned credentials belong to the deployment, so this command comes after the first successful deploy:

```
uv run mda connections create research-tavily --secret-from-env MDA_DEV_RESEARCH_TAVILY
```

Rotating this value later takes effect on the next run, with no redeploy. For more authored tools, see [Custom tools](/langsmith/python/managed-deep-agents-tools). For other create modes and per-caller credentials, see [Manage connections](/langsmith/python/managed-deep-agents-connections).

6

Run locally

Install the project dependencies and start the agent:

```
uv sync
uv run mda dev
```

`mda dev` loads the API keys from `.env`, starts a local Agent Server, and opens the agent in LangSmith Studio.In Studio, send:

```
What were the main announcements from the latest LangChain release?
```

You should see the agent call the web search tool, then return a concise answer that cites sources. If search never appears in the trace, confirm the provider tool dict matches the model you set in `agent.py` or `agent.ts`.In an [agent-based workspace](/langsmith/agent-registry), tracing will result in errors until you register the agent. For details, see [Trace local runs](/langsmith/python/managed-deep-agents-local-development#trace-local-runs).

7

Deploy the agent

On [BYOC](/langsmith/byoc), add `--push-to <image-repository>` to every command in this step. A BYOC data plane deploys from an image in a registry you manage.Deploy the project by running:

```
uv run mda deploy
```

Managed Deep Agents packages the project and runs it as a hosted deployment on [LangSmith Agent Server](/langsmith/agent-server). When deployment finishes, the CLI prints the deployment dashboard URL.Open that URL. You should see the deployment in a ready state. Send the same research question from the previous step and confirm the hosted agent returns an answer with a search tool call. For deployment options and secrets handling, see [Deploy a Managed Deep Agent](/langsmith/python/managed-deep-agents-deploy). To inspect the agent’s execution after it runs, use [LangSmith observability](/langsmith/observability-quickstart).

## Next steps

## Tutorial

Add a custom Tavily search tool, durable memory, and a daily schedule.

## Design agent template

Deploy LangChain’s open-source design agent instead of scaffolding from scratch.

## Paid media agent template

Deploy LangChain’s open-source paid media agent for Slack campaign analysis.

## Custom tools

Add authored LangChain tools from your project.

## Connections

Authenticate with external services, as the agent or as the caller.

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).