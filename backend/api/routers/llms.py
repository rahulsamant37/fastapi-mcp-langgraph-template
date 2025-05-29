from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse

from api.dependencies import LLMDep

router = APIRouter(tags=["chat"])


async def stream(query: str, llm: LLMDep):
    async for chunk in llm.astream_events(query):
        yield dict(data=chunk)


@router.get("/chat/completions")
async def completions(query: str, llm: LLMDep):
    """Stream completions via Server Sent Event"""
    return EventSourceResponse(stream(query, llm))
