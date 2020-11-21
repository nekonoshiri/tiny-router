from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

Route = TypeVar("Route")


class Routes(ABC, Generic[Route]):
    @abstractmethod
    def merge(self, routes: Routes[Route]) -> Routes[Route]:
        ...

    @abstractmethod
    def resolve(self, method: str, resource: str) -> Route:
        ...

    @abstractmethod
    def add(self, method: str, resource: str, route: Route) -> None:
        ...
