from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse

from app.dependencies import LLMDep

router = APIRouter()


async def stream(query: str, llm: LLMDep):
    async for chunk in llm.astream_events(query):
        yield dict(data=chunk)


@router.get("/chat/completions", tags=["/chat"])
async def completions(query: str, llm: LLMDep):
    return EventSourceResponse(stream(query, llm))
