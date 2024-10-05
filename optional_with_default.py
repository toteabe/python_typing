from typing import Optional

def connect(host: str, port: Optional[int] = None) -> None:
    if port is not None:
        print(f"Connecting to {host} on port {port}")
    else:
        print(f"Connecting to {host} on default port")

connect("localhost")          # Output: Connecting to localhost on default port
connect("localhost", 8080)    # Output: Connecting to localhost on port 8080
