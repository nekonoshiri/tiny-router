import json

from .app import run
from .request import Request


def test_get_user() -> None:
    response = run("GET", "/users/{user_id}", Request({"user_id": "001"}, ""))
    assert response.status_code == 200
    assert json.loads(response.body) == {"id": "001", "name": "Alice"}


def test_create_user() -> None:
    response = run("POST", "/users", Request({}, json.dumps({"name": "Bob"})))
    assert response.status_code == 201
    assert json.loads(response.body) == {"id": "002", "name": "Bob"}


def test_method_not_allowed() -> None:
    response = run("DELETE", "/users/{user_id}", Request({"user_id": "001"}, ""))
    assert response.status_code == 405
    assert json.loads(response.body) == {"message": "Method not allowed"}


def test_resource_not_found() -> None:
    response = run("GET", "/items", Request({}, ""))
    assert response.status_code == 404
    assert json.loads(response.body) == {"message": "Resource not found"}
