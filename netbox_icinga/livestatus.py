import json
import socket
import requests

TIMEOUT = 3  # seconds
BUFFER_SIZE = 4096  # bytes


def hoststatus(hostname: str, livestatus_host: str, livestatus_port: int):
    """Fetches livestatus from icinga about hostname."""
    url = 'https://' + livestatus_host + ':' + str(livestatus_port) + '/v1/objects/hosts/' + hostname
    data = requests.get(url, auth=('icingaweb', 'icingaweb'), verify=False)

    if not data:
        return None
    
    parsed_data = data.json()
    return parsed_data
hoststatus("icinga2", "localhost", 5665)
