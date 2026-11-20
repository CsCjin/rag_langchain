---
title: "Vector store integrations - Docs by LangChain"
url: https://docs.langchain.com/oss/javascript/integrations/vectorstores
scraped_at: 2026-11-15T03:43:25.765023
word_count: 1374
---

## Overview

A [vector store](/oss/javascript/integrations/vectorstores) stores [embedded](/oss/javascript/integrations/embeddings) data and performs similarity search.

### Interface

LangChain provides a unified interface for vector stores, allowing you to:

* `addDocuments` - Add documents to the store.
* `delete` - Remove stored documents by ID.
* `similaritySearch` - Query for semantically similar documents.

This abstraction lets you switch between different implementations without altering your application logic.

### Initialization

Most vectorstores in LangChain accept an embedding model as an argument when initializing the vector store.

```
import { OpenAIEmbeddings } from "@langchain/openai";
import { MemoryVectorStore } from "@langchain/classic/vectorstores/memory";

const embeddings = new OpenAIEmbeddings({
  model: "text-embedding-3-small",
});
const vectorStore = new MemoryVectorStore(embeddings);
```

### Adding documents

You can add documents to the vector store by using the `addDocuments` function.

```
import { Document } from "@langchain/core/documents";
const document = new Document({
  pageContent: "Hello world",
});
await vectorStore.addDocuments([document]);
```

### Deleting documents

You can delete documents from the vector store by using the `delete` function.

```
await vectorStore.delete({
  filter: {
    pageContent: "Hello world",
  },
});
```

### Similarity search

Issue a semantic query using `similaritySearch`, which returns the closest embedded documents:

```
const results = await vectorStore.similaritySearch("Hello world", 10);
```

Many vector stores support parameters like:

* `k` — number of results to return
* `filter` — conditional filtering based on metadata

### Similarity metrics & indexing

Embedding similarity may be computed using:

* **Cosine similarity**
* **Euclidean distance**
* **Dot product**

Efficient search often employs indexing methods such as HNSW (Hierarchical Navigable Small World), though specifics depend on the vector store.

### Metadata filtering

Filtering by metadata (e.g., source, date) can refine search results:

```
vectorStore.similaritySearch("query", 2, { source: "tweets" });
```

Support for metadata-based filtering varies between implementations.
Check the documentation of your chosen vector store for details.

## Top integrations

**Select embedding model:**

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
npm i @langchain/aws
```

```
yarn add @langchain/aws
```

```
pnpm add @langchain/aws
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
npm i @langchain/google-genai
```

```
yarn add @langchain/google-genai
```

```
pnpm add @langchain/google-genai
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
npm i @langchain/google-vertexai
```

```
yarn add @langchain/google-vertexai
```

```
pnpm add @langchain/google-vertexai
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
npm i @langchain/cohere
```

```
yarn add @langchain/cohere
```

```
pnpm add @langchain/cohere
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

**Select vector store:**

Memory

yarn

pnpm

```
npm i langchain
```

```
yarn add langchain
```

```
pnpm add langchain
```

```
import { MemoryVectorStore } from "@langchain/classic/vectorstores/memory";

const vectorStore = new MemoryVectorStore(embeddings);
```

MongoDB

* Manual embedding
* Automated embedding

npm

yarn

pnpm

```
npm install @langchain/mongodb mongodb @langchain/core
```

```
yarn add @langchain/mongodb mongodb @langchain/core
```

```
pnpm add @langchain/mongodb mongodb @langchain/core
```

```
import { MongoDBAtlasVectorSearch } from "@langchain/mongodb"
import { MongoClient } from "mongodb";

const client = new MongoClient(process.env.MONGODB_ATLAS_URI!);
const collection = client
  .db(process.env.MONGODB_ATLAS_DB_NAME)
  .collection(process.env.MONGODB_ATLAS_COLLECTION_NAME);

const vectorStore = new MongoDBAtlasVectorSearch(embeddings, {
  collection,
  indexName: "vector_index",
  textKey: "text",
  embeddingKey: "embedding",
});
```

npm

yarn

pnpm

```
npm install @langchain/mongodb mongodb @langchain/core
```

```
yarn add @langchain/mongodb mongodb @langchain/core
```

```
pnpm add @langchain/mongodb mongodb @langchain/core
```

```
import { MongoDBAtlasVectorSearch } from "@langchain/mongodb"
import { MongoClient } from "mongodb";

const client = new MongoClient(process.env.MONGODB_ATLAS_URI!);
const collection = client
  .db(process.env.MONGODB_ATLAS_DB_NAME)
  .collection(process.env.MONGODB_ATLAS_COLLECTION_NAME);

const vectorStore = new MongoDBAtlasVectorSearch({ collection });
```

Pinecone

npm

yarn

pnpm

```
npm install @langchain/pinecone @langchain/core @pinecone-database/pinecone
```

```
yarn add @langchain/pinecone @langchain/core @pinecone-database/pinecone
```

```
pnpm add @langchain/pinecone @langchain/core @pinecone-database/pinecone
```

```
import { PineconeStore } from "@langchain/pinecone";
import { Pinecone as PineconeClient } from "@pinecone-database/pinecone";

const pinecone = new PineconeClient();
const vectorStore = new PineconeStore(embeddings, {
  pineconeIndex,
  maxConcurrency: 5,
});
```

Redis

npm

yarn

pnpm

```
npm install @langchain/redis @langchain/core redis
```

```
yarn add @langchain/redis @langchain/core redis
```

```
pnpm add @langchain/redis @langchain/core redis
```

```
import { RedisVectorStore } from "@langchain/redis";

const vectorStore = new RedisVectorStore(embeddings, {
  redisClient: client,
  indexName: "langchainjs-testing",
});
```

Qdrant

npm

yarn

pnpm

```
npm install @langchain/qdrant @langchain/core
```

```
yarn add @langchain/qdrant @langchain/core
```

```
pnpm add @langchain/qdrant @langchain/core
```

```
import { QdrantVectorStore } from "@langchain/qdrant";

const vectorStore = await QdrantVectorStore.fromExistingCollection(embeddings, {
  url: process.env.QDRANT_URL,
  collectionName: "langchainjs-testing",
});
```

Oracle AI Database

npm

yarn

pnpm

```
npm i @oracle/langchain-oracledb @langchain/core
```

```
yarn add @oracle/langchain-oracledb @langchain/core
```

```
pnpm add @oracle/langchain-oracledb @langchain/core
```

```
import oracledb from "oracledb";
import { OracleEmbeddings, OracleVS } from "@oracle/langchain-oracledb";

const connection = await oracledb.getConnection({
  user: process.env.ORACLE_USER,
  password: process.env.ORACLE_PASSWORD,
  connectionString: process.env.ORACLE_DSN,
});

const embeddings = new OracleEmbeddings(connection, {
  provider: "database",
  model: process.env.DEMO_ONNX_MODEL ?? "DEMO_MODEL",
});

const vectorStore = new OracleVS(embeddings, {
  client: connection,
  tableName: "DEMO_VECTORS",
  query: "Find support tickets mentioning service outages.",
  distanceStrategy: "DOT",
});
await vectorStore.initialize();
```

Weaviate

npm

yarn

pnpm

```
npm install @langchain/weaviate @langchain/core weaviate-client
```

```
yarn add @langchain/weaviate @langchain/core weaviate-client
```

```
pnpm add @langchain/weaviate @langchain/core weaviate-client
```

```
import { WeaviateStore } from "@langchain/weaviate";

const vectorStore = new WeaviateStore(embeddings, {
    client: weaviateClient,
    indexName: "Langchainjs_test",
});
```

LangChain.js integrates with a variety of vector stores. You can check out a full list below:

## All vector stores

| Vectorstore | Downloads |
| --- | --- |
| [`WeaviateStore`](/oss/javascript/integrations/vectorstores/weaviate) | [Downloads per month](https://www.npmjs.com/package/@langchain/weaviate) |
| [`PineconeStore`](/oss/javascript/integrations/vectorstores/pinecone) | [Downloads per month](https://www.npmjs.com/package/@langchain/pinecone) |
| [`MongoDBAtlasVectorSearch`](/oss/javascript/integrations/vectorstores/mongodb_atlas) | [Downloads per month](https://www.npmjs.com/package/@langchain/mongodb) |
| [`QdrantVectorStore`](/oss/javascript/integrations/vectorstores/qdrant) | [Downloads per month](https://www.npmjs.com/package/@langchain/qdrant) |
| [`RedisVectorStore`](/oss/javascript/integrations/vectorstores/redis) | [Downloads per month](https://www.npmjs.com/package/@langchain/redis) |
| [`OracleVS`](/oss/javascript/integrations/vectorstores/oracleai) | [Downloads per month](https://www.npmjs.com/package/@oracle/langchain-oracledb) |
| [`PGVectorStore`](/oss/javascript/integrations/vectorstores/pgvector) | [Downloads per month](https://www.npmjs.com/package/@langchain/pgvector) |
| [`Cloudflare vectorize`](/oss/javascript/integrations/vectorstores/cloudflare_vectorize) | [Downloads per month](https://www.npmjs.com/package/@langchain/cloudflare) |
| [`TurbopufferVectorStore`](/oss/javascript/integrations/vectorstores/turbopuffer) | [Downloads per month](https://www.npmjs.com/package/@langchain/turbopuffer) |
| [`Google cloud SQL for postgresql`](/oss/javascript/integrations/vectorstores/google_cloudsql_pg) | [Downloads per month](https://www.npmjs.com/package/@langchain/google-cloud-sql-pg) |
| [`Azure Cosmos DB for MongoDB vCore (deprecated)`](/oss/javascript/integrations/vectorstores/azure_cosmosdb_mongodb) | [Downloads per month](https://www.npmjs.com/package/@langchain/azure-cosmosdb) |
| [`Azure Cosmos DB for NoSQL`](/oss/javascript/integrations/vectorstores/azure_cosmosdb_nosql) | [Downloads per month](https://www.npmjs.com/package/@langchain/azure-cosmosdb) |
| [`Azure DocumentDB`](/oss/javascript/integrations/vectorstores/azure_documentdb) | [Downloads per month](https://www.npmjs.com/package/@langchain/azure-cosmosdb) |
| [`Neo4jVectorStore`](/oss/javascript/integrations/vectorstores/neo4jvector) | [Downloads per month](https://www.npmjs.com/package/@langchain/neo4j) |
| [`SAP HANA Cloud Vector Engine`](/oss/javascript/integrations/vectorstores/sap_hanavector) | [Downloads per month](https://www.npmjs.com/package/@sap/hana-langchain) |
| [`RushDBVectorStore`](https://docs.rushdb.com/connect/langchain) | [Downloads per month](https://www.npmjs.com/package/@rushdb/langchain) |
| [`LambdaDB`](https://docs.lambdadb.ai/guides/get-started/quickstart) | [Downloads per month](https://www.npmjs.com/package/@functional-systems/langchain-lambdadb) |
| [`Infino`](https://infino.ai/docs) | [Downloads per month](https://www.npmjs.com/package/@infino-ai/langchain-infino) |
| [`YDB`](/oss/javascript/integrations/vectorstores/ydb) | [Downloads per month](https://www.npmjs.com/package/@ydbjs/langchain) |
| [`langchain`](/oss/javascript/integrations/vectorstores/memory) | N/A |

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/vectorstores/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).