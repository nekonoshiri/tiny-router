import pytest

from tiny_router import MethodNotAllowed, ResourceNotFound, RouteNotFound
from tiny_router.simple_regex import SimpleRegexRouter


@pytest.fixture
def router():
    router = SimpleRegexRouter(matching_precedence="last-in")

    @router.get("/users")
    def get_users(match):
        def _get_users():
            return "GET_USERS"

        return _get_users

    def get_user(match):
        def _get_user():
            user_id = match.group("user_id")
            return f"GET_USER_{user_id}"

        return _get_user

    router.add("GET", r"/users/(?P<user_id>\d+)", get_user)

    return router


def test_resolve(router):
    route = router.resolve("GET", "/users")
    assert route() == "GET_USERS"
    route = router.resolve("GET", "/users/100")
    assert route() == "GET_USER_100"


def test_resolve_not_found(router):
    with pytest.raises(MethodNotAllowed) as exc_info:
        router.resolve("DELETE", "/users/100")
    assert isinstance(exc_info.value, RouteNotFound)

    with pytest.raises(ResourceNotFound) as exc_info:
        router.resolve("GET", "/users/me")
    assert isinstance(exc_info.value, RouteNotFound)
