# LangGraph

> Gain control with LangGraph to design agents that reliably handle complex tasks.

Learn more [here](https://www.langchain.com/langgraph)

[![LangGraph](https://img.shields.io/github/stars/langchain-ai/langgraph?logo=langgraph&label=LangGraph)](https://github.com/langchain-ai/langgraph)

## Streaming

At its core, a compiled LangGraph is a [Runnable](https://github.com/langchain-ai/langchain/blob/langchain%3D%3D0.3.6/libs/core/langchain_core/runnables/base.py#L108). This template utilizes LangChain’s built-in streaming support through [`astream_events`](https://python.langchain.com/docs/how_to/streaming/#using-stream-events), granting programmatic access to every stage of the Agentic Workflow. You can observe and interact with key components—LLM, prompt, and tool—throughout their full execution lifecycle: start, stream, and end. For a comprehensive list of event types and usage examples, refer to the [Event Reference](https://python.langchain.com/docs/how_to/streaming/#event-reference).

## Persistence

LangGraph offers built-in state management and persistence via the [AsyncPostgresSaver](https://github.com/langchain-ai/langgraph/blob/0.2.39/libs/checkpoint-postgres/langgraph/checkpoint/postgres/aio.py#L39), enabling faster iteration on agentic workflows. Since LLMs are inherently stateless, chat history must typically be injected as context for each query—but LangGraph abstracts this away, requiring only a `thread_id`. It seamlessly handles chat history and metadata serialization/deserialization, simplifying development. Learn more about its advanced persistence capabilities [here](https://langchain-ai.github.io/langgraph/concepts/persistence/).
