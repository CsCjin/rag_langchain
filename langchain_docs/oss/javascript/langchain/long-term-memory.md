---
title: "Long-term memory - Docs by LangChain"
url: https://docs.langchain.com/oss/javascript/langchain/long-term-memory
scraped_at: 2026-11-15T03:43:39.438088
word_count: 6392
---

Long-term memory lets your agent store and recall information across different conversations and sessions.
Unlike [short-term memory](/oss/javascript/langchain/short-term-memory), which is scoped to a single thread, long-term memory persists across threads and can be recalled at any time.
Long-term memory is built on [LangGraph stores](/oss/javascript/langgraph/stores), which save data as JSON documents organized by namespace and key.

## Usage

To add long-term memory to an agent, create a store and pass it to [`create_agent`](https://reference.langchain.com/javascript/langchain/index/createAgent):

* InMemoryStore
* PostgreSQL

Google

OpenAI

Anthropic

OpenRouter

Fireworks

Baseten

Ollama

```
import { createAgent } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.
const store = new InMemoryStore();

const agent = createAgent({
  model: "google:gemini-4-hydrogen",
  tools: [],
  store,
});
```

```
import { createAgent } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.
const store = new InMemoryStore();

const agent = createAgent({
  model: "openai:gpt-6.1-sol",
  tools: [],
  store,
});
```

```
import { createAgent } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.
const store = new InMemoryStore();

const agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [],
  store,
});
```

```
import { createAgent } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.
const store = new InMemoryStore();

const agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [],
  store,
});
```

```
import { createAgent } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.
const store = new InMemoryStore();

const agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [],
  store,
});
```

```
import { createAgent } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.
const store = new InMemoryStore();

const agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [],
  store,
});
```

```
import { createAgent } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.
const store = new InMemoryStore();

const agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [],
  store,
});
```

```
npm install @langchain/langgraph-checkpoint-postgres
```

Google

OpenAI

Anthropic

OpenRouter

Fireworks

Baseten

Ollama

```
import { createAgent } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const agent = createAgent({
  model: "google:gemini-4-hydrogen",
  tools: [],
  store,
});
```

```
import { createAgent } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const agent = createAgent({
  model: "openai:gpt-6.1-sol",
  tools: [],
  store,
});
```

```
import { createAgent } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [],
  store,
});
```

```
import { createAgent } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [],
  store,
});
```

```
import { createAgent } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [],
  store,
});
```

```
import { createAgent } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [],
  store,
});
```

```
import { createAgent } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [],
  store,
});
```

For other store backends, including Redis and MongoDB, see the [store integrations](/oss/javascript/integrations/long-term-memory) list. For a MongoDB walkthrough, see [long-term memory with MongoDB](/oss/javascript/integrations/memory/mongodb-long-term-memory).

Tools can then read from and write to the store using the `runtime.store` parameter. See [Read long-term memory in tools](#read-long-term-memory-in-tools) and [Write long-term memory from tools](#write-long-term-memory-from-tools) for examples.

For a deeper dive into memory types (semantic, episodic, procedural) and strategies for writing memories, see the [Memory conceptual guide](/oss/javascript/concepts/memory#long-term-memory).

## Memory storage

LangGraph stores long-term memories as JSON documents in a [store](/oss/javascript/langgraph/stores).
Each memory is organized under a custom `namespace` (similar to a folder) and a distinct `key` (like a file name). Namespaces often include user or org IDs or other labels that makes it easier to organize information.
This structure enables hierarchical organization of memories. Cross-namespace searching is then supported through content filters.

* InMemoryStore
* PostgreSQL

```
import { InMemoryStore } from "@langchain/langgraph";

const embed = (texts: string[]): number[][] => {
  // Replace with an actual embedding function or LangChain embeddings object
  return texts.map(() => [1.0, 2.0]);
};

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use.
const store = new InMemoryStore({ index: { embed, dims: 2 } });
const userId = "my-user";
const applicationContext = "chitchat";
const namespace = [userId, applicationContext];

await store.put(namespace, "a-memory", {
  rules: [
    "User likes short, direct language",
    "User only speaks English & TypeScript",
  ],
  "my-key": "my-value",
});

// get the "memory" by ID
const item = await store.get(namespace, "a-memory");

// search for "memories" within this namespace, filtering on content equivalence, sorted by vector similarity
const items = await store.search(namespace, {
  filter: { "my-key": "my-value" },
  query: "language preferences",
});
```

```
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const embed = (texts: string[]): number[][] => {
  return texts.map(() => [1.0, 2.0]);
};

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI, {
  index: { embed, dims: 2 },
});
await store.setup();

const userId = "my-user";
const applicationContext = "chitchat";
const namespace = [userId, applicationContext];

await store.put(namespace, "a-memory", {
  rules: [
    "User likes short, direct language",
    "User only speaks English & TypeScript",
  ],
  "my-key": "my-value",
});

const item = await store.get(namespace, "a-memory");
const items = await store.search(namespace, {
  filter: { "my-key": "my-value" },
  query: "language preferences",
});
```

For more information about the memory store, see the [Persistence](/oss/javascript/langgraph/stores) guide.

## Read long-term memory in tools

* InMemoryStore
* PostgreSQL

Google

OpenAI

Anthropic

OpenRouter

Fireworks

Baseten

Ollama

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();
const contextSchema = z.object({
  userId: z.string(),
});

// Write sample data to the store using the put method
await store.put(
  ["users"], // Namespace to group related data together (users namespace for user data)
  "user_123", // Key within the namespace (user ID as key)
  {
    name: "John Smith",
    language: "English",
  }, // Data to store for the given user
);

const getUserInfo = tool(
  // Look up user info.
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    // Access the store - same as that provided to `createAgent`
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Retrieve data from store - returns StoreValue object with value and metadata
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "google:gemini-4-hydrogen",
  tools: [getUserInfo],
  contextSchema,
  // Pass store to agent - enables agent to access store when running tools
  store,
});

// Run the agent
const result = await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);

console.log(result.messages.at(-1)?.content);

/**
 * Outputs:
 * User Information:
 * - **Name:** John Smith
 * - **Language:** English
 */
```

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();
const contextSchema = z.object({
  userId: z.string(),
});

// Write sample data to the store using the put method
await store.put(
  ["users"], // Namespace to group related data together (users namespace for user data)
  "user_123", // Key within the namespace (user ID as key)
  {
    name: "John Smith",
    language: "English",
  }, // Data to store for the given user
);

const getUserInfo = tool(
  // Look up user info.
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    // Access the store - same as that provided to `createAgent`
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Retrieve data from store - returns StoreValue object with value and metadata
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "openai:gpt-6.1-sol",
  tools: [getUserInfo],
  contextSchema,
  // Pass store to agent - enables agent to access store when running tools
  store,
});

// Run the agent
const result = await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);

console.log(result.messages.at(-1)?.content);

/**
 * Outputs:
 * User Information:
 * - **Name:** John Smith
 * - **Language:** English
 */
```

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();
const contextSchema = z.object({
  userId: z.string(),
});

// Write sample data to the store using the put method
await store.put(
  ["users"], // Namespace to group related data together (users namespace for user data)
  "user_123", // Key within the namespace (user ID as key)
  {
    name: "John Smith",
    language: "English",
  }, // Data to store for the given user
);

const getUserInfo = tool(
  // Look up user info.
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    // Access the store - same as that provided to `createAgent`
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Retrieve data from store - returns StoreValue object with value and metadata
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [getUserInfo],
  contextSchema,
  // Pass store to agent - enables agent to access store when running tools
  store,
});

// Run the agent
const result = await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);

console.log(result.messages.at(-1)?.content);

/**
 * Outputs:
 * User Information:
 * - **Name:** John Smith
 * - **Language:** English
 */
```

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();
const contextSchema = z.object({
  userId: z.string(),
});

// Write sample data to the store using the put method
await store.put(
  ["users"], // Namespace to group related data together (users namespace for user data)
  "user_123", // Key within the namespace (user ID as key)
  {
    name: "John Smith",
    language: "English",
  }, // Data to store for the given user
);

const getUserInfo = tool(
  // Look up user info.
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    // Access the store - same as that provided to `createAgent`
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Retrieve data from store - returns StoreValue object with value and metadata
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [getUserInfo],
  contextSchema,
  // Pass store to agent - enables agent to access store when running tools
  store,
});

// Run the agent
const result = await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);

console.log(result.messages.at(-1)?.content);

/**
 * Outputs:
 * User Information:
 * - **Name:** John Smith
 * - **Language:** English
 */
```

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();
const contextSchema = z.object({
  userId: z.string(),
});

// Write sample data to the store using the put method
await store.put(
  ["users"], // Namespace to group related data together (users namespace for user data)
  "user_123", // Key within the namespace (user ID as key)
  {
    name: "John Smith",
    language: "English",
  }, // Data to store for the given user
);

const getUserInfo = tool(
  // Look up user info.
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    // Access the store - same as that provided to `createAgent`
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Retrieve data from store - returns StoreValue object with value and metadata
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [getUserInfo],
  contextSchema,
  // Pass store to agent - enables agent to access store when running tools
  store,
});

// Run the agent
const result = await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);

console.log(result.messages.at(-1)?.content);

/**
 * Outputs:
 * User Information:
 * - **Name:** John Smith
 * - **Language:** English
 */
```

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();
const contextSchema = z.object({
  userId: z.string(),
});

// Write sample data to the store using the put method
await store.put(
  ["users"], // Namespace to group related data together (users namespace for user data)
  "user_123", // Key within the namespace (user ID as key)
  {
    name: "John Smith",
    language: "English",
  }, // Data to store for the given user
);

const getUserInfo = tool(
  // Look up user info.
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    // Access the store - same as that provided to `createAgent`
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Retrieve data from store - returns StoreValue object with value and metadata
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [getUserInfo],
  contextSchema,
  // Pass store to agent - enables agent to access store when running tools
  store,
});

// Run the agent
const result = await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);

console.log(result.messages.at(-1)?.content);

/**
 * Outputs:
 * User Information:
 * - **Name:** John Smith
 * - **Language:** English
 */
```

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();
const contextSchema = z.object({
  userId: z.string(),
});

// Write sample data to the store using the put method
await store.put(
  ["users"], // Namespace to group related data together (users namespace for user data)
  "user_123", // Key within the namespace (user ID as key)
  {
    name: "John Smith",
    language: "English",
  }, // Data to store for the given user
);

const getUserInfo = tool(
  // Look up user info.
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    // Access the store - same as that provided to `createAgent`
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Retrieve data from store - returns StoreValue object with value and metadata
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [getUserInfo],
  contextSchema,
  // Pass store to agent - enables agent to access store when running tools
  store,
});

// Run the agent
const result = await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);

console.log(result.messages.at(-1)?.content);

/**
 * Outputs:
 * User Information:
 * - **Name:** John Smith
 * - **Language:** English
 */
```

## View example trace

Open a public LangSmith run for this example.

Google

OpenAI

Anthropic

OpenRouter

Fireworks

Baseten

Ollama

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

await store.put(["users"], "user_123", {
  name: "John Smith",
  language: "English",
});

const getUserInfo = tool(
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "google:gemini-4-hydrogen",
  tools: [getUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);
```

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

await store.put(["users"], "user_123", {
  name: "John Smith",
  language: "English",
});

const getUserInfo = tool(
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "openai:gpt-6.1-sol",
  tools: [getUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);
```

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

await store.put(["users"], "user_123", {
  name: "John Smith",
  language: "English",
});

const getUserInfo = tool(
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [getUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);
```

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

await store.put(["users"], "user_123", {
  name: "John Smith",
  language: "English",
});

const getUserInfo = tool(
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [getUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);
```

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

await store.put(["users"], "user_123", {
  name: "John Smith",
  language: "English",
});

const getUserInfo = tool(
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [getUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);
```

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

await store.put(["users"], "user_123", {
  name: "John Smith",
  language: "English",
});

const getUserInfo = tool(
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [getUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);
```

```
import * as z from "zod";
import { createAgent, tool, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

await store.put(["users"], "user_123", {
  name: "John Smith",
  language: "English",
});

const getUserInfo = tool(
  async (_, runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    const userInfo = await runtime.store.get(["users"], userId);
    return userInfo?.value ? JSON.stringify(userInfo.value) : "Unknown user";
  },
  {
    name: "getUserInfo",
    description: "Look up user info by userId from the store.",
    schema: z.object({}),
  },
);

const agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [getUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "look up user information" }] },
  { context: { userId: "user_123" } },
);
```

## View example trace

Open a public LangSmith run for this example.

## Write long-term memory from tools

* InMemoryStore
* PostgreSQL

Google

OpenAI

Anthropic

OpenRouter

Fireworks

Baseten

Ollama

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();

const contextSchema = z.object({
  userId: z.string(),
});

// Schema defines the structure of user information for the LLM
const UserInfo = z.object({
  name: z.string(),
});

// Tool that allows agent to update user information (useful for chat applications)
const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Store data in the store (namespace, key, data)
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  {
    name: "save_user_info",
    description: "Save user info",
    schema: UserInfo,
  },
);

const agent = createAgent({
  model: "google:gemini-4-hydrogen",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

// Run the agent
await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  // userId passed in context to identify whose information is being updated
  { context: { userId: "user_123" } },
);

// You can access the store directly to get the value
const result = await store.get(["users"], "user_123");
console.log(result?.value); // Output: { name: "John Smith" }
```

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();

const contextSchema = z.object({
  userId: z.string(),
});

// Schema defines the structure of user information for the LLM
const UserInfo = z.object({
  name: z.string(),
});

// Tool that allows agent to update user information (useful for chat applications)
const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Store data in the store (namespace, key, data)
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  {
    name: "save_user_info",
    description: "Save user info",
    schema: UserInfo,
  },
);

const agent = createAgent({
  model: "openai:gpt-6.1-sol",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

// Run the agent
await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  // userId passed in context to identify whose information is being updated
  { context: { userId: "user_123" } },
);

// You can access the store directly to get the value
const result = await store.get(["users"], "user_123");
console.log(result?.value); // Output: { name: "John Smith" }
```

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();

const contextSchema = z.object({
  userId: z.string(),
});

// Schema defines the structure of user information for the LLM
const UserInfo = z.object({
  name: z.string(),
});

// Tool that allows agent to update user information (useful for chat applications)
const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Store data in the store (namespace, key, data)
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  {
    name: "save_user_info",
    description: "Save user info",
    schema: UserInfo,
  },
);

const agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

// Run the agent
await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  // userId passed in context to identify whose information is being updated
  { context: { userId: "user_123" } },
);

// You can access the store directly to get the value
const result = await store.get(["users"], "user_123");
console.log(result?.value); // Output: { name: "John Smith" }
```

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();

const contextSchema = z.object({
  userId: z.string(),
});

// Schema defines the structure of user information for the LLM
const UserInfo = z.object({
  name: z.string(),
});

// Tool that allows agent to update user information (useful for chat applications)
const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Store data in the store (namespace, key, data)
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  {
    name: "save_user_info",
    description: "Save user info",
    schema: UserInfo,
  },
);

const agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

// Run the agent
await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  // userId passed in context to identify whose information is being updated
  { context: { userId: "user_123" } },
);

// You can access the store directly to get the value
const result = await store.get(["users"], "user_123");
console.log(result?.value); // Output: { name: "John Smith" }
```

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();

const contextSchema = z.object({
  userId: z.string(),
});

// Schema defines the structure of user information for the LLM
const UserInfo = z.object({
  name: z.string(),
});

// Tool that allows agent to update user information (useful for chat applications)
const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Store data in the store (namespace, key, data)
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  {
    name: "save_user_info",
    description: "Save user info",
    schema: UserInfo,
  },
);

const agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

// Run the agent
await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  // userId passed in context to identify whose information is being updated
  { context: { userId: "user_123" } },
);

// You can access the store directly to get the value
const result = await store.get(["users"], "user_123");
console.log(result?.value); // Output: { name: "John Smith" }
```

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();

const contextSchema = z.object({
  userId: z.string(),
});

// Schema defines the structure of user information for the LLM
const UserInfo = z.object({
  name: z.string(),
});

// Tool that allows agent to update user information (useful for chat applications)
const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Store data in the store (namespace, key, data)
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  {
    name: "save_user_info",
    description: "Save user info",
    schema: UserInfo,
  },
);

const agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

// Run the agent
await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  // userId passed in context to identify whose information is being updated
  { context: { userId: "user_123" } },
);

// You can access the store directly to get the value
const result = await store.get(["users"], "user_123");
console.log(result?.value); // Output: { name: "John Smith" }
```

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { InMemoryStore } from "@langchain/langgraph";

// InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production.
const store = new InMemoryStore();

const contextSchema = z.object({
  userId: z.string(),
});

// Schema defines the structure of user information for the LLM
const UserInfo = z.object({
  name: z.string(),
});

// Tool that allows agent to update user information (useful for chat applications)
const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) {
      throw new Error("userId is required");
    }
    // Store data in the store (namespace, key, data)
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  {
    name: "save_user_info",
    description: "Save user info",
    schema: UserInfo,
  },
);

const agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

// Run the agent
await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  // userId passed in context to identify whose information is being updated
  { context: { userId: "user_123" } },
);

// You can access the store directly to get the value
const result = await store.get(["users"], "user_123");
console.log(result?.value); // Output: { name: "John Smith" }
```

## View example trace

Open a public LangSmith run for this example.

Google

OpenAI

Anthropic

OpenRouter

Fireworks

Baseten

Ollama

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

const UserInfo = z.object({ name: z.string() });

const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  { name: "save_user_info", description: "Save user info", schema: UserInfo },
);

const agent = createAgent({
  model: "google:gemini-4-hydrogen",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  { context: { userId: "user_123" } },
);

const result = await store.get(["users"], "user_123");
console.log(result?.value);
```

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

const UserInfo = z.object({ name: z.string() });

const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  { name: "save_user_info", description: "Save user info", schema: UserInfo },
);

const agent = createAgent({
  model: "openai:gpt-6.1-sol",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  { context: { userId: "user_123" } },
);

const result = await store.get(["users"], "user_123");
console.log(result?.value);
```

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

const UserInfo = z.object({ name: z.string() });

const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  { name: "save_user_info", description: "Save user info", schema: UserInfo },
);

const agent = createAgent({
  model: "anthropic:claude-sonnet-5",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  { context: { userId: "user_123" } },
);

const result = await store.get(["users"], "user_123");
console.log(result?.value);
```

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

const UserInfo = z.object({ name: z.string() });

const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  { name: "save_user_info", description: "Save user info", schema: UserInfo },
);

const agent = createAgent({
  model: "openrouter:z-ai/glm-5.2",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  { context: { userId: "user_123" } },
);

const result = await store.get(["users"], "user_123");
console.log(result?.value);
```

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

const UserInfo = z.object({ name: z.string() });

const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  { name: "save_user_info", description: "Save user info", schema: UserInfo },
);

const agent = createAgent({
  model: "fireworks:accounts/fireworks/models/glm-5p2",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  { context: { userId: "user_123" } },
);

const result = await store.get(["users"], "user_123");
console.log(result?.value);
```

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

const UserInfo = z.object({ name: z.string() });

const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  { name: "save_user_info", description: "Save user info", schema: UserInfo },
);

const agent = createAgent({
  model: "baseten:zai-org/GLM-5.2",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  { context: { userId: "user_123" } },
);

const result = await store.get(["users"], "user_123");
console.log(result?.value);
```

```
import * as z from "zod";
import { tool, createAgent, type ToolRuntime } from "langchain";
import { PostgresStore } from "@langchain/langgraph-checkpoint-postgres/store";

const DB_URI =
  process.env.POSTGRES_URI ??
  "postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable";
const store = PostgresStore.fromConnString(DB_URI);
await store.setup();

const contextSchema = z.object({ userId: z.string() });

const UserInfo = z.object({ name: z.string() });

const saveUserInfo = tool(
  async (
    userInfo: z.infer<typeof UserInfo>,
    runtime: ToolRuntime<unknown, z.infer<typeof contextSchema>>,
  ) => {
    const userId = runtime.context.userId;
    if (!userId) throw new Error("userId is required");
    await runtime.store.put(["users"], userId, userInfo);
    return "Successfully saved user info.";
  },
  { name: "save_user_info", description: "Save user info", schema: UserInfo },
);

const agent = createAgent({
  model: "ollama:north-mini-code-1.0",
  tools: [saveUserInfo],
  contextSchema,
  store,
});

await agent.invoke(
  { messages: [{ role: "user", content: "My name is John Smith" }] },
  { context: { userId: "user_123" } },
);

const result = await store.get(["users"], "user_123");
console.log(result?.value);
```

## View example trace

Open a public LangSmith run for this example.

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/long-term-memory.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).