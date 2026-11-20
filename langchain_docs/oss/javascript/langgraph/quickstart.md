---
title: "Quickstart - Docs by LangChain"
url: https://docs.langchain.com/oss/javascript/langgraph/quickstart
scraped_at: 2026-11-15T03:44:07.899180
word_count: 1509
---

This quickstart demonstrates how to build a calculator agent with the LangGraph Graph API.
Already have an agent and want to deploy it? See [LangSmith Agent Server](/langsmith/deployment).

**Using an AI coding assistant?**

* Install the [LangChain Docs MCP servers](/use-these-docs) to give your agent access to up-to-date LangChain documentation and examples.

  Connect LangChain docs MCP servers

  CopiedCopy prompt
* Install [LangChain Skills](https://github.com/langchain-ai/langchain-skills) to improve your agent’s performance on LangChain ecosystem tasks.

  Install LangChain Skills

  CopiedCopy prompt

## Prerequisites

Before you begin, make sure you have an API key from a model provider (e.g., Gemini, Anthropic, OpenAI).
See [chat model integrations](/oss/javascript/integrations/chat) for all available providers.
If you use [LangSmith Gateway](/langsmith/llm-gateway), you can [bring your own provider keys](/langsmith/llm-gateway-quickstart) or use [Gateway Credits](/langsmith/llm-gateway-credits) to access models without a provider key.

## Setup

Install `@langchain/langgraph`, `@langchain/core`, `@langchain/anthropic`, `langchain`, and `zod`:

```
npm install @langchain/langgraph @langchain/core @langchain/anthropic langchain zod
```

This example uses Anthropic. Set your API key in the shell or a `.env` file:

Shell

.env

```
export ANTHROPIC_API_KEY="your-api-key"
```

```
ANTHROPIC_API_KEY=your-api-key
```

To use another provider, see [chat model integrations](/oss/javascript/integrations/chat) and adapt the model initialization in the next steps.

## Build the agent

The model can call tools, then the agent calls the model again until it returns a final answer.
Create one file. Add the code from each step below the previous step.
For conceptual information, see the [Graph API overview](/oss/javascript/langgraph/graph-api).

Build the LangGraph Graph API calculator quickstart

CopiedCopy prompt

## 1. Define tools and model

This example uses the Claude Sonnet model and defines tools for addition, multiplication, and division.
Create a file for the agent (`agent.py` or `agent.ts`). Add the following:

```
import { ChatAnthropic } from "@langchain/anthropic";
import { tool } from "@langchain/core/tools";
import * as z from "zod";

const model = new ChatAnthropic({
  model: "claude-sonnet-4-6",
  temperature: 0,
});

// Define tools
const add = tool(({ a, b }) => a + b, {
  name: "add",
  description: "Add two numbers",
  schema: z.object({
    a: z.number().describe("First number"),
    b: z.number().describe("Second number"),
  }),
});

const multiply = tool(({ a, b }) => a * b, {
  name: "multiply",
  description: "Multiply two numbers",
  schema: z.object({
    a: z.number().describe("First number"),
    b: z.number().describe("Second number"),
  }),
});

const divide = tool(({ a, b }) => a / b, {
  name: "divide",
  description: "Divide two numbers",
  schema: z.object({
    a: z.number().describe("First number"),
    b: z.number().describe("Second number"),
  }),
});

// Augment the LLM with tools
const toolsByName = {
  [add.name]: add,
  [multiply.name]: multiply,
  [divide.name]: divide,
};
const tools = Object.values(toolsByName);
const modelWithTools = model.bindTools(tools);
```

## 2. Define state

The graph’s state stores the messages and the number of LLM calls.
Add the following below the tools and model:

State in LangGraph persists throughout the agent’s execution.`MessagesValue` appends messages with a built-in reducer. The `llmCalls` field uses a `ReducedValue` with `(x, y) => x + y` to accumulate the count.

```
import {
  StateGraph,
  StateSchema,
  MessagesValue,
  ReducedValue,
  GraphNode,
  ConditionalEdgeRouter,
  START,
  END,
} from "@langchain/langgraph";
import { z } from "zod/v4";

const MessagesState = new StateSchema({
  messages: MessagesValue,
  llmCalls: new ReducedValue(
    z.number().default(0),
    { reducer: (x, y) => x + y }
  ),
});
```

## 3. Define model node

The model node calls the LLM and decides whether to call a tool.
Add the following below the state schema:

```
import { SystemMessage } from "@langchain/core/messages";

const llmCall: GraphNode<typeof MessagesState> = async (state) => {
  const response = await modelWithTools.invoke([
    new SystemMessage(
      "You are a helpful assistant tasked with performing arithmetic on a set of inputs."
    ),
    ...state.messages,
  ]);
  return {
    messages: [response],
    llmCalls: 1,
  };
};
```

## 4. Define tool node

The tool node calls the tools and returns the results.
Add the following below the model node:

```
import { AIMessage, ToolMessage } from "@langchain/core/messages";

const toolNode: GraphNode<typeof MessagesState> = async (state) => {
  const lastMessage = state.messages.at(-1);

  if (lastMessage == null || !AIMessage.isInstance(lastMessage)) {
    return { messages: [] };
  }

  const result: ToolMessage[] = [];
  for (const toolCall of lastMessage.tool_calls ?? []) {
    const tool = toolsByName[toolCall.name];
    const observation = await tool.invoke(toolCall);
    result.push(observation);
  }

  return { messages: result };
};
```

## 5. Define end logic

The conditional edge function routes to the tool node or to the end, depending on whether the LLM made a tool call.
Add the following below the tool node:

```
const shouldContinue: ConditionalEdgeRouter<{ InputSchema: typeof MessagesState; Nodes: "toolNode" }> = (state) => {
  const lastMessage = state.messages.at(-1);

  // Check if it's an AIMessage before accessing tool_calls
  if (!lastMessage || !AIMessage.isInstance(lastMessage)) {
    return END;
  }

  // If the LLM makes a tool call, then perform an action
  if (lastMessage.tool_calls?.length) {
    return "toolNode";
  }

  // Otherwise, we stop (reply to the user)
  return END;
};
```

## 6. Build and compile the agent

Add the following below the routing function. Build the graph with [`StateGraph`](https://reference.langchain.com/javascript/langchain-langgraph/index/StateGraph) and compile it with [`compile`](https://reference.langchain.com/javascript/langchain-langgraph/index/StateGraph/compile):

```
const agent = new StateGraph(MessagesState)
  .addNode("llmCall", llmCall)
  .addNode("toolNode", toolNode)
  .addEdge(START, "llmCall")
  .addConditionalEdges("llmCall", shouldContinue, ["toolNode", END])
  .addEdge("toolNode", "llmCall")
  .compile();
```

## 7. Set up LangSmith tracing

[LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=oss-langgraph-quickstart) shows tool calls and model responses as the agent runs.
This step is optional. Sign up at [smith.langchain.com](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=oss-langgraph-quickstart), create an API key, and set these environment variables in the shell before you run the agent:

```
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY="your-langsmith-api-key"
```

## 8. Run the agent

Add the following below the compiled graph:

```
import { HumanMessage } from "@langchain/core/messages";

const result = await agent.invoke({
  messages: [new HumanMessage("Add 3 and 4.")],
});

for (const message of result.messages) {
  console.log(`[${message.type}]: ${message.text}`);
}
```

Run the file:

```
npx tsx agent.ts
```

You should see the human message, a tool call to `add`, the tool result `7`, and a final assistant reply. The exact text varies by model, but the tool result is `7`.
To check your file, compare it with the full example:

Full code example

```
import { ChatAnthropic } from "@langchain/anthropic";
import { tool } from "@langchain/core/tools";
import {
  StateGraph,
  StateSchema,
  MessagesValue,
  ReducedValue,
  GraphNode,
  ConditionalEdgeRouter,
  START,
  END,
} from "@langchain/langgraph";
import { SystemMessage, AIMessage, ToolMessage, HumanMessage } from "@langchain/core/messages";
import * as z from "zod";

// Step 2: Define tools and model

let model = new ChatAnthropic({
  model: "claude-sonnet-4-6",
  temperature: 0,
});

// Define tools
const add = tool(({ a, b }) => a + b, {
  name: "add",
  description: "Add two numbers",
  schema: z.object({
    a: z.number().describe("First number"),
    b: z.number().describe("Second number"),
  }),
});

const multiply = tool(({ a, b }) => a * b, {
  name: "multiply",
  description: "Multiply two numbers",
  schema: z.object({
    a: z.number().describe("First number"),
    b: z.number().describe("Second number"),
  }),
});

const divide = tool(({ a, b }) => a / b, {
  name: "divide",
  description: "Divide two numbers",
  schema: z.object({
    a: z.number().describe("First number"),
    b: z.number().describe("Second number"),
  }),
});

// Augment the LLM with tools
const toolsByName = {
  [add.name]: add,
  [multiply.name]: multiply,
  [divide.name]: divide,
};
const tools = Object.values(toolsByName);
const modelWithTools = model.bindTools(tools);

// Step 3: Define state

const MessagesState = new StateSchema({
  messages: MessagesValue,
  llmCalls: new ReducedValue(
    z.number().default(0),
    { reducer: (x, y) => x + y }
  ),
});

// Step 4: Define model node

const llmCall: GraphNode<typeof MessagesState> = async (state) => {
  return {
    messages: [await modelWithTools.invoke([
      new SystemMessage(
        "You are a helpful assistant tasked with performing arithmetic on a set of inputs."
      ),
      ...state.messages,
    ])],
    llmCalls: 1,
  };
};

// Step 5: Define tool node

const toolNode: GraphNode<typeof MessagesState> = async (state) => {
  const lastMessage = state.messages.at(-1);

  if (lastMessage == null || !AIMessage.isInstance(lastMessage)) {
    return { messages: [] };
  }

  const result: ToolMessage[] = [];
  for (const toolCall of lastMessage.tool_calls ?? []) {
    const tool = toolsByName[toolCall.name];
    const observation = await tool.invoke(toolCall);
    result.push(observation);
  }

  return { messages: result };
};

// Step 6: Define end logic

const shouldContinue: ConditionalEdgeRouter<{ InputSchema: typeof MessagesState; Nodes: "toolNode" }> = (state) => {
  const lastMessage = state.messages.at(-1);

  // Check if it's an AIMessage before accessing tool_calls
  if (!lastMessage || !AIMessage.isInstance(lastMessage)) {
    return END;
  }

  // If the LLM makes a tool call, then perform an action
  if (lastMessage.tool_calls?.length) {
    return "toolNode";
  }

  // Otherwise, we stop (reply to the user)
  return END;
};

// Step 7: Build and compile the agent

const agent = new StateGraph(MessagesState)
  .addNode("llmCall", llmCall)
  .addNode("toolNode", toolNode)
  .addEdge(START, "llmCall")
  .addConditionalEdges("llmCall", shouldContinue, ["toolNode", END])
  .addEdge("toolNode", "llmCall")
  .compile();

// Step 8: Set up LangSmith tracing (optional)
// export LANGSMITH_TRACING=true
// export LANGSMITH_API_KEY="your-langsmith-api-key"

// Step 9: Run the agent
const result = await agent.invoke({
  messages: [new HumanMessage("Add 3 and 4.")],
});

for (const message of result.messages) {
  console.log(`[${message.type}]: ${message.text}`);
}
```

## Next steps

You now have a working calculator agent. Continue with one of the following subjects:

* **Build with the Graph API**: [Build checklist for the Graph API](/oss/javascript/langgraph/use-graph-api) and [Thinking in the Graph API](/oss/javascript/langgraph/thinking-in-graph-api).
* **Add persistence**: Use a [checkpointer](/oss/javascript/langgraph/persistence) so runs can pause and resume across sessions.
* **Add human-in-the-loop**: Pause with [interrupts](/oss/javascript/langgraph/interrupts) for approval or edits.
* **Stream results**: Follow [streaming](/oss/javascript/langgraph/streaming) for tokens and state updates.
* **Go deeper**: [Workflows and agents](/oss/javascript/langgraph/workflows-agents).
* **Deploy**: Host the agent with [LangSmith Agent Server](/langsmith/deployment).
* **Evaluate**: Test behavior with [LangSmith evaluation](/langsmith/evaluation-quickstart).

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).