
from fastmcp import FastMCP

from iwx.constants import make_get_call, make_call

source_mcp = FastMCP("Sources")

SOURCES_URI = '/sources'

@source_mcp.tool(description="Get Total Sources Count")
def get_sources_count() -> int:
    source_count_uri = SOURCES_URI
    total_count = make_get_call(source_count_uri, keys=['total_count'])['total_count']
    return total_count

@source_mcp.tool(description="Get Sources List")
def get_sources() -> dict:
    source_uri = SOURCES_URI
    results = make_get_call(source_uri, recursive=True)['result']
    
    data = {}
    for result in results:
        data[result['name']] = {
            'id': result['id'],
            'type': result['type'], 
            'sub_type': result['sub_type']
            }
    print(data)
    return data

@source_mcp.tool(description="Get Source Info")
def get_source_info(source_id: str | None = None) -> dict:
    source_uri = f'{SOURCES_URI}/{source_id}'
    response_data = make_call('GET', source_uri)
    result = response_data['result']
    return result
