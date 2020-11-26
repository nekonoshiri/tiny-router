from unittest.mock import sentinel

import pytest

from tiny_router import MethodNotAllowed, ResourceNotFound, RouteNotFound, SimpleRouter


@pytest.fixture
def router():
    router = SimpleRouter()

    @router.get("/users")
    def get_users():
        return "GET_USERS"

    return router


def test_resolve(router):
    route = router.resolve("GET", "/users")
    assert route() == "GET_USERS"


def test_resolve_not_found(router):
    with pytest.raises(MethodNotAllowed) as exc_info:
        router.resolve("DELETE", "/users")
    assert isinstance(exc_info.value, RouteNotFound)

    with pytest.raises(ResourceNotFound) as exc_info:
        router.resolve("GET", "/non-users")
    assert isinstance(exc_info.value, RouteNotFound)


def test_route(router):
    @router.route("OPTIONS", "/path")
    def route():
        return sentinel

    assert router.resolve("OPTIONS", "/path")() == sentinel


def test_get(router):
    @router.get("/path")
    def route():
        return sentinel

    assert router.resolve("GET", "/path")() == sentinel


def test_post(router):
    @router.post("/path")
    def route():
        return sentinel

    assert router.resolve("POST", "/path")() == sentinel


def test_put(router):
    @router.put("/path")
    def route():
        return sentinel

    assert router.resolve("PUT", "/path")() == sentinel


def test_patch(router):
    @router.patch("/path")
    def route():
        return sentinel

    assert router.resolve("PATCH", "/path")() == sentinel


def test_delete(router):
    @router.delete("/path")
    def route():
        return sentinel

    assert router.resolve("DELETE", "/path")() == sentinel


def test_head(router):
    @router.head("/path")
    def route():
        return sentinel

    assert router.resolve("HEAD", "/path")() == sentinel
