from typing import Any, Dict

from ..router import Router

router = Router()


@router.get("/users")
def list_users() -> Dict[str, Any]:
    users = [{"id": "001", "name": "user1"}]
    return {"users": users}
