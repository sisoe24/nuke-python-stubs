# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from nukescripts import utils as utils

HOST: str
PORT: int

class client:
    """Example of running an IPV6 socket client to create nodes in Nuke.

    from nukescripts import clientserver
    c = clientserver.client()
    c.send("Blur")
    """
    def __init__(self, host: str = ..., port: Any = ...) -> None: ...
    def close(self) -> None: ...
    def send(self, msg: Any) -> None: ...

class server:
    """Example of running an IPV6 socket server on a separate thread inside Nuke.
    The default command is to create the named node.

    from nukescripts import clientserver
    clientserver.threaded_server()
    """
    def __init__(self, host: str = ..., port: Any = ...) -> None: ...
    def start(self) -> None: ...

def start_server(host: str = ..., port: Any = ...) -> None: ...

def threaded_server() -> None: ...
