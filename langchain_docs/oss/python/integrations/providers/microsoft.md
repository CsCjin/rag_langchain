---
title: "Microsoft integrations - Docs by LangChain"
url: https://docs.langchain.com/oss/python/integrations/providers/microsoft
scraped_at: 2026-11-15T03:44:49.828112
word_count: 1146
---

Browse LangChain Python integrations for [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/) and [Azure](https://azure.microsoft.com/). For package selection, shared Azure setup, memory, vector stores, and hosted agents, see [Azure AI integrations](/oss/python/integrations/providers/azure_ai).

**Recommended: Microsoft Foundry**For new LangChain, LangGraph, or Deep Agents applications centered on [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/), start with [`langchain-azure-ai`](/oss/python/integrations/providers/azure_ai). It adds Foundry project endpoints, Azure credential integration, Agent Service, hosting, tools, Content Safety, retrieval, and Azure observability.For direct [Azure OpenAI v1 API](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?tabs=python) model access, code that switches between OpenAI and Azure, traditional Azure OpenAI API versions, completion LLMs, or a smaller dependency surface, use the `langchain-openai` package.

## Explore integrations

### Chat models

Choose an integration to call chat models:

* **Microsoft Foundry (recommended)**: To call models in Microsoft Foundry, use `AzureAIOpenAIApiChatModel` from `langchain-azure-ai`. It handles project endpoint resolution and Microsoft Entra ID authentication through Azure credentials.
* **Azure OpenAI**: Use `ChatOpenAI` from `langchain-openai` for direct v1 API calls or code shared between OpenAI and Azure. Use `AzureChatOpenAI` for traditional dated Azure OpenAI API versions.

**Claude on Azure**Microsoft Foundry also offers access to all [Anthropic Claude models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude), including Opus, Sonnet, and Haiku. Claude models are served through a dedicated Anthropic-native endpoint rather than the Azure OpenAI v1 API. Prefer `AzureAIAnthropicChatModel` from `langchain-azure-ai` for Foundry project endpoints and Microsoft Entra ID. You can also use [`ChatAnthropic`](/oss/python/integrations/chat/anthropic) from `langchain-anthropic` pointed at your Foundry Anthropic endpoint.

## Microsoft Foundry

Use `langchain-azure-ai` to call models deployed in Microsoft Foundry through LangChain’s chat model interface.

Get started

## Azure OpenAI (chat models)

Use `langchain-openai` to call Azure OpenAI models through LangChain’s chat model interface.

Get started

#### Call a model

Call a model deployed in your Foundry project. Install `langchain-azure-ai` and set `AZURE_AI_PROJECT_ENDPOINT` and `AZURE_AI_MODEL_DEPLOYMENT_NAME`.
Configure Microsoft Entra ID authentication for your environment. On Azure, use a managed identity. For local development, you can sign in with `az login`.

```
import os

from azure.identity import DefaultAzureCredential
from langchain_azure_ai.chat_models import AzureAIOpenAIApiChatModel

model = AzureAIOpenAIApiChatModel(
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=DefaultAzureCredential(),
)
model.invoke("Tell me a joke and include some emojis.").pretty_print()
```

For setup and usage examples, see [Microsoft Foundry chat models](/oss/python/integrations/chat/azure_ai).

### LLMs

## Azure OpenAI (text completions)

Call Azure OpenAI text-completion models through LangChain’s LLM interface.

Get started

### Agents

Use an existing Foundry agent as a node in your LangGraph workflow. To host a new LangGraph agent on Microsoft Foundry, see [Runtime](#runtime).

## Microsoft Foundry Agent Service

Use `langchain-azure-ai` to invoke Foundry Agent Service agents as nodes in a LangGraph workflow.

Get started

#### Use an existing Foundry agent

Install `langchain-azure-ai` and set `AZURE_AI_PROJECT_ENDPOINT`. Configure Microsoft Entra ID authentication for your environment. Replace `my-echo-agent` with your agent name.

```
from langchain_azure_ai.agents import (
    AgentServiceAgentState,
    AgentServiceFactory,
)
from langgraph.graph import END, START, StateGraph

factory = AgentServiceFactory()
agent_node = factory.get_agent_node(
    name="my-echo-agent", version="latest"
)

workflow = StateGraph(AgentServiceAgentState)
workflow.add_node("foundry_agent", agent_node)
workflow.add_edge(START, "foundry_agent")
workflow.add_edge("foundry_agent", END)

graph = workflow.compile()
result = graph.invoke({"messages": [("user", "Hello, world!")]})
result["messages"][-1].pretty_print()
```

For more on using Foundry agents in LangGraph, see [Microsoft Foundry Agent Service](https://github.com/langchain-ai/langchain-azure/blob/main/libs/azure-ai/README.md#microsoft-foundry-agent-service).

### Runtime

[Microsoft Foundry hosted agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents) run your LangGraph code on managed infrastructure. Foundry manages compute, session lifecycles, and scaling. Responses hosting options can enable background execution, failure recovery after process interruptions, stream replay, and steering for new user input. These options are off by default.
Expose your agent through OpenAI-compatible Responses endpoints or Invocations endpoints with custom JSON inputs and outputs. The LangGraph hosting adapters handle request conversion, response mapping, and streaming. Responses also provides managed conversation history.
Hosted agents can call Foundry models and Toolbox tools with a dedicated Microsoft Entra agent identity. Foundry also supports RBAC, private networking, and Content Safety guardrails. Application Insights tracing helps investigate failures.

## Microsoft Foundry hosted agents

Deploy LangGraph applications to Microsoft Foundry as hosted agents.

Get started

## Azure Durable Task Scheduler

Add durable execution, retries, and crash recovery to LangGraph workflows.

Get started

#### Host a LangGraph agent

Run an existing compiled LangGraph graph locally with `langchain-azure-ai[hosting]`. From your configured project directory, point `langgraph.json` at the exported graph. Set the Foundry project endpoint and model deployment name, then start the Responses endpoint:

```
pip install -U "langchain-azure-ai[hosting]"
export FOUNDRY_PROJECT_ENDPOINT="https://<account>.services.ai.azure.com/api/projects/<project>"
export AZURE_AI_MODEL_DEPLOYMENT_NAME="<model-deployment-name>"
python -m langchain_azure_ai.agents.hosting.run --protocol responses
```

To deploy, use `azd ai agent init` to initialize a hosted-agent project with the same hosting entry point in `azure.yaml`, `azd ai agent run` to test locally, and `azd deploy` to deploy. Run `azd provision` first only when you need to create the Foundry project or other Azure resources:

```
azd ext install azure.ai.agents
azd auth login
azd ai agent init
azd ai agent run
azd provision
azd deploy
```

For project configuration and deployment steps, see [Microsoft Foundry hosted agents](/oss/python/integrations/providers/azure_ai#microsoft-foundry-hosted-agents).

### Tools

## Azure AI services

Use Azure AI services for document analysis, image analysis, and speech processing.

Get started

## Microsoft Foundry built-in tools

Use built-in tools for web search, file search, code execution, and image generation.

Get started

## Microsoft Foundry Toolbox

Access built-in tools, tools from MCP servers, and skills through Microsoft Foundry Toolbox.

Get started

## Azure Logic Apps

Let agents invoke Azure Logic Apps workflows as tools.

Get started

### Middleware

## Azure AI Content Safety

Apply Content Safety checks to agent inputs and outputs.

Get started

### Sandboxes

## Azure Container Apps dynamic sessions

Run Python code in ephemeral Azure Container Apps sessions.

Get started

## Azure Container Apps sandboxes

Use `langchain-azure-compute[sandboxes]` to give Deep Agents stateful workspaces on Azure Container Apps.

Get started

### Backends

## Azure Blob Storage

Persist Deep Agents workspace files in Azure Blob Storage.

Get started

### Retrievers

## Azure AI Search

Retrieve documents from an existing Azure AI Search index.

Get started

### Embedding models

## Microsoft Foundry

Generate text embeddings with models deployed in Microsoft Foundry.

Get started

## Azure OpenAI

Generate text embeddings with models deployed in Azure OpenAI.

Get started

### Vector stores

## Azure Cosmos DB for MongoDB vCore

Store embeddings and search documents in Azure Cosmos DB for MongoDB vCore.

Get started

## Azure Cosmos DB for NoSQL

Store embeddings and search documents in Azure Cosmos DB for NoSQL.

Get started

## Azure Database for PostgreSQL

Run vector search in Azure Database for PostgreSQL with DiskANN indexing.

Get started

## Azure SQL Database

Store and query vector embeddings in Azure SQL Database.

Get started

## pgvector

Store embeddings and search PostgreSQL data with the pgvector extension.

Get started

## Azure AI Search

Store embeddings and run vector, hybrid, and semantic searches in Azure AI Search.

Get started

### Chat message history

## Azure Cosmos DB (chat message history)

Persist and retrieve conversation messages in Azure Cosmos DB.

Get started

### Caches

## Azure Cosmos DB (semantic cache)

Reuse cached model responses for semantically similar prompts with Azure Cosmos DB.

Get started

### Document loaders

## Azure Blob Storage

Load files from Azure Blob Storage as LangChain documents.

Get started

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/microsoft.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).