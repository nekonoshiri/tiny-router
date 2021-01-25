from typing import Callable

from tiny_router.simple_regex import SimpleRegexRouter

from .request import Request
from .response import Response

ResolvedRoute = Callable[[Request], Response]


class Router(SimpleRegexRouter[ResolvedRoute]):
    def __init__(self) -> None:
        super().__init__(matching_precedence="last-in")
