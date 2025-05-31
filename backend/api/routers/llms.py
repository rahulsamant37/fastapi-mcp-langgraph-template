from typing import AsyncGenerator

from fastapi import APIRouter
from langchain_core.messages import HumanMessage
from sse_starlette.sse import EventSourceResponse
from starlette.responses import Response

from api.dependencies import LLMDep, get_config, get_graph

router = APIRouter(tags=["chat"])


async def stream_completions(
    query: str, llm: LLMDep
) -> AsyncGenerator[dict[str, str], None]:
    async for chunk in llm.astream_events(query):
        yield dict(data=chunk)


@router.get("/chat/completions")
async def completions(query: str, llm: LLMDep) -> Response:
    """Stream completions via Server Sent Events"""
    return EventSourceResponse(stream_completions(query, llm))


async def stream_graph(
    query: str,
    llm: LLMDep,
) -> AsyncGenerator[dict[str, str], None]:
    graph = get_graph(llm)
    config = get_config()
    events = dict(messages=[HumanMessage(content=query)])

    async for event in graph.astream_events(events, config, version="v2"):
        yield dict(data=event)


@router.get("/chat/agent")
async def agent(query: str, llm: LLMDep) -> Response:
    """Stream LangGraph completions via Server Sent Events"""
    return EventSourceResponse(stream_graph(query, llm))
