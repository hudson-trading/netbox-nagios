import json
import socket
import requests

TIMEOUT = 3  # seconds
BUFFER_SIZE = 4096  # bytes


def hoststatus(hostname: str, icinga_base_url: str, livestatus_port: int):
    """Fetches livestatus from icinga about hostname."""
    url = 'https://' + icinga_base_url + ':' + str(livestatus_port) + '/v1/objects/services?host=' + hostname
    data = requests.get(url, auth=('icingaweb', 'icingaweb'), verify=False)

    if not data:
        return None
    
    parsed_data = data.json()
    return parsed_data
