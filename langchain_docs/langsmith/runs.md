---
title: "Runs - Docs by LangChain"
url: https://docs.langchain.com/langsmith/runs
scraped_at: 2026-11-15T03:39:49.175916
word_count: 285
---

A *run* is an invocation of an [assistant](/langsmith/assistants). When you execute a run, you specify which assistant to use—either by graph ID for the default assistant, or by assistant ID for a specific configuration.

This diagram shows how a **run** combines an assistant with a thread to execute the graph:

* **Graph** (light blue): The deployed code containing your agent’s logic
* **Assistants** (blue): Configuration options (model, prompts, tools)
* **Threads** (orange): State containers for conversation history
* **Runs** (green): Executions that pair an assistant + thread

**Example combinations:**

* **Run: A1 + T1**: Assistant 1 configuration applied to User A’s conversation
* **Run: A1 + T2**: Same assistant serving User B (different conversation)
* **Run: A2 + T1**: Different assistant applied to User A’s conversation (configuration switch)

When executing a run:

* Each run may have its own input, configuration overrides, and metadata.
* Runs can be stateless (no thread) or stateful (executed on a [thread](/langsmith/use-threads) for conversation persistence).
* Multiple runs can use the same assistant configuration.
* The assistant’s configuration affects how the underlying graph executes.

The Agent Server API provides several endpoints for creating and managing runs. For more details, refer to the [API reference](/langsmith/server-api-ref).

## In this section

## Kick off background runs

Run your agent asynchronously and poll for results.

## Run multiple agents on the same thread

Use multiple assistants on a shared thread to combine agent capabilities.

## Stateless runs

Execute runs without persisting state when conversation history isn’t needed.

## Cancel a run

Cancel a single run or multiple runs via the API.

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/runs.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).