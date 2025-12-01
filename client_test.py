import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def get_sources():
    async with client:
        result = await client.call_tool("get_sources", {})
        print(result)

asyncio.run(get_sources())
