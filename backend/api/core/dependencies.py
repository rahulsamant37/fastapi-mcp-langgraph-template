from contextlib import asynccontextmanager
from typing import Annotated, AsyncGenerator

import psycopg.errors
from fastapi import Depends
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from mcp import ClientSession
from mcp.client.sse import sse_client
from psycopg_pool import AsyncConnectionPool
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine

from api.core.config import settings
from api.core.logs import uvicorn


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


async def checkpointer_setup(pool):
    checkpointer = AsyncPostgresSaver(pool)
    try:
        await checkpointer.setup()
    except (
        psycopg.errors.DuplicateColumn,
        psycopg.errors.ActiveSqlTransaction,
    ):
        uvicorn.warning("Skipping checkpointer setup — already configured.")
    return checkpointer


@asynccontextmanager
async def setup_graph():
    # NOTE: LangGraph AsyncPostgresSaver does not support SQLAlchemy ORM Connections.
    # A compatible psycopg connection is created via the connection pool to connect to the checkpointer.
    async with AsyncConnectionPool(
        conninfo=settings.checkpoint_conn_str,
        kwargs=dict(prepare_threshold=None),
    ) as pool:
        checkpointer = await checkpointer_setup(pool)

        async with mcp_sse_client() as session:
            tools = await load_mcp_tools(session)
            yield checkpointer, tools, session