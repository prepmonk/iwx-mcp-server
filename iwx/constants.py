import os
import requests

def get_auth_headers() -> dict:
    refresh_token = os.getenv('IWX_REFRESH_TOKEN')
    auth_url = "/security/token/access"
    headers = {
        'Authorization': f"Basic {refresh_token}"
    }

    response = _make_call('GET', auth_url, headers=headers)
    access_token = response.json()['result']['authentication_token']
    auth_headers = {
        'Authorization' : f'Bearer {access_token}'
    } 
    return auth_headers

def _make_call(method: str, 
              uri: str, 
              *,
              params: dict|None =None, 
              data: dict|None = None, 
              json: dict|None = None, 
              headers:dict | None=None,
              ) -> requests.Response:
    
    auth_headers = get_auth_headers() if headers is None else headers
    base_url = os.getenv('IWX_BASE_URL')
    request_url = f"{base_url}{uri}"

    response = requests.request(
        method=method, 
        url=request_url,
        params=params,
        data=data,
        json=json,
        headers=auth_headers, 
        verify=False)
    
    if response.status_code >= 400:
        raise Exception(f"Exception {str(response.text)}")
    return response

def make_get_call( uri: str, 
                  *, 
                  params: dict|None =None, 
                  data: dict|None = None, 
                  json: dict|None = None, 
                  headers:dict | None=None, 
                  keys: list[str] = ['result'],
                  recursive: bool = False,
                ) -> dict:
    method = 'GET'
    response = _make_call(method, uri, params=params, data=data, json=json, headers=headers)
    responses_data = []
    if response.json():
        response_data = response.json()
        responses_data.append(response_data)
        total_count = response_data['total_count']
        offset = response_data['limit'] + response_data['offset']
        while recursive:
            response = _make_call(method, uri, params={'offset': offset}, headers=headers)
            response_data = response.json()
            responses_data.append(response_data)
            offset = response_data['limit'] + response_data['offset']
            if total_count < offset:
                break
    filtered_data = {}
    for resonse_data in responses_data:
        for key in keys:
            _data = resonse_data[key]
            if key not in filtered_data:
                filtered_data[key] = _data
            elif isinstance(filtered_data[key], list):
                filtered_data[key].extend(_data)
            elif isinstance(filtered_data[key], set) or isinstance(filtered_data[key], dict):
                filtered_data[key].update(_data)
            else:
                raise Exception(f"Unable to update the keys, {type(filtered_data[key])}")
        
    return filtered_data


def make_call(method: str, 
              uri: str, 
              *,
              params: dict|None =None, 
              data: dict|None = None, 
              json: dict|None = None, 
              headers:dict | None=None,
              ) -> dict:
    response = _make_call(method, uri, params=params, data=data, json=json, headers=headers)
    return response.json()
