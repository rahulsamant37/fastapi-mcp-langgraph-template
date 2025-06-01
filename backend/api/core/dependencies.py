from contextlib import asynccontextmanager
from typing import Annotated, AsyncGenerator

from fastapi import Depends
from langchain_openai import ChatOpenAI
from mcp import ClientSession
from mcp.client.sse import sse_client
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from api.core.config import settings


def get_llm() -> ChatOpenAI:
    return ChatOpenAI(
        streaming=True,
        model=settings.model,
        temperature=0,
        api_key=settings.openai_api_key,
        stream_usage=True,
    )


LLMDep = Annotated[ChatOpenAI, Depends(get_llm)]


engine: AsyncEngine = create_async_engine(settings.orm_conn_str)


def get_engine() -> AsyncEngine:
    return engine


EngineDep = Annotated[AsyncEngine, Depends(get_engine)]


@asynccontextmanager
async def mcp_sse_client() -> AsyncGenerator[ClientSession, None]:
    async with sse_client(f"http://mcp:{settings.mcp_server_port}/sse") as (
        read_stream,
        write_stream,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            yield session