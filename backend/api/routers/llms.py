from typing import AsyncGenerator

from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse
from starlette.responses import Response

from api.dependencies import LLMDep

router = APIRouter(tags=["chat"])


async def stream(
    query: str, llm: LLMDep
) -> AsyncGenerator[dict[str, str], None]:
    async for chunk in llm.astream_events(query):
        yield dict(data=chunk)


@router.get("/chat/completions")
async def completions(query: str, llm: LLMDep) -> Response:
    """Stream completions via Server Sent Events"""
    return EventSourceResponse(stream(query, llm))
