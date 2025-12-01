
from fastmcp import FastMCP

from iwx.constants import make_call

table_group_mcp = FastMCP("Table Group")

@table_group_mcp.tool(description="Get all source table groups")
def get_table_groups(source_id: str) -> dict:
    uri = f'/sources/{source_id}/table-groups'
    response = make_call('GET', uri)
    results = response.json()['result']
    data = {}
    for result in results:
        data[result['id']] = result['name']
    
    return data


