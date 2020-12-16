from __future__ import annotations

from typing import Callable, Match, TypeVar

from typing_extensions import Literal

from ..router import Router
from .mapping import ResourceMapping
from .resource_resolver import first_in, last_in

ResolvedRoute = TypeVar("ResolvedRoute")

Route = Callable[[Match[str]], ResolvedRoute]


class SimpleRegexRouter(Router[Route[ResolvedRoute], ResolvedRoute]):
    def __init__(self, matching_precedence: Literal["first-in", "last-in"]) -> None:
        if matching_precedence == "first-in":
            self._resource_resolver = first_in
        elif matching_precedence == "last-in":
            self._resource_resolver = last_in
        else:
            raise ValueError(f"unknown matching_precedence '{matching_precedence}'")

        self._resource_mapping: ResourceMapping[ResolvedRoute] = ResourceMapping()

    def include(self, other: SimpleRegexRouter[ResolvedRoute]) -> None:
        self._resource_mapping = self._resource_mapping.merge(other._resource_mapping)

    def resolve(self, method: str, resource: str) -> ResolvedRoute:
        pattern, match = self._resource_resolver(list(self._resource_mapping), resource)
        return self._resource_mapping[pattern].resolve(method)(match)

    def add(self, method: str, resource: str, route: Route[ResolvedRoute]) -> None:
        self._resource_mapping.add(resource, method, route)
