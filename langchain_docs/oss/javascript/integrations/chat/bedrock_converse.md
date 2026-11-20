---
title: "ChatBedrockConverse integration - Docs by LangChain"
url: https://docs.langchain.com/oss/javascript/integrations/chat/bedrock_converse
scraped_at: 2026-11-15T03:43:16.069143
word_count: 602
---

[Amazon Bedrock Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) is a fully managed service that makes Foundation Models (FMs) from leading AI startups and Amazon available via an API. You can choose from a wide range of FMs to find the model that is best suited for your use case. It provides a unified conversational interface for Bedrock models.
This will help you getting started with `ChatBedrockConverse` [chat models](/oss/javascript/langchain/models). For detailed documentation of all `ChatBedrockConverse` features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-aws/ChatBedrockConverse).

## Overview

### Integration details

| Class | Package | Serializable | [PY support](/oss/python/integrations/chat/bedrock) | Downloads | Version |
| --- | --- | --- | --- | --- | --- |
| [`ChatBedrockConverse`](https://reference.langchain.com/javascript/langchain-aws/ChatBedrockConverse) | [`@langchain/aws`](https://npmjs.com/@langchain/aws) | ✅ | ✅ | NPM - Downloads | NPM - Version |

### Model features

See the links in the table headers below for guides on how to use specific features.

| [Tool calling](/oss/javascript/langchain/tools) | [Structured output](/oss/javascript/langchain/structured-output) | [Image input](/oss/javascript/langchain/messages#multimodal) | Audio input | Video input | [Token-level streaming](/oss/javascript/langchain/streaming/) | [Token usage](/oss/javascript/langchain/models#token-usage) | [Logprobs](/oss/javascript/langchain/models#log-probabilities) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ |

## Setup

To access Bedrock models you’ll need to create an AWS account, set up the Bedrock API service, get an access key ID and secret key, and install the `@langchain/aws` integration package.

### Credentials

Head to the [AWS docs](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html) to sign up for AWS and setup your credentials. You’ll also need to turn on model access for your account, which you can do by [following these instructions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html).
Set your Bedrock credentials in the environment:

```
export BEDROCK_AWS_REGION="us-east-1"
export BEDROCK_AWS_ACCESS_KEY_ID="your-access-key-id"
export BEDROCK_AWS_SECRET_ACCESS_KEY="your-secret-access-key"
```

Alternatively, set `AWS_BEARER_TOKEN_BEDROCK` for API key authentication. See the [AWS Bedrock API key docs](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html).
If you want to get automated tracing of your model calls you can also set your [LangSmith](/langsmith/observability) API key by uncommenting below:

```
# export LANGSMITH_TRACING="true"
# export LANGSMITH_API_KEY="your-api-key"
```

### Installation

The LangChain `ChatBedrockConverse` integration lives in the `@langchain/aws` package:

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

## Instantiation

Now we can instantiate our model object and generate chat completions.
There are a few different ways to authenticate with AWS - the below examples rely on an access key, secret access key and region set in your environment variables:

```
import { ChatBedrockConverse } from "@langchain/aws";

const llm = new ChatBedrockConverse({
  model: "us.anthropic.claude-sonnet-4-6",
  region: process.env.BEDROCK_AWS_REGION,
  credentials: {
    accessKeyId: process.env.BEDROCK_AWS_ACCESS_KEY_ID!,
    secretAccessKey: process.env.BEDROCK_AWS_SECRET_ACCESS_KEY!,
  },
});
```

## Invocation

```
const aiMsg = await llm.invoke([
  [
    "system",
    "You are a helpful assistant that translates English to French. Translate the user sentence.",
  ],
  ["human", "I love programming."],
])
aiMsg
```

```
AIMessage {
  "id": "f5dc5791-224e-4fe5-ba2e-4cc51d9e7795",
  "content": "J'adore la programmation.",
  "additional_kwargs": {},
  "response_metadata": {
    "$metadata": {
      "httpStatusCode": 200,
      "requestId": "f5dc5791-224e-4fe5-ba2e-4cc51d9e7795",
      "attempts": 1,
      "totalRetryDelay": 0
    },
    "metrics": {
      "latencyMs": 584
    },
    "stopReason": "end_turn",
    "usage": {
      "inputTokens": 29,
      "outputTokens": 11,
      "totalTokens": 40
    }
  },
  "tool_calls": [],
  "invalid_tool_calls": [],
  "usage_metadata": {
    "input_tokens": 29,
    "output_tokens": 11,
    "total_tokens": 40
  }
}
```

```
console.log(aiMsg.content)
```

```
J'adore la programmation.
```

## Tool calling

Tool calling with Bedrock models works in a similar way to [other models](/oss/javascript/langchain/tools), but note that not all Bedrock models support tool calling. Please refer to the [AWS model documentation](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html) for more information.

---

## API reference

For detailed documentation of all `ChatBedrockConverse` features and configurations head to the [API reference](https://reference.langchain.com/javascript/langchain-aws/ChatBedrockConverse).

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/chat/bedrock_converse.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).