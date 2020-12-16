from typing import Any, Callable, Dict

from tiny_router import SimpleRegexRouter

ResolvedRoute = Callable[[], Dict[str, Any]]


class Router(SimpleRegexRouter[ResolvedRoute]):
    def __init__(self) -> None:
        super().__init__(matching_precedence="last-in")
