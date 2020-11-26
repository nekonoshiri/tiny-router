from __future__ import annotations

import re
from typing import TYPE_CHECKING, Callable, Dict, Match, Pattern, TypeVar

from ..exceptions import MethodNotAllowed

if TYPE_CHECKING:
    # mypy doesn't support typing.OrderedDict
    from collections import OrderedDict
else:
    # Python 3.7 and 3.8 don't support collections.OrderedDict[K, V]
    from typing import OrderedDict


RouteResponse = TypeVar("RouteResponse")

Route = Callable[[Match[str]], RouteResponse]


class MethodMapping(Dict[str, Route[RouteResponse]]):
    def resolve(self, method: str) -> Route[RouteResponse]:
        try:
            return self[method]
        except KeyError:
            raise MethodNotAllowed(method) from None

    def add(self, method: str, route: Route[RouteResponse]) -> None:
        self[method] = route

    def merge(
        self, other: MethodMapping[RouteResponse]
    ) -> MethodMapping[RouteResponse]:
        return MethodMapping({**self, **other})


class ResourceMapping(OrderedDict[Pattern[str], MethodMapping[RouteResponse]]):
    def add(self, resource: str, method: str, route: Route[RouteResponse]) -> None:
        pattern = re.compile(resource)
        if pattern not in self:
            self[pattern] = MethodMapping()
        self[pattern].add(method, route)

    def merge(
        self, other: ResourceMapping[RouteResponse]
    ) -> ResourceMapping[RouteResponse]:
        result = ResourceMapping(self)
        for pattern, method_mapping in other.items():
            result[pattern] = result.get(pattern, MethodMapping()).merge(method_mapping)
        return result
