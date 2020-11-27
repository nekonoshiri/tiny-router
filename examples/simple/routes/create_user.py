from typing import Any, Callable, Dict

from tiny_router import SimpleRouter

Route = Callable[[], Dict[str, Any]]

router = SimpleRouter[Route]()


@router.post("/users")
def create_user() -> Any:
    new_user = {"id": "002", "name": "user2"}
    return {"id": new_user["id"]}
