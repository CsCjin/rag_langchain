---
title: "Quickstart - Docs by LangChain"
url: https://docs.langchain.com/oss/python/langgraph/quickstart
scraped_at: 2026-11-15T03:45:34.415756
word_count: 1404
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
See [chat model integrations](/oss/python/integrations/chat) for all available providers.
If you use [LangSmith Gateway](/langsmith/llm-gateway), you can [bring your own provider keys](/langsmith/llm-gateway-quickstart) or use [Gateway Credits](/langsmith/llm-gateway-credits) to access models without a provider key.

## Setup

Install `langgraph`, `langchain`, and `langchain-anthropic`:

pip

uv

```
pip install -U langgraph langchain langchain-anthropic
```

```
uv add langgraph langchain langchain-anthropic
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

To use another provider, see [chat model integrations](/oss/python/integrations/chat) and adapt the model initialization in the next steps.

## Build the agent

The model can call tools, then the agent calls the model again until it returns a final answer.
Create one file. Add the code from each step below the previous step.
For conceptual information, see the [Graph API overview](/oss/python/langgraph/graph-api).

Build the LangGraph Graph API calculator quickstart

CopiedCopy prompt

## 1. Define tools and model

This example uses the Claude Sonnet model and defines tools for addition, multiplication, and division.
Create a file for the agent (`agent.py` or `agent.ts`). Add the following:

```
from langchain.tools import tool
from langchain.chat_models import init_chat_model

model = init_chat_model(
    "claude-sonnet-4-6",
    temperature=0
)

# Define tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiply `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Adds `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a + b

@tool
def divide(a: int, b: int) -> float:
    """Divide `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a / b

# Augment the LLM with tools
tools = [add, multiply, divide]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)
```

## 2. Define state

The graph’s state stores the messages and the number of LLM calls.
Add the following below the tools and model:

State in LangGraph persists throughout the agent’s execution.The `Annotated` type with `operator.add` appends new messages to the list instead of replacing it.

```
from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator

class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int
```

## 3. Define model node

The model node calls the LLM and decides whether to call a tool.
Add the following below the state schema:

```
from langchain.messages import SystemMessage

def llm_call(state: dict):
    """LLM decides whether to call a tool or not"""

    return {
        "messages": [
            model_with_tools.invoke(
                [
                    SystemMessage(
                        content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
                    )
                ]
                + state["messages"]
            )
        ],
        "llm_calls": state.get('llm_calls', 0) + 1
    }
```

## 4. Define tool node

The tool node calls the tools and returns the results.
Add the following below the model node:

```
from langchain.messages import ToolMessage

def tool_node(state: dict):
    """Performs the tool call"""

    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
    return {"messages": result}
```

## 5. Define end logic

The conditional edge function routes to the tool node or to the end, depending on whether the LLM made a tool call.
Add the following below the tool node:

```
from typing import Literal
from langgraph.graph import StateGraph, START, END

def should_continue(state: MessagesState) -> Literal["tool_node", END]:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

    messages = state["messages"]
    last_message = messages[-1]

    # If the LLM makes a tool call, then perform an action
    if last_message.tool_calls:
        return "tool_node"

    # Otherwise, we stop (reply to the user)
    return END
```

## 6. Build and compile the agent

Add the following below the routing function. Build the graph with [`StateGraph`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph) and compile it with [`compile`](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/compile):

```
# Build workflow
agent_builder = StateGraph(MessagesState)

# Add nodes
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)

# Add edges to connect nodes
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges(
    "llm_call",
    should_continue,
    ["tool_node", END]
)
agent_builder.add_edge("tool_node", "llm_call")

# Compile the agent
agent = agent_builder.compile()
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
from langchain.messages import HumanMessage

messages = [HumanMessage(content="Add 3 and 4.")]
messages = agent.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()
```

Run the file:

```
python agent.py
```

You should see the human message, a tool call to `add`, the tool result `7`, and a final assistant reply. The exact text varies by model, but the tool result is `7`.
To check your file, compare it with the full example:

Full code example

```
# Step 2: Define tools and model

from langchain.tools import tool
from langchain.chat_models import init_chat_model

model = init_chat_model(
    "claude-sonnet-4-6",
    temperature=0
)

# Define tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiply `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Adds `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a + b

@tool
def divide(a: int, b: int) -> float:
    """Divide `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a / b

# Augment the LLM with tools
tools = [add, multiply, divide]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)

# Step 3: Define state

from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator

class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    llm_calls: int

# Step 4: Define model node
from langchain.messages import SystemMessage

def llm_call(state: MessagesState):
    """LLM decides whether to call a tool or not"""

    return {
        "messages": [
            model_with_tools.invoke(
                [
                    SystemMessage(
                        content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."
                    )
                ]
                + state["messages"]
            )
        ],
        "llm_calls": state.get('llm_calls', 0) + 1
    }

# Step 5: Define tool node

from langchain.messages import ToolMessage

def tool_node(state: MessagesState):
    """Performs the tool call"""

    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
    return {"messages": result}

# Step 6: Define end logic

from typing import Literal
from langgraph.graph import StateGraph, START, END

# Conditional edge function to route to the tool node or end based upon whether the LLM made a tool call
def should_continue(state: MessagesState) -> Literal["tool_node", END]:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

    messages = state["messages"]
    last_message = messages[-1]

    # If the LLM makes a tool call, then perform an action
    if last_message.tool_calls:
        return "tool_node"

    # Otherwise, we stop (reply to the user)
    return END

# Step 7: Build and compile the agent

# Build workflow
agent_builder = StateGraph(MessagesState)

# Add nodes
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)

# Add edges to connect nodes
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges(
    "llm_call",
    should_continue,
    ["tool_node", END]
)
agent_builder.add_edge("tool_node", "llm_call")

# Compile the agent
agent = agent_builder.compile()

# Step 8: Set up LangSmith tracing (optional)
# export LANGSMITH_TRACING=true
# export LANGSMITH_API_KEY="your-langsmith-api-key"

# Step 9: Run the agent
from langchain.messages import HumanMessage
messages = [HumanMessage(content="Add 3 and 4.")]
messages = agent.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()
```

## Next steps

You now have a working calculator agent. Continue with one of the following subjects:

* **Build with the Graph API**: [Build checklist for the Graph API](/oss/python/langgraph/use-graph-api) and [Thinking in the Graph API](/oss/python/langgraph/thinking-in-graph-api).
* **Add persistence**: Use a [checkpointer](/oss/python/langgraph/persistence) so runs can pause and resume across sessions.
* **Add human-in-the-loop**: Pause with [interrupts](/oss/python/langgraph/interrupts) for approval or edits.
* **Stream results**: Follow [streaming](/oss/python/langgraph/streaming) for tokens and state updates.
* **Go deeper**: [Workflows and agents](/oss/python/langgraph/workflows-agents).
* **Deploy**: Host the agent with [LangSmith Agent Server](/langsmith/deployment).
* **Evaluate**: Test behavior with [LangSmith evaluation](/langsmith/evaluation-quickstart).

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).