from dataclasses import dataclass


@dataclass
class Response:
    status_code: int
    body: str
