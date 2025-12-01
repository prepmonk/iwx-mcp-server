from fastmcp import FastMCP
from fastmcp.server.middleware import Middleware, MiddlewareContext

from iwx.sources.sources import source_mcp
from iwx.sources.table_groups import table_group_mcp
from iwx.domains import domains_mcp
from iwx.jobs.job import jobs_mcp

from dotenv import load_dotenv
load_dotenv()

mcp = FastMCP("Infoworks MCP Server")

class CustomHeaderMiddleware(Middleware):
    async def on_request(self, context: MiddlewareContext, call_next):
        # Add custom logic here
        print(f"Processing {context.method}")
        
        result = await call_next(context)
        
        print(f"Completed {context.method}")
        return result

mcp.add_middleware(CustomHeaderMiddleware())

mcp.mount(source_mcp)
mcp.mount(table_group_mcp)
# mcp.mount(domains_mcp, as_proxy=True)
# mcp.mount(jobs_mcp, as_proxy=True)

