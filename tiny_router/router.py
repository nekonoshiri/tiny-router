from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Callable, Generic, TypeVar

Self = TypeVar("Self")

Route = TypeVar("Route")

RouteDecorator = Callable[[Route], None]


class Router(ABC, Generic[Route]):
    @abstractmethod
    def include(self: Self, other: Self) -> None:
        ...

    @abstractmethod
    def resolve(self, method: str, resource: str) -> Route:
        ...

    @abstractmethod
    def add(self, method: str, resource: str, route: Route) -> None:
        ...

    def route(self, method: str, resource: str) -> RouteDecorator[Route]:
        def _decorator(route: Route) -> None:
            self.add(method, resource, route)

        return _decorator

    def get(self, resource: str) -> RouteDecorator[Route]:
        return self.route("GET", resource)

    def post(self, resource: str) -> RouteDecorator[Route]:
        return self.route("POST", resource)

    def put(self, resource: str) -> RouteDecorator[Route]:
        return self.route("PUT", resource)

    def patch(self, resource: str) -> RouteDecorator[Route]:
        return self.route("PATCH", resource)

    def delete(self, resource: str) -> RouteDecorator[Route]:
        return self.route("DELETE", resource)

    def head(self, resource: str) -> RouteDecorator[Route]:
        return self.route("HEAD", resource)
