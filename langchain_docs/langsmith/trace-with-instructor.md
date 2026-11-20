---
title: "Trace with Instructor - Docs by LangChain"
url: https://docs.langchain.com/langsmith/trace-with-instructor
scraped_at: 2026-11-15T03:42:40.518084
word_count: 307
---

LangSmith provides a convenient integration with [Instructor](https://python.useinstructor.com/), a popular open-source library for generating structured output with LLMs.

In an [agent-based workspace](/langsmith/agent-registry), [create an agent](/langsmith/create-an-agent) once before sending traces. Use [agent addressing](/langsmith/log-traces-to-agent) to select its identifier and environment. If an integration requires `project_name`, use the selected environment’s [`tracer_session_name`](/langsmith/create-an-agent#use-an-environment-project) as a compatibility value.

In order to use, you first need to set your LangSmith API key.

```
export LANGSMITH_API_KEY=<your-api-key>
export LANGSMITH_AGENT_ID="<your-agent-id>"
export LANGSMITH_AGENT_ENVIRONMENT="local"
# For LangSmith API keys linked to multiple workspaces, set the LANGSMITH_WORKSPACE_ID environment variable to specify which workspace to use.
export LANGSMITH_WORKSPACE_ID=<your-workspace-id>
```

Next, you will need to install the LangSmith SDK:

pip

uv

```
pip install -U langsmith
```

```
uv add langsmith
```

Wrap your OpenAI client with `langsmith.wrappers.wrap_openai`

```
from openai import OpenAI
from langsmith import wrappers

client = wrappers.wrap_openai(OpenAI())
```

After this, you can patch the wrapped OpenAI client using `instructor`:

```
import instructor

client = instructor.patch(client)
```

Now, you can use `instructor` as you normally would, but now everything is logged to LangSmith!

```
from pydantic import BaseModel

class UserDetail(BaseModel):
    name: str
    age: int

user = client.chat.completions.create(
    model="gpt-6-luna",
    response_model=UserDetail,
    messages=[
        {"role": "user", "content": "Extract Jason is 25 years old"},
    ]
)
```

Oftentimes, you use `instructor` inside of other functions.
You can get nested traces by using this wrapped client and decorating those functions with `@traceable`.
Please see [Custom instrumentation](/langsmith/annotate-code) for more information on how to annotate your code for tracing with the `@traceable` decorator.

```
from langsmith import traceable

# You can customize the run name with the `name` keyword argument
@traceable(name="Extract User Details")
def my_function(text: str) -> UserDetail:
    return client.chat.completions.create(
        model="gpt-6-luna",
        response_model=UserDetail,
        messages=[
            {"role": "user", "content": f"Extract {text}"},
        ]
    )

my_function("Jason is 25 years old")
```

---

[Connect these docs](/use-these-docs) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/trace-with-instructor.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).