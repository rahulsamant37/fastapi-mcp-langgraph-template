# Langfuse

> Traces, evals, prompt management and metrics to debug and improve your LLM application.

Learn more [here](https://langfuse.com/)

[![LangFuse](https://img.shields.io/github/stars/langfuse/langfuse?logo=langfuse&label=LangFuse)](https://github.com/langfuse/langfuse)

Below is an outline of the steps involved in a simple Math Agent. Key elements illustrated include:

- A visual breakdown of each step—e.g., when the agent invokes a tool and when control returns to the agent
- Inputs and outputs at each stage of the process:
  - **User to Agent**: The user asks a natural language question — e.g., `What is 1 + 1?`
  - **Agent to Tool**: The agent decides to call a calculator tool with structured arguments — e.g., `args: { a: 1, b: 1 }`.
  - **Tool to Agent**: The tool executes the operation and returns the result — e.g., `2`.
  - **Agent to User**: The agent responds with the final answer in natural language — e.g., `1 + 1 = 2`.
- The full chat history throughout the interaction
- Latency and cost associated with each node

### Step 1: Math Agent (User to Agent → Agent to Tool)

This section shows:

- **User to Agent**: The user asks a natural language question — e.g., `What is 1 + 1?`
- **Agent to Tool**: The agent decides to call a calculator tool with structured arguments — e.g., `args: { a: 1, b: 1 }`.
- **Full Chat History Throughout the Interaction**: You can inspect earlier user-agent messages. For instance:

```text
User: reply only no
Agent: No.
```

In this example, the agent responded directly without calling any tools.

### Step 2: Tool Call (Tool to Agent)

This section shows:

  - **Tool to Agent**: The tool executes the operation and returns the result — e.g., `2`.

### Step 3: Math Agent (Agent to User)

This section shows:

  - **Agent to User**: The agent responds with the final answer in natural language — e.g., `1 + 1 = 2`.
