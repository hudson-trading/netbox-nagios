import json
import socket

TIMEOUT = 3  # seconds
BUFFER_SIZE = 4096  # bytes


def hoststatus(hostname: str, livestatus_host: str, livestatus_port: int):
    """Fetches livestatus from Nagios about hostname."""
    query = (
        "GET hosts\n"
        + "Filter: host_name = %s\n" % hostname  #
        + "OutputFormat: json\n"
    )

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)
    s.connect((livestatus_host, livestatus_port))
    s.sendall(query.encode("utf-8"))
    s.shutdown(socket.SHUT_WR)

    data = []
    while True:
        buf_data = s.recv(BUFFER_SIZE)
        if not buf_data:
            break
        data.append(buf_data)
    s.close()

    if not data:
        return None
    data = json.loads(b"".join(data))

    if not data or len(data) <= 1:
        return None
    return dict(zip(data[0], data[1]))
