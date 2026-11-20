---
title: "Embedding model integrations - Docs by LangChain"
url: https://docs.langchain.com/oss/javascript/integrations/embeddings
scraped_at: 2026-11-15T03:43:20.301298
word_count: 1098
---

## Overview

This overview covers **text-based embedding models**. LangChain does not currently support multimodal embeddings.

Embedding models transform raw text—such as a sentence, paragraph, or tweet—into a fixed-length vector of numbers that captures its **semantic meaning**. These vectors allow machines to compare and search text based on meaning rather than exact words.
In practice, this means that texts with similar ideas are placed close together in the vector space. For example, instead of matching only the phrase *“machine learning”*, embeddings can surface documents that discuss related concepts even when different wording is used.

### How it works

1. **Vectorization**: The model encodes each input string as a high-dimensional vector.
2. **Similarity scoring**: Vectors are compared using mathematical metrics to measure how closely related the underlying texts are.

### Similarity metrics

Several metrics are commonly used to compare embeddings:

* **Cosine similarity**: measures the angle between two vectors.
* **Euclidean distance**: measures the straight-line distance between points.
* **Dot product**: measures how much one vector projects onto another.

## Interface

LangChain provides a standard interface for text embedding models (e.g., OpenAI, Cohere, Hugging Face) via the [Embeddings](https://reference.langchain.com/javascript/langchain-core/embeddings/Embeddings) interface.
Two main methods are available:

* `embedDocuments(documents: string[]) → number[][]`: Embeds a list of documents.
* `embedQuery(text: string) → number[]`: Embeds a single query.

The interface allows queries and documents to be embedded with different strategies, though most providers handle them the same way in practice.

## Install and use

OpenAI

Install dependencies:

npm

yarn

pnpm

```
npm install @langchain/openai @langchain/core
```

```
yarn add @langchain/openai @langchain/core
```

```
pnpm add @langchain/openai @langchain/core
```

Add environment variables:

```
OPENAI_API_KEY=your-api-key
```

Instantiate the model:

```
import { OpenAIEmbeddings } from "@langchain/openai";

const embeddings = new OpenAIEmbeddings({
  model: "text-embedding-3-large"
});
```

Azure

Install dependencies

npm

yarn

pnpm

```
npm install @langchain/openai @langchain/core
```

```
yarn add @langchain/openai @langchain/core
```

```
pnpm add @langchain/openai @langchain/core
```

Add environment variables:

```
AZURE_OPENAI_API_INSTANCE_NAME=<YOUR_INSTANCE_NAME>
AZURE_OPENAI_API_KEY=<YOUR_KEY>
AZURE_OPENAI_API_VERSION="2024-02-01"
```

Instantiate the model:

```
import { AzureOpenAIEmbeddings } from "@langchain/openai";

const embeddings = new AzureOpenAIEmbeddings({
  azureOpenAIApiEmbeddingsDeploymentName: "text-embedding-ada-002"
});
```

AWS

Install dependencies:

npm

yarn

pnpm

```
npm install @langchain/aws @langchain/core
```

```
yarn add @langchain/aws @langchain/core
```

```
pnpm add @langchain/aws @langchain/core
```

Add environment variables:

```
BEDROCK_AWS_REGION=your-region
```

Instantiate the model:

```
import { BedrockEmbeddings } from "@langchain/aws";

const embeddings = new BedrockEmbeddings({
  model: "amazon.titan-embed-text-v1"
});
```

Google Gemini

Install dependencies:

npm

yarn

pnpm

```
npm install @langchain/google-genai @langchain/core
```

```
yarn add @langchain/google-genai @langchain/core
```

```
pnpm add @langchain/google-genai @langchain/core
```

Add environment variables:

```
GOOGLE_API_KEY=your-api-key
```

Instantiate the model:

```
import { GoogleGenerativeAIEmbeddings } from "@langchain/google-genai";

const embeddings = new GoogleGenerativeAIEmbeddings({
  model: "gemini-embedding-001"
});
```

Gemini Enterprise Agent Platform

Install dependencies:

npm

yarn

pnpm

```
npm install @langchain/google-vertexai @langchain/core
```

```
yarn add @langchain/google-vertexai @langchain/core
```

```
pnpm add @langchain/google-vertexai @langchain/core
```

Add environment variables:

```
GOOGLE_APPLICATION_CREDENTIALS=credentials.json
```

Instantiate the model:

```
import { VertexAIEmbeddings } from "@langchain/google-vertexai";

const embeddings = new VertexAIEmbeddings({
  model: "gemini-embedding-001"
});
```

MistralAI

Install dependencies:

npm

yarn

pnpm

```
npm install @langchain/mistralai @langchain/core
```

```
yarn add @langchain/mistralai @langchain/core
```

```
pnpm add @langchain/mistralai @langchain/core
```

Add environment variables:

```
MISTRAL_API_KEY=your-api-key
```

Instantiate the model:

```
import { MistralAIEmbeddings } from "@langchain/mistralai";

const embeddings = new MistralAIEmbeddings({
  model: "mistral-embed"
});
```

Cohere

Install dependencies:

npm

yarn

pnpm

```
npm install @langchain/cohere @langchain/core
```

```
yarn add @langchain/cohere @langchain/core
```

```
pnpm add @langchain/cohere @langchain/core
```

Add environment variables:

```
COHERE_API_KEY=your-api-key
```

Instantiate the model:

```
import { CohereEmbeddings } from "@langchain/cohere";

const embeddings = new CohereEmbeddings({
  model: "embed-english-v3.0"
});
```

Ollama

Install dependencies:

npm

yarn

pnpm

```
npm install @langchain/ollama @langchain/core
```

```
yarn add @langchain/ollama @langchain/core
```

```
pnpm add @langchain/ollama @langchain/core
```

Instantiate the model:

```
import { OllamaEmbeddings } from "@langchain/ollama";

const embeddings = new OllamaEmbeddings({
  model: "llama2",
  baseUrl: "http://localhost:11434", // Default value
});
```

Voyage AI

Install dependencies:

npm

yarn

pnpm

```
npm install @langchain/mongodb @langchain/core
```

```
yarn add @langchain/mongodb @langchain/core
```

```
pnpm add @langchain/mongodb @langchain/core
```

Add environment variables:

```
VOYAGE_API_KEY=your-api-key
```

Instantiate the model:

```
import { VoyageEmbeddings } from "@langchain/mongodb";

const embeddings = new VoyageEmbeddings({
  model: "voyage-4"
});
```

## Caching

Embeddings can be stored or temporarily cached to avoid needing to recompute them.
Caching embeddings can be done using a `CacheBackedEmbeddings`. This wrapper stores embeddings in a key-value store, where the text is hashed and the hash is used as the key in the cache.
The main supported way to initialize a `CacheBackedEmbeddings` is `fromBytesStore`. It takes the following parameters:

* **underlyingEmbeddings**: The embedder to use for embedding.
* **documentEmbeddingStore**: Any [`BaseStore`](/oss/javascript/integrations/stores/) for caching document embeddings.
* **options.namespace**: (optional, defaults to `""`) The namespace to use for the document cache. Helps avoid collisions (e.g., set it to the embedding model name).

* Always set the `namespace` parameter to avoid collisions when using different embedding models.
* `CacheBackedEmbeddings` does not cache query embeddings by default. To enable this, specify a `query_embedding_store`.

```
import { CacheBackedEmbeddings } from "@langchain/classic/embeddings/cache_backed";
import { InMemoryStore } from "@langchain/core/stores";

const underlyingEmbeddings = new OpenAIEmbeddings();

const inMemoryStore = new InMemoryStore();

const cacheBackedEmbeddings = CacheBackedEmbeddings.fromBytesStore(
  underlyingEmbeddings,
  inMemoryStore,
  {
    namespace: underlyingEmbeddings.model,
  }
);

// Example: caching a query embedding
const tic = Date.now();
const queryEmbedding = cacheBackedEmbeddings.embedQuery("Hello, world!");
console.log(`First call took: ${Date.now() - tic}ms`);

// Example: caching a document embedding
const tic = Date.now();
const documentEmbedding = cacheBackedEmbeddings.embedDocuments(["Hello, world!"]);
console.log(`Cached creation time: ${Date.now() - tic}ms`);
```

In production, you would typically use a more robust persistent store, such as a database or cloud storage. Please see [stores integrations](/oss/javascript/integrations/stores/) for options.

## All integrations

| Integration | Downloads |
| --- | --- |
| [`AzureOpenAIEmbeddings`](/oss/javascript/integrations/embeddings/azure_openai) | [Downloads per month](https://www.npmjs.com/package/@langchain/openai) |
| [`OpenAIEmbeddings`](/oss/javascript/integrations/embeddings/openai) | [Downloads per month](https://www.npmjs.com/package/@langchain/openai) |
| [`GoogleGenerativeAIEmbeddings`](/oss/javascript/integrations/embeddings/google_generative_ai) | [Downloads per month](https://www.npmjs.com/package/@langchain/google-genai) |
| [`Bedrock`](/oss/javascript/integrations/embeddings/bedrock) | [Downloads per month](https://www.npmjs.com/package/@langchain/aws) |
| [`VertexAIEmbeddings`](/oss/javascript/integrations/embeddings/google_vertex_ai) | [Downloads per month](https://www.npmjs.com/package/@langchain/google-vertexai) |
| [`OllamaEmbeddings`](/oss/javascript/integrations/embeddings/ollama) | [Downloads per month](https://www.npmjs.com/package/@langchain/ollama) |
| [`MistralAIEmbeddings`](/oss/javascript/integrations/embeddings/mistralai) | [Downloads per month](https://www.npmjs.com/package/@langchain/mistralai) |
| [`PineconeEmbeddings`](/oss/javascript/integrations/embeddings/pinecone) | [Downloads per month](https://www.npmjs.com/package/@langchain/pinecone) |
| [`VoyageEmbeddings`](/oss/javascript/integrations/embeddings/voyageai) | [Downloads per month](https://www.npmjs.com/package/@langchain/mongodb) |
| [`CohereEmbeddings`](/oss/javascript/integrations/embeddings/cohere) | [Downloads per month](https://www.npmjs.com/package/@langchain/cohere) |
| [`FireworksEmbeddings`](/oss/javascript/integrations/embeddings/fireworks) | [Downloads per month](https://www.npmjs.com/package/@langchain/fireworks) |
| [`Nomic`](/oss/javascript/integrations/embeddings/nomic) | [Downloads per month](https://www.npmjs.com/package/@langchain/nomic) |
| [`Baidu qianfan`](/oss/javascript/integrations/embeddings/baidu_qianfan) | [Downloads per month](https://www.npmjs.com/package/@langchain/baidu-qianfan) |
| [`CloudflareWorkersAIEmbeddings`](/oss/javascript/integrations/embeddings/cloudflare_ai) | [Downloads per month](https://www.npmjs.com/package/@langchain/cloudflare) |
| [`TogetherAIEmbeddings`](/oss/javascript/integrations/embeddings/togetherai) | [Downloads per month](https://www.npmjs.com/package/@langchain/together-ai) |
| [`WatsonxEmbeddings`](/oss/javascript/integrations/embeddings/ibm) | [Downloads per month](https://www.npmjs.com/package/@langchain/ibm) |
| [`EmpirioLabsEmbeddings`](https://docs.empiriolabs.ai/integrations#langchain) | [Downloads per month](https://www.npmjs.com/package/@empiriolabs/langchain) |
| [`Mixedbread AI`](/oss/javascript/integrations/embeddings/mixedbread_ai) | [Downloads per month](https://www.npmjs.com/package/@langchain/mixedbread-ai) |
| [`SCXEmbeddings`](https://scx.ai/) | [Downloads per month](https://www.npmjs.com/package/@scx-ai/langchain) |
| [`Minimax`](/oss/javascript/integrations/embeddings/minimax) | N/A |
| [`OracleEmbeddings`](/oss/javascript/integrations/embeddings/oracleai) | N/A |

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/embeddings/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).