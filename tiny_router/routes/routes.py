from __future__ import annotations

from typing import Protocol, TypeVar

Route = TypeVar("Route")


class Routes(Protocol[Route]):
    def merge(self, routes: Routes[Route]) -> Routes[Route]:
        ...

    def resolve(self, method: str, resource: str) -> Route:
        ...

    def add(self, method: str, resource: str, route: Route) -> None:
        ...
