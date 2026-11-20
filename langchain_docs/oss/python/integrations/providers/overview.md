---
title: "LangChain Python integrations - Docs by LangChain"
url: https://docs.langchain.com/oss/python/integrations/providers/overview
scraped_at: 2026-11-15T03:44:50.751214
word_count: 920
---

LangChain offers an extensive ecosystem with 1000+ integrations across chat & embedding models, tools & toolkits, document loaders, vector stores, and more.
A **provider** is a company or platform that hosts AI models and exposes them through an API (e.g., OpenAI, Anthropic, Google). Many providers have a dedicated `langchain-<provider>` package that implements one or more of LangChain’s standard interfaces—chat models, embedding models, vector stores, and more—giving you a consistent API regardless of the underlying provider. Install the package, pick a model name, and swap providers without changing your code.

## Chat models

## Embedding models

## Tools and toolkits

## Middleware

## Checkpointers

## Sandboxes

To see a full list of integrations by component type, refer to the categories in the sidebar.

For a conceptual overview of how providers and models work in LangChain, including how to find model names, use new models immediately, and work with routers—see [Providers and models](/oss/python/concepts/providers-and-models).

## Popular providers

| Provider | Package | Downloads | Latest version | JS/TS support |
| --- | --- | --- | --- | --- |
| [OpenAI](/oss/python/integrations/providers/openai/) | [`langchain-openai`](https://reference.langchain.com/python/langchain-openai) | [Downloads per month](https://pypi.org/project/langchain-openai/) | [PyPI - Latest version](https://pypi.org/project/langchain-openai/) | [✅](https://www.npmjs.com/package/@langchain/openai) |
| [Google (Gemini Enterprise Agent Platform)](/oss/python/integrations/providers/google) | [`langchain-google-vertexai`](https://reference.langchain.com/python/langchain-google-vertexai) | [Downloads per month](https://pypi.org/project/langchain-google-vertexai/) | [PyPI - Latest version](https://pypi.org/project/langchain-google-vertexai/) | [✅](https://www.npmjs.com/package/@langchain/google-vertexai) |
| [Anthropic (Claude)](/oss/python/integrations/providers/anthropic/) | [`langchain-anthropic`](https://reference.langchain.com/python/langchain-anthropic) | [Downloads per month](https://pypi.org/project/langchain-anthropic/) | [PyPI - Latest version](https://pypi.org/project/langchain-anthropic/) | [✅](https://www.npmjs.com/package/@langchain/anthropic) |
| [Google (GenAI)](/oss/python/integrations/providers/google) | [`langchain-google-genai`](https://reference.langchain.com/python/langchain-google-genai) | [Downloads per month](https://pypi.org/project/langchain-google-genai/) | [PyPI - Latest version](https://pypi.org/project/langchain-google-genai/) | [✅](https://www.npmjs.com/package/@langchain/google-genai) |
| [AWS](/oss/python/integrations/providers/aws/) | [`langchain-aws`](https://reference.langchain.com/python/langchain-aws) | [Downloads per month](https://pypi.org/project/langchain-aws/) | [PyPI - Latest version](https://pypi.org/project/langchain-aws/) | [✅](https://www.npmjs.com/package/@langchain/aws) |
| [Ollama](/oss/python/integrations/providers/ollama/) | [`langchain-ollama`](https://reference.langchain.com/python/langchain-ollama) | [Downloads per month](https://pypi.org/project/langchain-ollama/) | [PyPI - Latest version](https://pypi.org/project/langchain-ollama/) | [✅](https://www.npmjs.com/package/@langchain/ollama) |
| [Groq](/oss/python/integrations/providers/groq/) | [`langchain-groq`](https://reference.langchain.com/python/langchain-groq) | [Downloads per month](https://pypi.org/project/langchain-groq/) | [PyPI - Latest version](https://pypi.org/project/langchain-groq/) | [✅](https://www.npmjs.com/package/@langchain/groq) |
| [MistralAI](/oss/python/integrations/providers/mistralai/) | [`langchain-mistralai`](https://reference.langchain.com/python/langchain-mistralai) | [Downloads per month](https://pypi.org/project/langchain-mistralai/) | [PyPI - Latest version](https://pypi.org/project/langchain-mistralai/) | [✅](https://www.npmjs.com/package/@langchain/mistralai) |
| [LiteLLM](/oss/python/integrations/providers/litellm/) | [`langchain-litellm`](https://reference.langchain.com/python/langchain-litellm) | [Downloads per month](https://pypi.org/project/langchain-litellm/) | [PyPI - Latest version](https://pypi.org/project/langchain-litellm/) | N/A |
| [Huggingface](/oss/python/integrations/providers/huggingface/) | [`langchain-huggingface`](https://reference.langchain.com/python/langchain-huggingface) | [Downloads per month](https://pypi.org/project/langchain-huggingface/) | [PyPI - Latest version](https://pypi.org/project/langchain-huggingface/) | [✅](https://www.npmjs.com/package/@langchain/community) |
| [MongoDB](/oss/python/integrations/providers/mongodb_atlas) | [`langchain-mongodb`](https://reference.langchain.com/python/langchain-mongodb) | [Downloads per month](https://pypi.org/project/langchain-mongodb/) | [PyPI - Latest version](https://pypi.org/project/langchain-mongodb/) | [✅](https://www.npmjs.com/package/@langchain/mongodb) |
| [Chroma](/oss/python/integrations/providers/chroma/) | [`langchain-chroma`](https://reference.langchain.com/python/langchain-chroma) | [Downloads per month](https://pypi.org/project/langchain-chroma/) | [PyPI - Latest version](https://pypi.org/project/langchain-chroma/) | [✅](https://www.npmjs.com/package/@langchain/community) |
| [OpenRouter](/oss/python/integrations/providers/openrouter/) | [`langchain-openrouter`](https://reference.langchain.com/python/langchain-openrouter) | [Downloads per month](https://pypi.org/project/langchain-openrouter/) | [PyPI - Latest version](https://pypi.org/project/langchain-openrouter/) | ❌ |
| [xAI (Grok)](/oss/python/integrations/providers/xai/) | [`langchain-xai`](https://reference.langchain.com/python/langchain-xai) | [Downloads per month](https://pypi.org/project/langchain-xai/) | [PyPI - Latest version](https://pypi.org/project/langchain-xai/) | [✅](https://www.npmjs.com/package/@langchain/xai) |
| [DeepSeek](/oss/python/integrations/providers/deepseek/) | [`langchain-deepseek`](https://reference.langchain.com/python/langchain-deepseek) | [Downloads per month](https://pypi.org/project/langchain-deepseek/) | [PyPI - Latest version](https://pypi.org/project/langchain-deepseek/) | [✅](https://www.npmjs.com/package/@langchain/deepseek) |
| [Tavily](/oss/python/integrations/providers/tavily/) | [`langchain-tavily`](https://reference.langchain.com/python/langchain-tavily) | [Downloads per month](https://pypi.org/project/langchain-tavily/) | [PyPI - Latest version](https://pypi.org/project/langchain-tavily/) | [✅](https://www.npmjs.com/package/@langchain/tavily) |
| [Qdrant](/oss/python/integrations/providers/qdrant/) | [`langchain-qdrant`](https://reference.langchain.com/python/langchain-qdrant) | [Downloads per month](https://pypi.org/project/langchain-qdrant/) | [PyPI - Latest version](https://pypi.org/project/langchain-qdrant/) | [✅](https://www.npmjs.com/package/@langchain/qdrant) |
| [Fireworks](/oss/python/integrations/providers/fireworks/) | [`langchain-fireworks`](https://reference.langchain.com/python/langchain-fireworks) | [Downloads per month](https://pypi.org/project/langchain-fireworks/) | [PyPI - Latest version](https://pypi.org/project/langchain-fireworks/) | [✅](https://www.npmjs.com/package/@langchain/community) |
| [Cohere](/oss/python/integrations/providers/cohere/) | [`langchain-cohere`](https://reference.langchain.com/python/langchain-cohere) | [Downloads per month](https://pypi.org/project/langchain-cohere/) | [PyPI - Latest version](https://pypi.org/project/langchain-cohere/) | [✅](https://www.npmjs.com/package/@langchain/cohere) |
| [Nvidia AI Endpoints](/oss/python/integrations/providers/nvidia) | [`langchain-nvidia-ai-endpoints`](https://reference.langchain.com/python/langchain-nvidia-ai-endpoints) | [Downloads per month](https://pypi.org/project/langchain-nvidia-ai-endpoints/) | [PyPI - Latest version](https://pypi.org/project/langchain-nvidia-ai-endpoints/) | ❌ |
| [Azure AI](/oss/python/integrations/providers/azure_ai) | [`langchain-azure-ai`](https://reference.langchain.com/python/langchain-azure-ai) | [Downloads per month](https://pypi.org/project/langchain-azure-ai/) | [PyPI - Latest version](https://pypi.org/project/langchain-azure-ai/) | [✅](https://www.npmjs.com/package/@langchain/openai) |
| [Databricks](/oss/python/integrations/providers/databricks/) | [`databricks-langchain`](https://pypi.org/project/databricks-langchain/) | [Downloads per month](https://pypi.org/project/databricks-langchain/) | [PyPI - Latest version](https://pypi.org/project/databricks-langchain/) | [✅](https://www.npmjs.com/package/@langchain/community) |
| [Pinecone](/oss/python/integrations/providers/pinecone/) | [`langchain-pinecone`](https://reference.langchain.com/python/langchain-pinecone) | [Downloads per month](https://pypi.org/project/langchain-pinecone/) | [PyPI - Latest version](https://pypi.org/project/langchain-pinecone/) | [✅](https://www.npmjs.com/package/@langchain/pinecone) |
| [IBM](/oss/python/integrations/providers/ibm/) | [`langchain-ibm`](https://reference.langchain.com/python/langchain-ibm) | [Downloads per month](https://pypi.org/project/langchain-ibm/) | [PyPI - Latest version](https://pypi.org/project/langchain-ibm/) | [✅](https://www.npmjs.com/package/@langchain/ibm) |
| [Perplexity](/oss/python/integrations/providers/perplexity/) | [`langchain-perplexity`](https://reference.langchain.com/python/langchain-perplexity) | [Downloads per month](https://pypi.org/project/langchain-perplexity/) | [PyPI - Latest version](https://pypi.org/project/langchain-perplexity/) | [✅](https://www.npmjs.com/package/@langchain/community) |
| [Milvus](/oss/python/integrations/providers/milvus/) | [`langchain-milvus`](https://reference.langchain.com/python/langchain-milvus) | [Downloads per month](https://pypi.org/project/langchain-milvus/) | [PyPI - Latest version](https://pypi.org/project/langchain-milvus/) | [✅](https://www.npmjs.com/package/@langchain/community) |
| [DataStax Astra DB](/oss/python/integrations/providers/astradb/) | [`langchain-astradb`](https://reference.langchain.com/python/langchain-astradb) | [Downloads per month](https://pypi.org/project/langchain-astradb/) | [PyPI - Latest version](https://pypi.org/project/langchain-astradb/) | [✅](https://www.npmjs.com/package/@langchain/community) |
| [Elasticsearch](/oss/python/integrations/providers/elasticsearch/) | [`langchain-elasticsearch`](https://reference.langchain.com/python/langchain-elasticsearch) | [Downloads per month](https://pypi.org/project/langchain-elasticsearch/) | [PyPI - Latest version](https://pypi.org/project/langchain-elasticsearch/) | [✅](https://www.npmjs.com/package/@langchain/community) |
| [Redis](/oss/python/integrations/providers/redis/) | [`langchain-redis`](https://reference.langchain.com/python/langchain-redis) | [Downloads per month](https://pypi.org/project/langchain-redis/) | [PyPI - Latest version](https://pypi.org/project/langchain-redis/) | [✅](https://www.npmjs.com/package/@langchain/redis) |
| [Together](/oss/python/integrations/providers/together/) | [`langchain-together`](https://reference.langchain.com/python/langchain-together) | [Downloads per month](https://pypi.org/project/langchain-together/) | [PyPI - Latest version](https://pypi.org/project/langchain-together/) | [✅](https://www.npmjs.com/package/@langchain/community) |
| [SAP HANA Cloud](/oss/python/integrations/providers/sap) | [`langchain-hana`](https://pypi.org/project/langchain-hana/) | [Downloads per month](https://pypi.org/project/langchain-hana/) | [PyPI - Latest version](https://pypi.org/project/langchain-hana/) | [✅](https://www.npmjs.com/package/@sap/hana-langchain) |
| [MCP Toolbox (Google)](/oss/python/integrations/providers/toolbox/) | [`toolbox-langchain`](https://pypi.org/project/toolbox-langchain/) | [Downloads per month](https://pypi.org/project/toolbox-langchain/) | [PyPI - Latest version](https://pypi.org/project/toolbox-langchain/) | ❌ |
| [Google (Community)](/oss/python/integrations/providers/google) | [`langchain-google-community`](https://reference.langchain.com/python/langchain-google-community) | [Downloads per month](https://pypi.org/project/langchain-google-community/) | [PyPI - Latest version](https://pypi.org/project/langchain-google-community/) | ❌ |
| [OpenInference](/oss/python/integrations/callbacks/openinference) | [`openinference-instrumentation-langchain`](https://pypi.org/project/openinference-instrumentation-langchain/) | [Downloads per month](https://pypi.org/project/openinference-instrumentation-langchain/) | [PyPI - Latest version](https://pypi.org/project/openinference-instrumentation-langchain/) | [✅](https://www.npmjs.com/package/@arizeai/openinference-instrumentation-langchain) |
| [Weaviate](/oss/python/integrations/providers/weaviate/) | [`langchain-weaviate`](https://reference.langchain.com/python/langchain-weaviate) | [Downloads per month](https://pypi.org/project/langchain-weaviate/) | [PyPI - Latest version](https://pypi.org/project/langchain-weaviate/) | [✅](https://www.npmjs.com/package/@langchain/weaviate) |
| [Oracle AI Vector Search](/oss/python/integrations/providers/oracleai) | [`langchain-oracledb`](https://pypi.org/project/langchain-oracledb/) | [Downloads per month](https://pypi.org/project/langchain-oracledb/) | [PyPI - Latest version](https://pypi.org/project/langchain-oracledb/) | [✅](https://www.npmjs.com/package/@oracle/langchain-oracledb) |
| [Unstructured](/oss/python/integrations/providers/unstructured/) | [`langchain-unstructured`](https://reference.langchain.com/python/langchain-unstructured) | [Downloads per month](https://pypi.org/project/langchain-unstructured/) | [PyPI - Latest version](https://pypi.org/project/langchain-unstructured/) | [✅](https://www.npmjs.com/package/@langchain/community) |
| [Neo4J](/oss/python/integrations/providers/neo4j/) | [`langchain-neo4j`](https://reference.langchain.com/python/langchain-neo4j) | [Downloads per month](https://pypi.org/project/langchain-neo4j/) | [PyPI - Latest version](https://pypi.org/project/langchain-neo4j/) | [✅](https://www.npmjs.com/package/@langchain/community) |
| [Graph RAG](/oss/python/integrations/providers/graph_rag) | [`langchain-graph-retriever`](https://pypi.org/project/langchain-graph-retriever/) | [Downloads per month](https://pypi.org/project/langchain-graph-retriever/) | [PyPI - Latest version](https://pypi.org/project/langchain-graph-retriever/) | ❌ |
| [Cerebras](/oss/python/integrations/providers/cerebras/) | [`langchain-cerebras`](https://reference.langchain.com/python/langchain-cerebras) | [Downloads per month](https://pypi.org/project/langchain-cerebras/) | [PyPI - Latest version](https://pypi.org/project/langchain-cerebras/) | [✅](https://www.npmjs.com/package/@langchain/cerebras) |
| [Exa](/oss/python/integrations/providers/exa_search) | [`langchain-exa`](https://reference.langchain.com/python/langchain-exa) | [Downloads per month](https://pypi.org/project/langchain-exa/) | [PyPI - Latest version](https://pypi.org/project/langchain-exa/) | [✅](https://www.npmjs.com/package/@langchain/exa) |
| [VoyageAI](/oss/python/integrations/providers/voyageai/) | [`langchain-voyageai`](https://pypi.org/project/langchain-voyageai/) | [Downloads per month](https://pypi.org/project/langchain-voyageai/) | [PyPI - Latest version](https://pypi.org/project/langchain-voyageai/) | ❌ |

## All providers

[See all providers](/oss/python/integrations/providers/all_providers) or search for a provider using the search field.

If you’d like to contribute an integration, see the [contributing guide](/oss/python/contributing).

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).