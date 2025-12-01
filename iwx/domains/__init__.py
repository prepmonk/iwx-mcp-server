from fastmcp import FastMCP

from iwx.domains.pipelines.pipelines import pipelines_mcp
from iwx.domains.workflows.workflows import workflows_mcp

domains_mcp = FastMCP("Domains")


domains_mcp.mount(pipelines_mcp, as_proxy=True)
domains_mcp.mount(workflows_mcp, as_proxy=True)
