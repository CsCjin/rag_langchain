---
title: "Using standard tests - Docs by LangChain"
url: https://docs.langchain.com/oss/javascript/contributing/standard-tests-langchain
scraped_at: 2026-11-15T03:42:56.343174
word_count: 481
---

**Standard tests ensure your integration works as expected.**
When creating either a custom class for yourself or to publish in a LangChain integration, it is necessary to add tests to ensure it works as expected. LangChain provides a comprehensive [set of tests](https://pypi.org/project/langchain-tests/) for each integration type for you. This guide will show you how to add LangChain’s standard test suite to each integration type.

## Setup

First, install the required dependencies:

## langchain-core

Defines the interfaces we want to import to define our custom components

## langchain-tests

Provides the standard tests and plugins necessary to run them

npm

pnpm

yarn

bun

```
npm install @langchain/core
npm install @langchain/standard-tests
```

```
pnpm add @langchain/core
pnpm add @langchain/standard-tests
```

```
yarn add @langchain/core
yarn add @langchain/standard-tests
```

```
bun add @langchain/core
bun add @langchain/standard-tests
```

There are 2 namespaces in the `langchain-tests` package:

Unit tests

**Location**: `src.unit_tests`Designed to test the component in isolation and without access to external services[View API reference](https://reference.langchain.com/python/langchain-tests/unit_tests)

Integration tests

**Location**: `src.integration_tests`Designed to test the component with access to external services (in particular, the external service that the component is designed to interact with)[View API reference](https://reference.langchain.com/python/langchain-tests/integration_tests)

## Implementing standard tests

Depending on your integration type, you will need to implement either or both unit and integration tests.
By subclassing the standard test suite for your integration type, you get the full collection of standard tests for that type. For a test run to be successful, a given test should pass only if the model supports the capability being tested. Otherwise, the test should be skipped.
Because different integrations offer unique sets of features, most standard tests provided by LangChain are **opt-in by default** to prevent false positives. Consequently, you will need to override properties to indicate which features your integration supports - see the below example for an illustration.

tests/chat\_models.standard.int.test.ts

```
// Indicate that a chat model supports parallel tool calls

class ChatParrotLinkStandardIntegrationTests extends ChatModelIntegrationTests<
    ChatParrotLinkCallOptions,
    AIMessageChunk
> {
    constructor() {
        // ... other required properties

        super({
            // ... other required properties
            supportsParallelToolCalls: true,  // (The default is False)
            // ...
        });
    }
```

You should organize tests in these subdirectories relative to the root of your package:

* `tests/unit_tests` for unit tests
* `tests/integration_tests` for integration tests

To see the complete list of configurable capabilities and their defaults, see [Implementing standard tests](/oss/javascript/contributing/standard-tests-langchain#implementing-standard-tests).

## Sandbox integrations

Deep Agents sandbox integrations use `sandboxStandardTests` from `@langchain/sandbox-standard-tests`.
Call it with a config object that includes `createSandbox`, `resolvePath`, and `closeSandbox`.
Use the [Daytona integration tests](https://github.com/langchain-ai/deepagentsjs/blob/main/libs/providers/daytona/src/sandbox.int.test.ts) as a reference implementation.
See [Contributing a sandbox integration](/oss/javascript/contributing/integrations-langchain) for publishing guidelines.

---

## Troubleshooting

For a full list of the standard test suites that are available, as well as information on which tests are included and how to troubleshoot common issues, see the [contributing README](https://github.com/langchain-ai/langchainjs/blob/main/CONTRIBUTING.md).

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/contributing/standard-tests-langchain.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).