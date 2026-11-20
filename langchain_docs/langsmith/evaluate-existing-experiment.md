---
title: "How to add evaluators to an existing experiment (Python only) - Docs by LangChain"
url: https://docs.langchain.com/langsmith/evaluate-existing-experiment
scraped_at: 2026-11-15T03:38:52.354586
word_count: 180
---

Evaluation of existing experiments is currently only supported in the Python SDK.
After running an experiment, you may want to **add new evaluation metrics without re-running your application**. This is useful when you’ve added new evaluators or want to apply different scoring criteria to existing results. Instead of re-executing your target function on all examples, you can evaluate the existing experiment traces directly.
To add evaluators to an existing experiment, pass the experiment name or ID to `evaluate()` / `aevaluate()` instead of a target function. The evaluators will run on the cached traces from the original experiment, accessing the inputs, outputs, and any intermediate steps that were logged.

## Example

```
from langsmith import evaluate

def always_half(inputs: dict, outputs: dict) -> float:
    return 0.5

experiment_name = "my-experiment:abc"  # Replace with an actual experiment name or ID

evaluate(experiment_name, evaluators=[always_half])
```

## Related topics

* [Retry failed examples in experiments](/langsmith/evaluate-with-retry)
* [Run an evaluation](/langsmith/evaluate-llm-application)
* [Run an evaluation asynchronously](/langsmith/evaluation-async)

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/evaluate-existing-experiment.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).