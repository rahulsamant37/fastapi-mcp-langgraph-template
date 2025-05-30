import osAdd commentMore actions

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "MCP Server",
    host=os.environ["MCP_SERVER_HOST"],
    port=os.environ["MCP_SERVER_PORT"],
)


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
