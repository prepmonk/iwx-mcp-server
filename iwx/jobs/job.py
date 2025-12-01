
from fastmcp import FastMCP

from iwx.constants import make_call

jobs_mcp = FastMCP("Jobs")

def parse_results(results: dict) -> dict:
    data = {}
    for result in results:
        data[result['name']] = {
            'id': result['id'],
            'name': result['name'],
            'state': result['state']
        }
    return data

@jobs_mcp.tool(description="Get source jobs")
def get_source_jobs(source_id: str) -> dict:
    uri = f'/sources/{source_id}/jobs'
    response = make_call('GET', uri)
    return parse_results(response.json()['result'])
    

@jobs_mcp.tool(description="Get pipeline jobs")
def get_pipeline_jobs(pipeline_id: str) -> dict:
    uri = f'/pipelines/{pipeline_id}/jobs'
    response = make_call('GET', uri)
    return parse_results(response.json()['result'])
