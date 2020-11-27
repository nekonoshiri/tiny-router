from typing import Any, Callable, Dict

from tiny_router import SimpleRouter

Route = Callable[[], Dict[str, Any]]

router = SimpleRouter[Route]()


@router.get("/users")
def list_users() -> Any:
    users = [{"id": "001", "name": "user1"}]
    return {"users": users}
