from typing import Any, Callable

from tiny_router import SimpleRouter

Route = Callable[[], Any]

router = SimpleRouter[Route]()


@router.get("/users")
def list_users() -> Any:
    users = [{"id": 1, "name": "user1"}]
    return {"users": users}
