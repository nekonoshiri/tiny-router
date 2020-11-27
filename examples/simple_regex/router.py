from typing import Any, Dict

from tiny_router import SimpleRegexRouter

RouteResponse = Dict[str, Any]


def Router() -> SimpleRegexRouter[RouteResponse]:
    return SimpleRegexRouter[RouteResponse](resource_resolver="last-in")
