from fastmcp import FastMCP
from iwx.constants import make_call

workflows_mcp = FastMCP("Workflows")


@workflows_mcp.tool(description="Get all domain workflows")
def get(domain_id: str) -> dict:
    uri = f'/domains/{domain_id}/workflows'
    response = make_call('GET', uri)

    results = response.json()['result']
    data = {}
    for result in results:
        data[result['id']] = result['name']

    return data

