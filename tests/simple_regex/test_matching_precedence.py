from tiny_router import SimpleRegexRouter


def set_router(router):
    @router.get(r"/users/.*")
    def get_user(match):
        def _get_user():
            return "USER"

        return _get_user

    @router.get("/users/me")
    def get_me(match):
        def _get_me():
            return "ME"

        return _get_me


def test_first_in():
    router = SimpleRegexRouter(matching_precedence="first-in")
    set_router(router)

    assert router.resolve("GET", "/users/100")() == "USER"
    assert router.resolve("GET", "/users/me")() == "USER"


def test_last_in():
    router = SimpleRegexRouter(matching_precedence="last-in")
    set_router(router)

    assert router.resolve("GET", "/users/100")() == "USER"
    assert router.resolve("GET", "/users/me")() == "ME"
