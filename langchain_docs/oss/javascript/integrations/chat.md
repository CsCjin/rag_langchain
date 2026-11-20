---
title: "Chat model integrations - Docs by LangChain"
url: https://docs.langchain.com/oss/javascript/integrations/chat
scraped_at: 2026-11-15T03:43:17.991288
word_count: 1237
---

[Chat models](/oss/javascript/langchain/models) are language models that use a sequence of [messages](/oss/javascript/langchain/messages) as inputs and return messages as outputs (as opposed to plaintext).

## Install and use

See [this section for general instructions on installing LangChain packages](/oss/javascript/langchain/install).

OpenAI

Install:

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
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({ model: "gpt-5.4-mini" });
```

```
await model.invoke("Hello, world!")
```

Anthropic

Install:

npm

yarn

pnpm

```
npm i @langchain/anthropic @langchain/core
```

```
yarn add @langchain/anthropic @langchain/core
```

```
pnpm add @langchain/anthropic @langchain/core
```

Add environment variables:

```
ANTHROPIC_API_KEY=your-api-key
```

Instantiate the model:

```
import { ChatAnthropic } from "@langchain/anthropic";

const model = new ChatAnthropic({
model: "claude-sonnet-4-6",
temperature: 0
});
```

```
await model.invoke("Hello, world!")
```

Google Gemini

Install:

npm

yarn

pnpm

```
npm install @langchain/google @langchain/core
```

```
yarn add @langchain/google @langchain/core
```

```
pnpm add @langchain/google @langchain/core
```

Add environment variables:

```
GOOGLE_API_KEY=your-api-key
```

Instantiate the model:

```
import { ChatGoogle } from "@langchain/google";

const model = new ChatGoogle("gemini-4-hydrogen");
```

```
await model.invoke("Hello, world!")
```

MistralAI

Install:

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
import { ChatMistralAI } from "@langchain/mistralai";

const model = new ChatMistralAI({
model: "mistral-large-latest",
temperature: 0
});
```

```
await model.invoke("Hello, world!")
```

Groq

Install:

npm

yarn

pnpm

```
npm install @langchain/groq @langchain/core
```

```
yarn add @langchain/groq @langchain/core
```

```
pnpm add @langchain/groq @langchain/core
```

Add environment variables:

```
GROQ_API_KEY=your-api-key
```

Instantiate the model:

```
import { ChatGroq } from "@langchain/groq";

const model = new ChatGroq({
model: "openai/gpt-oss-120b",
temperature: 0
});
```

```
await model.invoke("Hello, world!")
```

## Featured models

**While these LangChain classes support the indicated advanced feature**, you may need to refer to provider-specific documentation to learn which hosted models or backends support the feature.

| Model | Stream | [Tool Calling](/oss/javascript/langchain/tools/) | [`withStructuredOutput()`](/oss/javascript/langchain/models#structured-output) | [`Multimodal`](/oss/javascript/langchain/messages#multimodal) | Downloads |
| --- | --- | --- | --- | --- | --- |
| [`ChatOpenAI`](/oss/javascript/integrations/chat/openai) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/openai) |
| [`ChatAnthropic`](/oss/javascript/integrations/chat/anthropic) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/anthropic) |
| [`ChatBedrockConverse`](/oss/javascript/integrations/chat/bedrock_converse) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/aws) |
| [`ChatGroq`](/oss/javascript/integrations/chat/groq) | ✅ | ✅ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/@langchain/groq) |
| [`ChatOllama`](/oss/javascript/integrations/chat/ollama) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/ollama) |
| [`ChatMistralAI`](/oss/javascript/integrations/chat/mistral) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/mistralai) |
| [`ChatGoogle`](/oss/javascript/integrations/chat/google) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/google) |
| [`ChatCohere`](/oss/javascript/integrations/chat/cohere) | ✅ | ✅ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/@langchain/cohere) |
| [`ChatXAI`](/oss/javascript/integrations/chat/xai) | ✅ | ✅ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/@langchain/xai) |
| [`ChatFireworks`](/oss/javascript/integrations/chat/fireworks) | ✅ | ✅ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/@langchain/fireworks) |
| [`ChatCloudflareWorkersAI`](/oss/javascript/integrations/chat/cloudflare_workersai) | ✅ | ❌ | ❌ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/cloudflare) |
| [`ChatTogetherAI`](/oss/javascript/integrations/chat/togetherai) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/together-ai) |
| [`ChatPerplexity`](/oss/javascript/integrations/chat/perplexity) | ✅ | ❌ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/@langchain/perplexity) |

See the [full list of chat model integrations](#all-chat-models) below for more options.

## Routers & proxies

Routers and proxies give you access to models from multiple providers through a single API and credential. They can simplify billing, let you switch between models without changing integrations, and offer features like automatic fallbacks.

| Provider | Integration | Description |
| --- | --- | --- |
| [OpenRouter](https://openrouter.ai/) | [`ChatOpenRouter`](/oss/javascript/integrations/chat/openrouter) | Unified access to models from OpenAI, Anthropic, Google, Meta, and more |

## Chat Completions API

Certain model providers offer endpoints that are compatible with OpenAI’s (legacy) [Chat Completions API](https://platform.openai.com/docs/guides/completions). In such case, you can use [`ChatOpenAI`](/oss/javascript/integrations/chat/openai) with a custom `base_url` to connect to these endpoints. Note that features built on top of the Chat Completions API may not be fully supported by `ChatOpenAI`; in such cases, consider using a provider-specific class if available.

## All chat models

| Model | Stream | [Tool Calling](/oss/javascript/langchain/tools/) | [`withStructuredOutput()`](/oss/javascript/langchain/models#structured-output) | [`Multimodal`](/oss/javascript/langchain/messages#multimodal) | Downloads |
| --- | --- | --- | --- | --- | --- |
| [`AzureChatOpenAI`](/oss/javascript/integrations/chat/azure) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/openai) |
| [`ChatOpenAI`](/oss/javascript/integrations/chat/openai) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/openai) |
| [`ChatAnthropic`](/oss/javascript/integrations/chat/anthropic) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/anthropic) |
| [`ChatGoogleGenerativeAI`](/oss/javascript/integrations/chat/google_generative_ai) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/google-genai) |
| [`ChatBedrockConverse`](/oss/javascript/integrations/chat/bedrock_converse) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/aws) |
| [`ChatVertexAI`](/oss/javascript/integrations/chat/google_vertex_ai) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/google-vertexai) |
| [`ChatGroq`](/oss/javascript/integrations/chat/groq) | ✅ | ✅ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/@langchain/groq) |
| [`ChatOllama`](/oss/javascript/integrations/chat/ollama) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/ollama) |
| [`ChatMistralAI`](/oss/javascript/integrations/chat/mistral) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/mistralai) |
| [`ChatGoogle`](/oss/javascript/integrations/chat/google) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/google) |
| [`ChatCohere`](/oss/javascript/integrations/chat/cohere) | ✅ | ✅ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/@langchain/cohere) |
| [`ChatXAI`](/oss/javascript/integrations/chat/xai) | ✅ | ✅ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/@langchain/xai) |
| [`ChatOpenRouter`](/oss/javascript/integrations/chat/openrouter) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/openrouter) |
| [`ChatDeepSeek`](/oss/javascript/integrations/chat/deepseek) | ✅ | ✅ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/@langchain/deepseek) |
| [`ChatCerebras`](/oss/javascript/integrations/chat/cerebras) | ✅ | ✅ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/@langchain/cerebras) |
| [`ChatFireworks`](/oss/javascript/integrations/chat/fireworks) | ✅ | ✅ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/@langchain/fireworks) |
| [`ChatBaiduQianfan`](/oss/javascript/integrations/chat/baidu_qianfan) |  |  |  |  | [Downloads per month](https://www.npmjs.com/package/@langchain/baidu-qianfan) |
| [`ChatCloudflareWorkersAI`](/oss/javascript/integrations/chat/cloudflare_workersai) | ✅ | ❌ | ❌ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/cloudflare) |
| [`ChatTogetherAI`](/oss/javascript/integrations/chat/togetherai) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/together-ai) |
| [`ChatWatsonx`](/oss/javascript/integrations/chat/ibm) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@langchain/ibm) |
| [`ChatPerplexity`](/oss/javascript/integrations/chat/perplexity) | ✅ | ❌ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/@langchain/perplexity) |
| [`ChatYandexGPT`](/oss/javascript/integrations/chat/yandex) |  |  |  |  | [Downloads per month](https://www.npmjs.com/package/@langchain/yandex) |
| [`ChatWebLLM`](https://github.com/ykoh42/web-llm-adapters/blob/main/packages/langchain-web-llm/README.md) | ✅ | ✅ | ✅ |  | [Downloads per month](https://www.npmjs.com/package/langchain-web-llm) |
| [`ChatEmpirioLabs`](https://docs.empiriolabs.ai/integrations#langchain) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@empiriolabs/langchain) |
| [`ChatExaone`](https://github.com/ykoh42/exaone-integrations/tree/main/packages/langchain-exaone-ts) | ✅ | ✅ | ✅ | ❌ | [Downloads per month](https://www.npmjs.com/package/langchain-exaone) |
| [`ChatInterfaze`](https://interfaze.ai/docs) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@interfaze-ai/langchain) |
| [`ChatKServe`](https://gitlab.com/bitkaio/langchain/kserve-provider) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@bitkaio/langchain-kserve) |
| [`RecallToolkit`](https://recallmem.dev/guides/langchain) |  |  |  |  | [Downloads per month](https://www.npmjs.com/package/@recall-memory/langchain) |
| [`ChatSCX`](https://scx.ai/) | ✅ | ✅ | ✅ | ✅ | [Downloads per month](https://www.npmjs.com/package/@scx-ai/langchain) |
| [`ChatObscurify`](https://github.com/Obscurify-ai/langchain-obscurify) | ✅ | ✅ | ✅ |  | [Downloads per month](https://www.npmjs.com/package/@obscurify/langchain) |
| [`Auxen`](https://auxen.ai) | ✅ | ✅ | ✅ | ❌ | N/A |
| [`FakeListChatModel`](/oss/javascript/integrations/chat/fake) |  |  |  |  | N/A |
| [`Tuning Engines`](https://www.tuningengines.com/) | ✅ | ✅ | ✅ | ❌ | N/A |

If you’d like to contribute an integration, see [Contributing integrations](/oss/javascript/contributing#add-a-new-integration).

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/chat/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).