from __future__ import annotations

from typing import Callable, Generic, TypeVar

from .routes import Routes

Route = TypeVar("Route")

RouteDecorator = Callable[[Route], None]


class Router(Generic[Route]):
    def __init__(self, routes: Routes[Route]) -> None:
        self.routes = routes

    def include(self, router: Router[Route]) -> None:
        self.routes = self.routes.merge(router.routes)

    def resolve(self, method: str, resource: str) -> Route:
        return self.routes.resolve(method, resource)

    def route(self, method: str, resource: str) -> RouteDecorator[Route]:
        def _decorator(r: Route) -> None:
            self.routes.add(method, resource, r)

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
