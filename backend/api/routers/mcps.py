from contextlib import asynccontextmanager
from typing import Iterable

from config import settings
from fastapi import APIRouter
from mcp import ClientSession, types
from mcp.client.sse import sse_client

from shared_mcp.models import ToolRequest

router = APIRouter(prefix="/mcps", tags=["mcps"])


@asynccontextmanager
async def mcp_sse_client():
    async with sse_client(f"http://mcp:{settings.mcp_server_port}/sse") as (
        read_stream,
        write_stream,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            yield session


@router.get("/list-tools")
async def list_tools() -> Iterable[types.Tool]:
    """
    Lists tools available from MCP server

    This endpoint establishes a Server-Sent Events connection with the client
    and forwards communication to the Model Context Protocol server.
    """
    async with mcp_sse_client() as session:
        response = await session.list_tools()
        return response.tools


@router.post("/call-tool")
async def call_tool(request: ToolRequest) -> str:
    """
    Calls tool available from MCP server

    This endpoint establishes a Server-Sent Events connection with the client
    and forwards communication to the Model Context Protocol server.
    """
    async with mcp_sse_client() as session:
        response = await session.call_tool(
            request.tool_name,
            arguments=request.model_dump(exclude=["tool_name"]),
        )
        return response.content[0].text
