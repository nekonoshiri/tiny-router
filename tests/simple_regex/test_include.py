import pytest

from tiny_router import SimpleRegexRouter


@pytest.fixture
def Router():
    return lambda: SimpleRegexRouter(matching_precedence="first-in")


def test_can_resolve_both_routers_routes(Router):
    router = Router()

    @router.get("/users")
    def get_users(match):
        return "GET_USERS"

    another_router = Router()

    @another_router.post("/items")
    def post_items(match):
        return "POST_ITEMS"

    router.include(another_router)

    router.resolve("GET", "/users")() == "GET_USERS"
    router.resolve("POST", "/items")() == "POST_ITEMS"


def test_override_will_occur_when_routes_are_same(Router):
    router = Router()

    @router.get("/path")
    def path(match):
        return "GET_PATH"

    another_router = Router()

    @another_router.get("/path")
    def overriden_path(match):
        return "GET_OVERRIDEN_PATH"

    router.include(another_router)

    router.resolve("GET", "/path")() == "GET_OVERRIDEN_PATH"


def test_override_will_not_occur_when_methods_differ(Router):
    router = Router()

    @router.get("/path")
    def get_path(match):
        return "GET_PATH"

    another_router = Router()

    @another_router.post("/path")
    def post_path(match):
        return "POST_PATH"

    router.include(another_router)

    router.resolve("GET", "/path")() == "GET_PATH"
    router.resolve("POST", "/path")() == "POST_PATH"


def test_override_will_not_occur_when_resources_differ(Router):
    router = Router()

    @router.get("/path1")
    def get_path1(match):
        return "GET_PATH1"

    another_router = Router()

    @another_router.get("/path2")
    def get_path2(match):
        return "GET_PATH2"

    router.include(another_router)

    router.resolve("GET", "/path1")() == "GET_PATH1"
    router.resolve("GET", "/path2")() == "GET_PATH2"
