from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Request:
    path_parameters: Dict[str, Any]
    body: str
