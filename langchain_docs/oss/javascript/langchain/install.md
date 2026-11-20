---
title: "Install LangChain - Docs by LangChain"
url: https://docs.langchain.com/oss/javascript/langchain/install
scraped_at: 2026-11-15T03:43:40.320573
word_count: 226
---

To install the LangChain package:

npm

pnpm

yarn

bun

```
npm install langchain @langchain/core
# Requires Node.js 22+
```

```
pnpm add langchain @langchain/core
# Requires Node.js 22+
```

```
yarn add langchain @langchain/core
# Requires Node.js 22+
```

```
bun add langchain @langchain/core
# Requires Bun v1.0.0+
```

LangChain provides integrations to hundreds of LLMs and thousands of other integrations. These live in independent provider packages.

npm

pnpm

yarn

bun

```
# Installing the OpenAI integration
npm install @langchain/openai
# Installing the Anthropic integration
npm install @langchain/anthropic
```

```
# Installing the OpenAI integration
pnpm install @langchain/openai
# Installing the Anthropic integration
pnpm install @langchain/anthropic
```

```
# Installing the OpenAI integration
yarn add @langchain/openai
# Installing the Anthropic integration
yarn add @langchain/anthropic
```

```
# Installing the OpenAI integration
bun add @langchain/openai
# Installing the Anthropic integration
bun add @langchain/anthropic
```

See the [Integrations tab](/oss/javascript/integrations/providers/overview) for a full list of available integrations.

Now that you have LangChain installed, you can get started by following the [Quickstart guide](/oss/javascript/langchain/quickstart).

Set up [LangSmith](https://smith.langchain.com?utm_source=docs&utm_medium=cta&utm_campaign=langsmith-signup&utm_content=oss-langchain-install) tracing to debug your first LangChain app. Follow the [tracing quickstart](/langsmith/trace-with-langchain) to get started. We recommend you also set up [LangSmith Engine](/langsmith/engine) which monitors your traces, detects issues, and proposes fixes.

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langchain/install.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).