from .app import run


def test_run() -> None:
    assert run("GET", "/users") == {"users": [{"id": "001", "name": "user1"}]}
    assert run("GET", "/users/100") == {"id": "100", "name": "user100"}
    assert run("HEAD", "/users") == {"error_code": "MethodNotAllowed"}
    assert run("GET", "/items") == {"error_code": "ResourceNotFound"}
