import pytest

from tiny_router import MethodNotAllowed, ResourceNotFound, SimpleRouter


@pytest.fixture
def router1():
    router1 = SimpleRouter()

    @router1.get("/users")
    def get_users_1():
        return "GET_USERS_1"

    @router1.post("/users")
    def post_users_1():
        return "POST_USERS_1"

    @router1.get("/items")
    def get_items_1():
        return "GET_ITEMS_1"

    @router1.get("/groups")
    def get_groups_1():
        return "GET_GROUPS_1"

    return router1


@pytest.fixture
def router2():
    router2 = SimpleRouter()

    @router2.get("/users")
    def get_users_2():
        return "GET_USERS_2"

    @router2.post("/items")
    def post_items_2():
        return "POST_ITEMS_2"

    @router2.get("/circles")
    def get_circles_2():
        return "GET_CIRCLES_2"

    return router2


def test_include(router1, router2):
    router1.include(router2)
    assert router1.resolve("GET", "/users")() == "GET_USERS_2"
    assert router1.resolve("POST", "/users")() == "POST_USERS_1"
    assert router1.resolve("GET", "/items")() == "GET_ITEMS_1"
    assert router1.resolve("POST", "/items")() == "POST_ITEMS_2"
    assert router1.resolve("GET", "/groups")() == "GET_GROUPS_1"
    with pytest.raises(MethodNotAllowed):
        router1.resolve("POST", "/groups")
    assert router1.resolve("GET", "/circles")() == "GET_CIRCLES_2"
    with pytest.raises(MethodNotAllowed):
        router1.resolve("POST", "/circles")

    with pytest.raises(ResourceNotFound):
        router1.resolve("GET", "/path")
