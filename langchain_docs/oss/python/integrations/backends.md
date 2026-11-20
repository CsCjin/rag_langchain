---
title: "Backend integrations - Docs by LangChain"
url: https://docs.langchain.com/oss/python/integrations/backends
scraped_at: 2026-11-15T03:44:45.665640
word_count: 210
---

Browse available filesystem backends for Deep Agents or contribute your own to the ecosystem. Learn more about how backends work in the [backends docs](/oss/python/deepagents/backends).

## Share your backend

Custom backends connect Deep Agents to storage systems such as databases, object stores, and virtual filesystems. Share yours with the community:

## Implement a custom backend

Follow the custom backends guide to build your own backend.

## Share a community backend

Open a PR to the docs repo to add your backend to the table below.

## All backends

| Backend | Description | Package | Source |
| --- | --- | --- | --- |
| [Azure Blob Backend](https://github.com/langchain-ai/langchain-azure/tree/main/libs/azure-storage) | Azure Blob Storage implementation of the Deep Agents `BackendProtocol`. Persist agent workspace files, memories, and artifacts in a blob container. | `langchain-azure-storage` | [`langchain-ai/langchain-azure`](https://github.com/langchain-ai/langchain-azure/tree/main/libs/azure-storage) |
| [MongoDB VFS Adapter](https://github.com/langchain-ai/langchain-mongodb/tree/main/libs/langchain-mongodb-deepagents-vfs) | Virtual filesystem backend backed by MongoDB Atlas. Persist agent files, including memories, artifacts, and conversation history, in a MongoDB collection. | `langchain-mongodb-deepagents-vfs` | [`langchain-ai/langchain-mongodb`](https://github.com/langchain-ai/langchain-mongodb/tree/main/libs/langchain-mongodb-deepagents-vfs) |

Have a backend to share? [Open a PR](https://github.com/langchain-ai/docs) to add it here.

If you’d like to contribute an integration, see [Contributing integrations](/oss/python/contributing#add-a-new-integration).

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/integrations/backends/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).