from __future__ import annotations

from typing import Dict, Generic, TypeVar

from ..exceptions import MethodNotAllowed, ResourceNotFound

Route = TypeVar("Route")


class MethodMapping(Dict[str, Route]):
    def resolve(self, method: str) -> Route:
        try:
            return self[method]
        except KeyError:
            raise MethodNotAllowed(method) from None

    def add(self, method: str, route: Route) -> None:
        self[method] = route

    def merge(self, other: MethodMapping[Route]) -> MethodMapping[Route]:
        return MethodMapping({**self, **other})


class ResourceMapping(Dict[str, MethodMapping[Route]]):
    def resolve(self, resource: str) -> MethodMapping[Route]:
        try:
            return self[resource]
        except KeyError:
            raise ResourceNotFound(resource) from None

    def add(self, resource: str, method: str, route: Route) -> None:
        if resource not in self:
            self[resource] = MethodMapping()
        self[resource].add(method, route)

    def merge(self, other: ResourceMapping[Route]) -> ResourceMapping[Route]:
        result = ResourceMapping(self)
        for resource, mapping in other.items():
            result[resource] = result.get(resource, MethodMapping()).merge(mapping)
        return result


class SimpleRoutes(Generic[Route]):
    def __init__(self) -> None:
        self._resource_mapping: ResourceMapping[Route] = ResourceMapping()

    def merge(self, other: SimpleRoutes[Route]) -> SimpleRoutes[Route]:
        result: SimpleRoutes[Route] = SimpleRoutes()
        result._resource_mapping = self._resource_mapping.merge(other._resource_mapping)
        return result

    def resolve(self, method: str, resource: str) -> Route:
        return self._resource_mapping.resolve(resource).resolve(method)

    def add(self, method: str, resource: str, route: Route) -> None:
        self._resource_mapping.add(resource, method, route)
