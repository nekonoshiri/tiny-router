from typing import Any, Callable

from tiny_router import SimpleRouter

Route = Callable[[], Any]

router = SimpleRouter[Route]()


@router.post("/users")
def create_user() -> Any:
    new_user = {"id": 2, "name": "user2"}
    return {"id": new_user["id"]}
