
from fastmcp import FastMCP

from iwx.constants import make_call

pipelines_mcp = FastMCP("Pipelines")

@pipelines_mcp.tool(description="Get all domain pipelines")
def get(domain_id: str, pipeline_id: str|None = None) -> dict:
    uri = f'/domains/{domain_id}/pipelines'
    response = make_call('GET', uri)

    results = response.json()['result']
    data = {}
    for result in results:
        data[result['id']] = result['name']

    return data
