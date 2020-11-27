from __future__ import annotations

from typing import Callable, Match, TypeVar

from typing_extensions import Literal

from ..router import Router
from .mapping import ResourceMapping
from .resource_resolver import first_in, last_in

RouteResponse = TypeVar("RouteResponse")

Route = Callable[[Match[str]], RouteResponse]
ResolvedRoute = Callable[[], RouteResponse]


class SimpleRegexRouter(Router[Route[RouteResponse], ResolvedRoute[RouteResponse]]):
    def __init__(self, matching_precedence: Literal["first-in", "last-in"]) -> None:
        if matching_precedence == "first-in":
            self._resource_resolver = first_in
        elif matching_precedence == "last-in":
            self._resource_resolver = last_in
        else:
            raise ValueError(f"unknown matching_precedence '{matching_precedence}'")

        self._resource_mapping: ResourceMapping[RouteResponse] = ResourceMapping()

    def include(self, other: SimpleRegexRouter[RouteResponse]) -> None:
        self._resource_mapping = self._resource_mapping.merge(other._resource_mapping)

    def resolve(self, method: str, resource: str) -> ResolvedRoute[RouteResponse]:
        pattern, match = self._resource_resolver(list(self._resource_mapping), resource)
        route = self._resource_mapping[pattern].resolve(method)

        def resolved_route() -> RouteResponse:
            return route(match)

        return resolved_route

    def add(self, method: str, resource: str, route: Route[RouteResponse]) -> None:
        self._resource_mapping.add(resource, method, route)
