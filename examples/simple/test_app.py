from .app import run


def test_run() -> None:
    assert run("GET", "/users") == {"users": [{"id": "001", "name": "user1"}]}
    assert run("POST", "/users") == {"id": "002"}
    assert run("HEAD", "/users") == {"error_code": "MethodNotAllowed"}
    assert run("GET", "/items") == {"error_code": "ResourceNotFound"}
